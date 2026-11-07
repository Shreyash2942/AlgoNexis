"""Validate complete trial coverage, source provenance, and optional release artifacts."""

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path

from performance.benchmark import OPERATIONS, STRUCTURES, load_rows

ROOT = Path(__file__).resolve().parents[1]


def verify_measurements(csv_path: Path, *, root: Path = ROOT) -> dict:
    rows = load_rows(csv_path)
    metadata = json.loads(csv_path.with_suffix('.environment.json').read_text(encoding='utf-8'))
    config = metadata['config']
    expected = Counter()
    for n in config['sizes']:
        cases = [(name, pattern) for pattern in config['patterns']
                 for name in config['algorithms'] + (list(STRUCTURES) if config['include_structures'] else [])]
        if config['include_structures']:
            cases.append(('graph', 'path'))
        for name, pattern in cases:
            if name in ('bubble_sort', 'bst') and n > 1000:
                expected[(name, n, pattern, 0, 'skipped')] += 1
            else:
                for trial in range(1, config['trials'] + 1):
                    for kind in ('timing', 'memory'):
                        expected[(name, n, pattern, trial, kind)] += 1
    actual = Counter((r['algorithm_or_structure'], r['input_size'], r['input_pattern'],
                      r['trial'], r['measurement']) for r in rows)
    if actual != expected:
        raise ValueError('Trial coverage differs from the configured workload matrix.')
    for row in rows:
        for field in ('run_id', 'source_digest', 'implementation_revision', 'python_version', 'seed'):
            reference = config['seed'] if field == 'seed' else metadata[field]
            if row[field] != reference:
                raise ValueError(f'Observation provenance mismatch: {field}.')
        name = row['algorithm_or_structure']
        if row['operation'] != OPERATIONS[name]:
            raise ValueError('Incorrect operation label.')
        if name == 'quickselect' and (row['k'] != (row['input_size'] + 1) // 2 or
                                     row['pivot_seed'] != config['seed'] + row['trial']):
            raise ValueError('Incorrect Quickselect rank or pivot seed.')
        if name == 'hash_table' and row['hash_capacity'] != max(8, 2 * row['input_size']):
            raise ValueError('Incorrect hash capacity.')
    sources = metadata['source_sha256']
    if sha256(json.dumps(sources, sort_keys=True).encode()).hexdigest() != metadata['source_digest']:
        raise ValueError('Source manifest digest mismatch.')
    for relative, digest in sources.items():
        if sha256((root / relative).read_bytes()).hexdigest() != digest:
            raise ValueError(f'Measured source changed: {relative}.')
    observed = sum(r['status'] == 'ok' for r in rows)
    skipped = len(rows) - observed
    if observed != metadata['observed_rows'] or skipped != metadata['skipped_cases']:
        raise ValueError('Metadata row totals disagree with CSV.')
    return {'run_id': metadata['run_id'], 'observed_rows': observed, 'skipped_cases': skipped,
            'source_digest': metadata['source_digest']}


def verify_artifacts(root: Path = ROOT) -> dict:
    # These dependencies belong only to requirements-report.txt, never to core imports.
    import pymupdf
    from pptx import Presentation

    docs = root / 'documentation'
    with pymupdf.open(docs / 'performance_analysis_report.pdf') as report:
        substantive = [page for page in report if len(page.get_text().split()) >= 180
                       and 'References' not in page.get_text().splitlines()[:5]
                       and 'Portfolio performance analysis' not in page.get_text().splitlines()[:5]]
        if len(substantive) < 5:
            raise ValueError('Fewer than five substantive report pages.')
        pages = len(report)
    slides = Presentation(docs / 'portfolio_presentation.pptx')
    if not 10 <= len(slides.slides) <= 12:
        raise ValueError('Presentation must contain 10–12 slides.')
    for slide in slides.slides:
        if not slide.has_notes_slide or not slide.notes_slide.notes_text_frame.text.strip():
            raise ValueError('A presentation slide is missing speaker notes.')
        for shape in slide.shapes:
            if (shape.left < 0 or shape.top < 0 or shape.left + shape.width > slides.slide_width + 100
                    or shape.top + shape.height > slides.slide_height + 100):
                raise ValueError('A slide shape extends beyond the canvas.')
    manifest = json.loads((root / 'results/analysis_manifest.json').read_text(encoding='utf-8'))
    for relative, digest in manifest['files_sha256'].items():
        if sha256((root / relative).read_bytes()).hexdigest() != digest:
            raise ValueError(f'Analysis evidence changed: {relative}.')
    return {'report_pages': pages, 'substantive_pages': len(substantive), 'slides': len(slides.slides)}


def verify_collisions(root: Path = ROOT) -> int:
    path = root / 'results/hash_collision_results.csv'
    rows = load_rows(path)
    metadata = json.loads(path.with_suffix('.environment.json').read_text(encoding='utf-8'))
    expected = Counter((n, c, trial, kind) for n in (10, 100, 1000) for c in (1, 2*n)
                       for trial in range(1, 6) for kind in ('timing', 'memory'))
    actual = Counter((r['input_size'], r['hash_capacity'], r['trial'], r['measurement']) for r in rows)
    if actual != expected or len(rows) != metadata['observed_rows']:
        raise ValueError('Controlled hash trial coverage differs from its design.')
    for row in rows:
        if (row['run_id'] != metadata['run_id'] or row['status'] != 'ok' or
                row['input_pattern'] != 'unique_integer_keys' or row['fixture_items'] != row['input_size'] or
                row['algorithm_or_structure'] != 'hash_table' or row['operation'] != 'find_all' or
                row['source_digest'] != metadata['source_digest']):
            raise ValueError('Controlled hash provenance or workload mismatch.')
    if sha256((root / 'scripts/measure_hash_collisions.py').read_bytes()).hexdigest() != metadata['script_sha256']:
        raise ValueError('Controlled measurement script changed.')
    for relative, digest in metadata['source_sha256'].items():
        if sha256((root / relative).read_bytes()).hexdigest() != digest:
            raise ValueError(f'Controlled experiment source changed: {relative}.')
    return len(rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifacts', action='store_true')
    args = parser.parse_args()
    result = verify_measurements(ROOT / 'results/benchmark_results.csv')
    if (ROOT / 'results/hash_collision_results.csv').exists():
        result['supplemental_observations'] = verify_collisions()
    if args.artifacts:
        result.update(verify_artifacts())
    print(json.dumps(result, indent=2))
