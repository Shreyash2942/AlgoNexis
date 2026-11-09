# APA Word report setup

The editable Word edition is `performance_analysis_report.docx`; its native Word
export is `performance_analysis_report_apa.pdf`. It reuses the original report's
analysis and actual measured summaries. The ten-page Day 4 PDF and the `v1.0.0`
tag remain the original release artifacts.

## Formatting decisions

This edition follows APA 7 student-paper conventions: U.S. letter paper,
one-inch margins, 12-point Times New Roman, double spacing, left-aligned body
paragraphs with half-inch first-line indents, and automatic page numbers at the
top right. The title page and first text page repeat the paper title. Descriptive
Level 1 headings are centered and bold; the introduction begins under the title
without an “Introduction” heading. No running head or abstract was added because
neither was requested for this student paper.

References have half-inch hanging indents and italicized work titles. Same-author
undated entries use consistent letter suffixes ordered by title: BreadthFirstPaths
precedes BST in this edition, so the matching narrative citations are corrected
together. This formatting change does not revise any measured result.

All five original measured figures are included, numbered in first-mention order,
with bold figure numbers, italic titles, and explanatory notes. Each appears on
its own page after the references, one of APA's permitted placement options.
The notes identify units, observed mean/min–max, five repeats, logarithmic axes,
and allocation/setup limits where relevant.

APA guidance consulted November 8, 2026:

- [Student Paper Setup Guide](https://apastyle.apa.org/instructional-aids/student-paper-setup-guide.pdf)
- [Title Page Setup](https://apastyle.apa.org/style-grammar-guidelines/paper-format/title-page)
- [Figure Setup](https://apastyle.apa.org/style-grammar-guidelines/tables-figures/figures)
- [Webpage References](https://apastyle.apa.org/style-grammar-guidelines/references/examples/webpage-website-references)

These are formatting sources for the Word edition, not extra algorithm references
in the paper. The paper retains its eight verified algorithm/library sources.

## Personalize and rebuild

Edit `apa_title_page.json` with the actual full author name, affiliation/course,
instructor, and assignment due date. Instructor and due-date prompts remain
bracketed unless supplied; the builder does not invent those details. Add a
department/program to the affiliation if required by the course. Metadata can
also be overridden for one build with `--author`, `--instructor`, and `--due-date`.

```powershell
python -m pip install -r requirements-report.lock.txt
python -m scripts.build_apa_report
python -m scripts.validate_apa_report
```

The builder resolves data tokens from the saved measured summaries and checks
default/supplemental source provenance. It uses the existing report authoring
template for prose and constructs APA references/captions explicitly. Word edits
are possible, but regenerating overwrites them; record repeatable changes in the
template, metadata, or builder. Optional python-docx is a documentation dependency
and does not affect launching the app or importing the core algorithms.

Open the DOCX in Microsoft Word and export it as
`performance_analysis_report_apa.pdf` to refresh the native preview. Then run
`python -m scripts.validate_apa_report --preview`. Changing metadata or document
content does not update an already exported PDF automatically. A full app guide is
available in the root [guide.md](../guide.md).
