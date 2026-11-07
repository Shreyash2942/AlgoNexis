"""Render the original authoring template with CSV-derived values into MD and PDF."""

from html import escape
import json
from pathlib import Path
import re

from performance.benchmark import ROOT, load_rows


def report_values() -> dict[str, str]:
    metadata = json.loads((ROOT / 'results/benchmark_results.environment.json').read_text(encoding='utf-8'))
    summaries = json.loads((ROOT / 'results/summary_statistics.json').read_text(encoding='utf-8'))

    def row(name, n, pattern='random', kind='timing', capacity=None):
        matches = [r for r in summaries if r['algorithm_or_structure'] == name and
                   r['input_size'] == n and r['input_pattern'] == pattern and r['measurement'] == kind
                   and (capacity is None or r['hash_capacity'] == capacity)]
        if len(matches) != 1:
            raise ValueError(f'Expected one summary: {name}/{n}/{pattern}/{kind}/{capacity}')
        return matches[0]

    hardware = json.loads((ROOT / 'results/hardware_environment.json').read_text(encoding='utf-8-sig'))
    values = {'observed': f"{metadata['observed_rows']:,}", 'skipped': str(metadata['skipped_cases']),
              'processor': hardware['processor'].strip(), 'ram': f"{hardware['physical_memory_gib']:.2f}",
              'platform': metadata['platform'], 'python': metadata['python_version'], 'run_id': metadata['run_id'],
              **metadata['package_versions']}
    for pattern in ('random', 'sorted', 'reverse', 'duplicates'):
        values[f'bubble_{pattern}'] = f"{row('bubble_sort', 1000, pattern)['mean']:.4f}"
    for key, name, n in [('bubble', 'bubble_sort', 1000), ('select', 'quickselect', 5000)]:
        for short, stat in [('median', 'median'), ('min', 'minimum'), ('max', 'maximum')]:
            values[f'{key}_{short}'] = f"{row(name, n)[stat]:.4f}"
    for pattern in ('random', 'duplicates'):
        values[f'select_{pattern}'] = f"{row('quickselect', 5000, pattern)['mean']:.4f}"
    for pattern in ('random', 'sorted', 'reverse'):
        values[f'bst_{pattern}'] = f"{row('bst', 1000, pattern)['mean']:.4f}"
    values['bst_ratio'] = f"{row('bst', 1000, 'sorted')['mean'] / row('bst', 1000)['mean']:.2f}×"
    for label, capacity in [('collision', 1), ('distributed', 2000)]:
        values[f'hash_{label}'] = f"{row('hash_table', 1000, 'unique_integer_keys', capacity=capacity)['mean']:.4f}"
    values['hash_ratio'] = f"{float(values['hash_collision']) / float(values['hash_distributed']):.2f}×"
    for label, name in [('bubble', 'bubble_sort'), ('select', 'quickselect'), ('queue', 'queue'), ('hash', 'hash_table')]:
        values[f'memory_{label}'] = f"{row(name, 1000, kind='memory')['mean']:,.0f}"
    reverse = next(r for r in load_rows(ROOT / 'results/benchmark_results.csv')
                   if r['algorithm_or_structure'] == 'bubble_sort' and r['input_size'] == 1000
                   and r['input_pattern'] == 'reverse' and r['status'] == 'ok')
    values['reverse_comparisons'] = f"{reverse['comparisons']:,}"
    values['reverse_swaps'] = f"{reverse['swaps']:,}"
    return values


def run() -> None:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak

    values = report_values()
    source = (ROOT / 'documentation/report_template.md').read_text(encoding='utf-8')
    text = re.sub(r'\{\{(\w+)\}\}', lambda match: values[match[1]], source)
    if '{{' in text:
        raise ValueError('Unresolved report data token.')
    target = ROOT / 'documentation/performance_analysis_report'
    target.with_suffix('.md').write_text(text, encoding='utf-8')
    font = 'Times-Roman'
    font_path = Path('C:/Windows/Fonts/times.ttf')
    if font_path.exists():
        pdfmetrics.registerFont(TTFont('PortfolioTimes', str(font_path)))
        font = 'PortfolioTimes'
    body = ParagraphStyle('body', fontName=font, fontSize=11, leading=15,
                          alignment=TA_JUSTIFY, spaceAfter=11, splitLongWords=True)
    heading = ParagraphStyle('heading', fontName=font, fontSize=18, leading=23,
                             textColor=colors.HexColor('#143f4a'), spaceAfter=17)
    caption = ParagraphStyle('caption', parent=body, fontSize=9.5, leading=12, alignment=TA_CENTER)
    refs = ParagraphStyle('refs', parent=body, fontSize=10, leading=14, spaceAfter=14,
                         leftIndent=18, firstLineIndent=-18, alignment=0)
    story = []
    reference_page = False
    for block in text.replace('@PAGE\n', '@PAGE\n\n').strip().split('\n\n'):
        if block == '@PAGE':
            story.append(PageBreak())
        elif block.startswith('# '):
            reference_page = block.startswith('# References')
            story.append(Paragraph(escape(block[2:]), heading))
        elif block.startswith('!['):
            match = re.fullmatch(r'!\[(.*?)\]\((.*?)\)', block)
            story += [Image(str(ROOT / match[2]), width=6.4*inch, height=3.24*inch),
                      Paragraph(escape(match[1]), caption), Spacer(1, 10)]
        else:
            story.append(Paragraph(escape(block).replace('\n', ' '), refs if reference_page else body))

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont(font, 9)
        canvas.setFillColor(colors.HexColor('#52636a'))
        canvas.drawString(52, 29, 'AlgoNexis | CSC506 | Reproducible portfolio analysis')
        canvas.drawRightString(560, 29, str(doc.page))
        canvas.restoreState()

    doc = SimpleDocTemplate(str(target.with_suffix('.pdf')), pagesize=(612, 792),
                            rightMargin=52, leftMargin=52, topMargin=48, bottomMargin=48,
                            title='AlgoNexis performance analysis', author='Shreyash')
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print('Generated report Markdown and PDF from verified summaries.')


if __name__ == '__main__':
    run()
