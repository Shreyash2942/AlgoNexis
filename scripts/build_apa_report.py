"""Create an APA 7 student-paper DOCX from the verified original report analysis.

Formatting follows APA's Student Paper Setup Guide. Figures are placed on
separate pages after references, an option allowed by APA's Figure Setup guide.
Missing personal/course metadata stays explicit in apa_title_page.json.
"""

import argparse
import json
import re

from performance.benchmark import ROOT
from scripts.build_report import report_values
from scripts.validate_release import verify_measurements, verify_collisions

REFERENCES = [
    ('OpenDSA Project Contributors. (n.d.). ', 'Bubble sort',
     '. In CS3 data structures & algorithms. ',
     'https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/BubbleSort.html'),
    ('Python Software Foundation. (n.d.-a). ', 'collections—Container datatypes',
     '. Python 3.14 documentation. ', 'https://docs.python.org/3.14/library/collections.html'),
    ('Python Software Foundation. (n.d.-b). ', 'time—Time access and conversions',
     '. Python 3.14 documentation. ', 'https://docs.python.org/3.14/library/time.html'),
    ('Python Software Foundation. (n.d.-c). ', 'tracemalloc—Trace memory allocations',
     '. Python 3.14 documentation. ', 'https://docs.python.org/3.14/library/tracemalloc.html'),
    ('Sedgewick, R., & Wayne, K. (n.d.-a). ', 'BreadthFirstPaths.java',
     ' [Source code]. Algorithms, 4th edition companion repository. ',
     'https://github.com/kevin-wayne/algs4/blob/master/src/main/java/edu/princeton/cs/algs4/BreadthFirstPaths.java'),
    ('Sedgewick, R., & Wayne, K. (n.d.-b). ', 'BST.java',
     ' [Source code]. Algorithms, 4th edition companion repository. ',
     'https://github.com/kevin-wayne/algs4/blob/master/src/main/java/edu/princeton/cs/algs4/BST.java'),
    ('Sedgewick, R., & Wayne, K. (n.d.-c). ', 'Quick.java',
     ' [Source code]. Algorithms, 4th edition companion repository. ',
     'https://github.com/kevin-wayne/algs4/blob/master/src/main/java/edu/princeton/cs/algs4/Quick.java'),
    ('Sedgewick, R., & Wayne, K. (n.d.-d). ', 'SeparateChainingHashST.java',
     ' [Source code]. Algorithms, 4th edition companion repository. ',
     'https://github.com/kevin-wayne/algs4/blob/master/src/main/java/edu/princeton/cs/algs4/SeparateChainingHashST.java'),
]

FIGURES = [
    ('bubble_sort', 'Bubble Sort Timing by Input Pattern',
     'Complete ordering with tracing disabled; cases above 1,000 elements are guarded skips.'),
    ('quickselect', 'Quickselect Middle-Rank Timing by Input Pattern',
     'One-based rank k = (n + 1) // 2; duplicates occupy repeated ranks. Selection and sorting perform different tasks.'),
    ('bst', 'Unbalanced Binary Search Tree Search Timing',
     'Every submitted input is searched in a prebuilt unique-integer tree. Repeated keys can reduce the stored fixture size.'),
    ('hash_collisions', 'Controlled Hash Lookup Timing by Bucket Capacity',
     'A separate profile uses keys range(n), capacity 1 versus 2n, and the same successful lookup queries in both profiles.'),
    ('allocations', 'Incremental Python-Tracked Peak Allocation',
     'Random-input operation peaks include returned results and internal copies, exclude prebuilt fixtures, and do not measure resident RAM.'),
]


def body_sections(values: dict) -> list[tuple[str, list[str]]]:
    source = (ROOT / 'documentation/report_template.md').read_text(encoding='utf-8')
    source = re.sub(r'\{\{(\w+)\}\}', lambda match: values[match[1]], source)
    sections = []
    for chunk in source.split('@PAGE')[1:]:
        blocks = chunk.strip().split('\n\n')
        heading = blocks[0].splitlines()[0].removeprefix('# ')
        if heading == 'References':
            break
        paragraphs = [block for block in blocks[1:] if not block.startswith('![')]
        # The shared Day 4 source used a/b in another order; APA letters follow
        # reference-title alphabetization: BreadthFirstPaths before BST.
        paragraphs = [p.replace('Sedgewick and Wayne (n.d.-a)', 'Sedgewick and Wayne (BST_PLACEHOLDER)')
                      .replace('Sedgewick and Wayne (n.d.-b)', 'Sedgewick and Wayne (n.d.-a)')
                      .replace('BST_PLACEHOLDER', 'n.d.-b') for p in paragraphs]
        paragraphs = [p.replace('Figure 2, supplied separately in results/figures/quickselect.png, displays',
                                 'Figure 2 displays')
                       .replace('Figure 4 (results/figures/hash_collisions.png)', 'Figure 4') for p in paragraphs]
        number = int(heading.split('.')[0])
        if number == 5:
            paragraphs.insert(0, 'Figures 1 and 2 show the measured timing profiles for complete ordering and middle-rank selection, respectively.')
        if number == 6:
            paragraphs.insert(0, 'Figure 3 shows successful search batches for the unbalanced tree. Figure 4 presents the separate controlled hash-capacity experiment.')
        if number == 7:
            paragraphs.insert(0, 'Figure 5 shows incremental operation-allocation peaks for four random-input workloads.')
        sections.append((heading, paragraphs))
    return sections


