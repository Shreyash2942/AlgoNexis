# Day 4 verification — November 7, 2026

## Regression gate (D4.1)

The original environment passed 191 existing tests before edits. Four release
evidence tests now verify the complete recorded workload and reject missing
trials, duplicate trials, and a forged source manifest. The expanded suite passed
195 tests in 6.86 seconds in the original environment, then **195 tests in 6.06
seconds** in a newly created environment with installed release dependencies.

Commands executed in the fresh environment:

```powershell
python -m pip install -r requirements.lock.txt -r requirements-report.txt
python -m pytest tests/ -v
python -m compileall -q algorithms data_structures visualization performance ui scripts app.py
python -m pip check
python -m scripts.validate_release
```

Compilation passed, dependency checking reported no broken requirements, and the
evidence validator verified 1,080 observed rows and eight guarded skips against
the actual source hashes. The suite covers both algorithms, Custom Set and five
additional structures, the manager, step sequence reconstruction, bounded input,
navigation, persistence, resets, and measurement/export failure behavior.

### Clean-install issue resolved

Freshly installed pandas 3.1.1 failed to load its parsers extension under this
machine's Windows Application Control policy, both in Temp and the workspace.
The extension's SHA-256 matched the previously working installation. The policy
was not changed. Installing the maintained pandas 3.0.6 wheel succeeded; the full
suite then passed. Requirements and the lock now select the tested 3.0 maintenance
series. This was an environment compatibility defect found by the fresh-install
check, not an algorithm defect. Other report-tool imports also passed.

### Known limits

The BST is unbalanced; the custom hash table has fixed capacity; graph operations
are undirected and unweighted. Full immutable sorting traces can be cubic in
storage/time and are bounded to 50 UI values. Allocation observations exclude
prebuilt fixtures and are Python-tracked peaks, not whole-process RAM. Timing
results are specific to the recorded environment, seeds, and workloads. These
limits are intentional, documented, and exercised within the supported bounds.

## Final observations and analysis (D4.2)

The final default run `c6f11506577d47dc87eddb2fc4391644` records 1,080 observed
rows and eight skips at measured revision `388fbf8`. Its source digest remains
`c41dfbc6a20fda9b7f6d1b0e4a3a6fb7e72de342b6755642a1d5d651ec4b5a87`.
Timing and allocation receive five repeats each. The separately saved controlled
hash study has 60 observations. There are 216 default summary groups and twelve
supplemental groups, with mean/median/min/max and explicit units/capacities.

Five real PNG/SVG figures and CSV/JSON summaries were generated. The validator
checks matrix coverage, trial uniqueness, seeds/ranks, source hashes, and the
controlled capacity design. The analysis manifest hashes raw data, environment,
hardware, summaries, and figures. The report distinguishes tasks, theoretical
bounds, observed spread, repeated-key fixture size, and operation-only allocation.

## Report and presentation (D4.3–D4.4)

PyMuPDF opened the ten-page report. Its eight body pages contain respectively
347, 377, 386, 375, 292, 304, 337, and 374 extracted words; cover and references
are excluded. Text bounds fit the pages. Body, methodology, allocation, and result
pages were visually inspected. Figures use saved measured summaries. The report
uses original third-person analysis and paraphrased primary-source attribution.

Microsoft PowerPoint opened the twelve-slide PPTX read-only without showing an
application window. It exported all twelve slides as PNG and a PDF preview.
Rendered architecture, algorithm, UI, results, and closing layouts were inspected;
the tree/graph/hash wording was shortened to improve fit. The native preview has
twelve pages and no large body text overlapping the footer. All slides have
speaker notes, authentic screenshots/figures, and editable text. Optional script
execution is restricted by this computer's existing PowerShell policy, so the
native export was performed with direct COM commands; policy was not changed.

`presentation_walkthrough.md` maps all requirements to a suggested 8–10 minute
script. Browser/script rehearsal and visual review were completed; human oral
delivery has not been claimed. The supplied native PDF works without Office.

## Browser and final regression (D4.5–D4.6)

The newly installed environment launched Streamlit on localhost:8504. Real
headless Microsoft Edge passed navigation, both algorithms, complete sorting
replay and bounds, invalid numeric input, all six structures, reset, measured
charts, mobile rendering, and an exact full CSV download. Final performance
screenshots were refreshed from the final saved run. The walkthrough used
`--skip-benchmark` to preserve the report's evidence.

After the release scripts and documentation changes, the fresh environment passed
**195 tests in 5.91 seconds**. Compilation, pip dependency checking, and
`python -m scripts.validate_release --artifacts` passed. That validator confirms
the eight substantive report pages, twelve slides, twelve native preview pages,
report data values, figure hashes, and unchanged measured core sources.

A clean local clone plus candidate release files passed 195 tests in 7.36 seconds.
Its evidence check exposed newline conversion in some previously staged generated
JSON/SVG files. The affected files were renormalized under byte-preserving
attributes, and the candidate checkout then passed full artifact/provenance
validation. This protects future Windows/POSIX clones; it changes no measurements.
The committed final clone receives the same regression, artifact, and app checks
before tagging. Final command output is reported with the release.

The candidate checkout also launched Streamlit independently on localhost:8505
and passed the full real Edge walkthrough with saved evidence preserved.

## Gate G4 and release procedure

The [release checklist](release_checklist.md) maps all eight deliverables. The
README, architecture, user guide, structure examples, dependency files, and
retrospective are complete. No archive was requested; ZIP packaging is therefore
not applicable. No critical algorithm or supported-workflow defects remain.
The documented unbalanced-tree, fixed-capacity, graph-scope, input-bound, and
single-machine measurement limits remain explicit.

Day 4 has four meaningful work units: regression/clean-install QA, final measured
analysis, the substantive report, and presentation/release documentation. After
the fourth commit and committed-clone checks, the annotated `v1.0.0` tag is
created and pushed with `main`. `git log --oneline c44dd50..v1.0.0` identifies
the actual four commits. Historical Day 1–3 records retain their original counts.
