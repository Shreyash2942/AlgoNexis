"""Generate exportable scientific figures and summaries from recorded CSVs only."""

import csv
from hashlib import sha256
import json
from pathlib import Path

from performance.benchmark import ROOT, load_rows
from performance.summary import summarize
from scripts.validate_release import verify_collisions, verify_measurements


def run() -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    evidence = verify_measurements(ROOT / 'results/benchmark_results.csv')
    supplemental_observations = verify_collisions()
    main = summarize(load_rows(ROOT / 'results/benchmark_results.csv'))
    collision = summarize(load_rows(ROOT / 'results/hash_collision_results.csv'))
    summaries = main + collision
    target = ROOT / 'results'
    (target / 'figures').mkdir(exist_ok=True)
    (target / 'summary_statistics.json').write_text(json.dumps(summaries, indent=2), encoding='utf-8')
    with (target / 'summary_statistics.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summaries[0]))
        writer.writeheader()
        writer.writerows(summaries)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'savefig.facecolor': 'white'})
    colors = ['#0b7c78', '#263c62', '#cc6e29', '#9473a6']

    def chart(filename, title, series, ylabel, log_y=True):
        fig, ax = plt.subplots(figsize=(8.3, 4.2), layout='constrained')
        for index, (label, rows) in enumerate(series):
            rows = sorted(rows, key=lambda row: row['input_size'])
            if not rows:
                raise ValueError(f'Missing figure data: {filename}/{label}')
            x, y = [r['input_size'] for r in rows], [r['mean'] for r in rows]
            ax.errorbar(x, y, yerr=([r['mean']-r['minimum'] for r in rows],
                                   [r['maximum']-r['mean'] for r in rows]),
                        label=label, color=colors[index], marker='o', capsize=3, linewidth=2)
        ax.set_xscale('log')
        if log_y:
            ax.set_yscale('log')
        ax.set(xlabel='Input elements (n; logarithmic scale)', ylabel=ylabel,
               title=title + '\nMean; whiskers = observed min–max; 5 trials')
        ax.grid(alpha=.2, which='major')
        ax.legend(frameon=False, fontsize=10)
        for extension in ('png', 'svg'):
            fig.savefig(target / 'figures' / f'{filename}.{extension}', dpi=180)
        plt.close(fig)

    def selected(name, pattern, kind='timing'):
        return [r for r in main if r['algorithm_or_structure'] == name and
                r['input_pattern'] == pattern and r['measurement'] == kind]

    patterns = ['random', 'sorted', 'reverse', 'duplicates']
    for name, title in [('bubble_sort', 'Bubble Sort: complete ordering, tracing disabled'),
                        ('quickselect', 'Quickselect: one middle rank, randomized pivots'),
                        ('bst', 'Unbalanced BST: find every input value (prebuilt tree)')]:
        chart(name, title, [(p, selected(name, p)) for p in patterns], 'Elapsed time (ms; log scale)')
    chart('hash_collisions', 'Hash lookup batch: explicit bucket-capacity experiment',
          [(label, [r for r in collision if r['measurement'] == 'timing' and
                    (r['hash_capacity'] == 1) == single])
           for label, single in [('1 bucket: all keys collide', True), ('2n buckets: keys distributed', False)]],
          'Elapsed time (ms; log scale)')
    chart('allocations', 'Random-input operations: incremental Python-tracked peak',
          [(label, selected(name, 'random', 'memory')) for label, name in
           [('Bubble Sort (no trace)', 'bubble_sort'), ('Quickselect', 'quickselect'),
            ('Queue drain (prebuilt)', 'queue'), ('Hash find-all (prebuilt)', 'hash_table')]],
          'Peak Python-tracked bytes (log scale)')
    files = [target / 'benchmark_results.csv', target / 'benchmark_results.environment.json',
             target / 'hardware_environment.json',
             target / 'hash_collision_results.csv', target / 'hash_collision_results.environment.json',
             target / 'summary_statistics.csv', target / 'summary_statistics.json',
             *sorted((target / 'figures').glob('*'))]
    manifest = {**evidence, 'summary_groups': len(summaries),
                'supplemental_observations': supplemental_observations,
                'files_sha256': {p.relative_to(ROOT).as_posix(): sha256(p.read_bytes()).hexdigest() for p in files}}
    (target / 'analysis_manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in manifest.items() if k != 'files_sha256'}, indent=2))


if __name__ == '__main__':
    run()