def build(metadata: dict) -> None:
    from docx import Document
    from docx.enum.style import WD_STYLE_TYPE
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor

    verify_measurements(ROOT / 'results/benchmark_results.csv')
    verify_collisions()
    values = report_values()
    document = Document()
    section = document.sections[0]
    section.page_width, section.page_height = Inches(8.5), Inches(11)
    section.top_margin = section.bottom_margin = section.left_margin = section.right_margin = Inches(1)
    section.header_distance = section.footer_distance = Inches(.5)
    normal = document.styles['Normal']
    normal.font.name = 'Times New Roman'
    normal.font.size = Pt(12)
    normal.font.color.rgb = RGBColor(0, 0, 0)
    normal.paragraph_format.line_spacing = 2
    normal.paragraph_format.space_before = normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.first_line_indent = Inches(.5)
    normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    normal.paragraph_format.widow_control = True
    for name in ('APA Title', 'APA Heading 1'):
        # Fresh styles avoid the stock template's theme fonts and title rule.
        style = document.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        style.base_style = normal
        style.font.name, style.font.size = 'Times New Roman', Pt(12)
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.font.bold = True
        style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        style.paragraph_format.first_line_indent = Inches(0)
        style.paragraph_format.space_before = style.paragraph_format.space_after = Pt(0)
        style.paragraph_format.line_spacing = 2
        style.paragraph_format.keep_with_next = True

    header = section.header.paragraphs[0]
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    header.paragraph_format.first_line_indent = Inches(0)
    field = OxmlElement('w:fldSimple')
    field.set(qn('w:instr'), 'PAGE')
    run = OxmlElement('w:r')
    text = OxmlElement('w:t')
    text.text = '1'
    run.append(text); field.append(run); header._p.append(field)

    title = document.add_paragraph(metadata['title'], 'APA Title')
    title.paragraph_format.space_before = Pt(72)
    title.paragraph_format.space_after = Pt(24)
    for key in ('author', 'affiliation', 'course', 'instructor', 'due_date'):
        paragraph = document.add_paragraph(metadata[key])
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        paragraph.paragraph_format.first_line_indent = Inches(0)
    document.add_page_break()
    document.add_paragraph(metadata['title'], 'APA Title')
    headings = ['Purpose, Scope, and Evidence', 'Algorithms and the Cost of Explanation',
                'Structures, Representations, and Contracts', 'Measurement Method and Reproducibility',
                'Ordering and Rank-Selection Results', 'Tree Shape and Controlled Hash Collisions',
                'Allocation Evidence and Interpretation', 'Evaluation, Limitations, and Conclusion']
    for index, (_, paragraphs) in enumerate(body_sections(values)):
        if index:
            document.add_paragraph(headings[index], 'APA Heading 1')
        for paragraph in paragraphs:
            document.add_paragraph(paragraph.replace('\n', ' '))

    document.add_page_break()
    document.add_paragraph('References', 'APA Heading 1')
    for prefix, title_text, source, url in REFERENCES:
        paragraph = document.add_paragraph()
        paragraph.paragraph_format.left_indent = Inches(.5)
        paragraph.paragraph_format.first_line_indent = Inches(-.5)
        paragraph.add_run(prefix)
        paragraph.add_run(title_text).italic = True
        paragraph.add_run(source)
        paragraph.add_run(url)

    for number, (filename, title_text, description) in enumerate(FIGURES, start=1):
        document.add_page_break()
        paragraph = document.add_paragraph()
        paragraph.paragraph_format.first_line_indent = Inches(0)
        paragraph.paragraph_format.keep_with_next = True
        paragraph.add_run(f'Figure {number}').bold = True
        paragraph = document.add_paragraph()
        paragraph.paragraph_format.first_line_indent = Inches(0)
        paragraph.paragraph_format.keep_with_next = True
        paragraph.add_run(title_text).italic = True
        paragraph = document.add_paragraph()
        paragraph.paragraph_format.first_line_indent = Inches(0)
        paragraph.add_run().add_picture(str(ROOT / f'results/figures/{filename}.png'), width=Inches(6.5))
        paragraph = document.add_paragraph()
        paragraph.paragraph_format.first_line_indent = Inches(0)
        paragraph.add_run('Note. ').italic = True
        paragraph.add_run(description + ' Lines show observed means; whiskers show observed minimum–maximum across five trials. '
                          'Both axes use logarithmic scaling. Original figures are generated from the recorded CSV observations.')

    document.core_properties.title = metadata['title']
    document.core_properties.author = metadata['author']
    document.core_properties.subject = 'APA 7 student paper; original implementation analysis and measured evidence'
    document.core_properties.comments = 'Title-page placeholders require actual course details. No instructor or due date is invented.'
    output = ROOT / 'documentation/performance_analysis_report.docx'
    document.save(output)
    print(f'Saved APA Word report: {output}')
    missing = [key for key, value in metadata.items() if value.startswith('[')]
    print('Title-page fields still requiring supplied details:', ', '.join(missing) if missing else 'none')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--author')
    parser.add_argument('--instructor')
    parser.add_argument('--due-date')
    args = parser.parse_args()
    metadata = json.loads((ROOT / 'documentation/apa_title_page.json').read_text(encoding='utf-8'))
    for key in ('author', 'instructor', 'due_date'):
        if getattr(args, key) is not None:
            metadata[key] = getattr(args, key)
    build(metadata)
