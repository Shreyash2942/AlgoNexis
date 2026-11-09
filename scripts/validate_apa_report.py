"""Validate the APA Word formatting contract and the optional native PDF preview."""

import argparse
import json

from performance.benchmark import ROOT
from scripts.build_apa_report import FIGURES, REFERENCES, body_sections
from scripts.build_report import report_values


def validate(*, preview: bool = False) -> dict:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.shared import Inches, Pt

    doc = Document(ROOT / 'documentation/performance_analysis_report.docx')
    normal = doc.styles['Normal']
    assert normal.font.name == 'Times New Roman' and normal.font.size == Pt(12)
    assert normal.paragraph_format.line_spacing == 2
    assert normal.paragraph_format.first_line_indent == Inches(.5)
    assert normal.paragraph_format.alignment == WD_ALIGN_PARAGRAPH.LEFT
    assert normal.paragraph_format.space_before == normal.paragraph_format.space_after == Pt(0)
    for name in ('APA Title', 'APA Heading 1'):
        style = doc.styles[name]
        assert style.font.name == 'Times New Roman' and style.font.size == Pt(12) and style.font.bold
        assert style.paragraph_format.alignment == WD_ALIGN_PARAGRAPH.CENTER
        assert 'asciiTheme' not in style._element.xml and 'pBdr' not in style._element.xml
    for section in doc.sections:
        assert section.page_width == Inches(8.5) and section.page_height == Inches(11)
        assert all(margin == Inches(1) for margin in (section.top_margin, section.bottom_margin,
                                                    section.left_margin, section.right_margin))
    assert doc.sections[0].header.paragraphs[0].alignment == WD_ALIGN_PARAGRAPH.RIGHT
    assert 'PAGE' in doc.sections[0].header._element.xml
    assert len(doc.inline_shapes) == len(FIGURES) == 5
    paragraphs = doc.paragraphs
    strings = [p.text for p in paragraphs]
    reference_index = strings.index('References')
    references = paragraphs[reference_index + 1:reference_index + 1 + len(REFERENCES)]
    assert len(references) == 8
    for paragraph, expected in zip(references, REFERENCES):
        assert paragraph.text == ''.join(expected)
        assert paragraph.paragraph_format.left_indent == Inches(.5)
        assert paragraph.paragraph_format.first_line_indent == Inches(-.5)
        assert paragraph.runs[1].italic is True
    body_text = '\n'.join(strings[:reference_index])
    for _, source_paragraphs in body_sections(report_values()):
        for paragraph in source_paragraphs:
            assert paragraph.replace('\n', ' ') in body_text, 'Analysis differs from current measured values.'
    assert 'BST_PLACEHOLDER' not in body_text and '{{' not in body_text
    captions = [p for p in paragraphs if p.text in [f'Figure {i}' for i in range(1, 6)]]
    assert [p.text for p in captions] == [f'Figure {i}' for i in range(1, 6)]
    assert all(p.runs[0].bold for p in captions)
    assert strings.index('Figure 1') > reference_index
    for _, title, _ in FIGURES:
        paragraph = next(p for p in paragraphs if p.text == title)
        assert paragraph.runs[0].italic
    # Each same-author n.d. suffix follows title order in this APA edition.
    assert 'Sedgewick and Wayne (n.d.-b) likewise' in body_text
    assert 'Sedgewick and Wayne (n.d.-a) document' in body_text
    result = {'format': 'APA 7 student paper', 'figures': 5, 'references': 8,
              'title_page_prompts': [text for text in strings[:8] if text.startswith('[')]}
    if preview:
        import pymupdf
        with pymupdf.open(ROOT / 'documentation/performance_analysis_report_apa.pdf') as pdf:
            texts = [page.get_text() for page in pdf]
            reference_page = next(i for i, text in enumerate(texts)
                                  if any(line.strip() == 'References' for line in text.splitlines()))
            body_pages = sum(len(text.split()) >= 150 for text in texts[1:reference_page])
            assert body_pages >= 5
            assert sum(bool(page.get_images()) for page in pdf) == 5
            assert not any('BST_PLACEHOLDER' in text or '{{' in text for text in texts)
            for i, page in enumerate(pdf):
                assert str(i + 1) in page.get_text().split(), f'Page number missing on page {i + 1}.'
            for page in list(pdf)[:reference_page + 1]:
                for block in page.get_text('dict')['blocks']:
                    for line in block.get('lines', []):
                        for span in line['spans']:
                            if span['text'].strip():
                                assert span['font'].startswith('TimesNewRoman'), span['font']
            result.update(pdf_pages=len(pdf), substantive_text_pages=body_pages)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview', action='store_true', help='Also check the Word-rendered PDF.')
    print(json.dumps(validate(preview=parser.parse_args().preview), indent=2))
