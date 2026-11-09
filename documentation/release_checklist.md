# AlgoNexis v1.0.0 release checklist

G4 evidence is recorded in [day4_verification.md](day4_verification.md). The
eight required deliverables map to actual artifacts below.

| # | Deliverable | Evidence |
|---|---|---|
| 1 | Bubble Sort and visualization | `algorithms/bubble_sort.py`, `visualization/sorting_visualizer.py`, event reconstruction tests, real UI stepper |
| 2 | Quickselect | `algorithms/quickselect.py`; rank/oracle, pivot, validation, and nonmutation tests |
| 3 | Custom Set | `data_structures/custom_set.py`, algebra tests, [operations guide](data_structures.md) |
| 4 | Integrated portfolio | Five additional structures, `data_structures/manager.py`, registry tests and UI operations |
| 5 | Interactive application | `app.py`, four UI sections, AppTest coverage, Edge walkthrough and authentic screenshots |
| 6 | Substantive report | [10-page PDF](performance_analysis_report.pdf), eight body pages, actual measured results and attributed sources |
| 7 | Presentation | [12-slide PPTX](portfolio_presentation.pptx), [native PDF preview](portfolio_presentation_preview.pdf), [speaker script](presentation_walkthrough.md) |
| 8 | Complete documentation | Root README, [architecture](architecture.md), [user guide](../guide.md), [structure contracts](data_structures.md), [methodology](benchmark_methodology.md) |

Release checks:

- [x] All 195 tests pass in a fresh installed environment; compilation and pip
  dependency checks pass.
- [x] Default data has 1,080 measured observations and eight explicit guard skips;
  the separate controlled collision profile has 60 observations.
- [x] Summary groups retain separate units/capacities; plotted mean/min/max values
  come from CSVs; manifest hashes bind the evidence together.
- [x] PDF opens with eight substantive body pages; report content and slide values
  use the same summaries. PowerPoint opens the deck and exports twelve slides.
- [x] The local app launches and passes a real Edge walkthrough. Failure paths,
  step replay, structure operations, reset, charts, and CSV download are checked.
- [x] The walkthrough script maps all requirements; slide order, fonts, charts,
  authentic screenshots, and rendered layouts have been reviewed. This is a
  scripted/browser rehearsal, not a claim of human oral delivery.
- [x] [Retrospective](retrospective.md) records outcomes, resolved challenges,
  limitations, and three realistic future improvements.
- [x] Source, dependency locks, provenance, docs, and all intended artifacts are
  included; environment folders, caches, secrets, scratch files, and generated
  slide PNG previews are excluded from Git.

No single-archive requirement was supplied, so ZIP packaging is not applicable.
Release order: finish checks, commit the fourth Day 4 change, verify a clean clone,
then create annotated tag `v1.0.0` and push `main` plus the tag. The tag identifies
the complete committed portfolio; measured-source revision remains recorded
separately in each benchmark sidecar. The Day 4 work is represented by four
meaningful commits; `git log --oneline c44dd50..v1.0.0` shows their exact hashes.
