# AlgoNexis: start here

AlgoNexis is a local teaching application for Bubble Sort, Quickselect, a Custom
Set, Stack, Queue, Binary Search Tree, Graph, and Hash Table. You can inspect
sorting events, operate on structures, and explore actual benchmark results.

## 1. Install and launch

You need Python and Git to clone the project. The tested release environment is
Python **3.14.4 on Windows**; the source targets Python 3.11+. The lock file records
the tested package versions. Word and PowerPoint are optional viewers, not app
dependencies. Internet access is needed for the initial package installation.

```bash
git clone https://github.com/Shreyash2942/AlgoNexis.git
cd AlgoNexis
python -m venv .venv
```

On Windows PowerShell, run these commands from the project root:

```powershell
& .\.venv\Scripts\python.exe -m pip install -r requirements.lock.txt
& .\.venv\Scripts\python.exe -m streamlit run app.py
```

On macOS or Linux:

```bash
.venv/bin/python -m pip install -r requirements.lock.txt
.venv/bin/python -m streamlit run app.py
```

Open the URL printed in the terminal, usually `http://localhost:8501`. Keep the
terminal running while using the app. Press **Ctrl+C** in that terminal to stop
the server. These commands call the virtual environment directly, so PowerShell
activation scripts are unnecessary. If your Python installation uses `python3`
or `py -3.14`, use that executable for the environment-creation command.

`requirements.txt` lists direct dependency ranges; `requirements.lock.txt` pins
the tested environment, including browser-QA tooling. On a different supported
Python/platform, direct requirements may be more appropriate than the release
lock. The application uses Streamlit, pandas, and Altair; pytest verifies behavior.

## 2. A five-minute tour

1. Open **Dashboard** to see the portfolio scope and sections.
2. Open **Algorithms**, enter `3, 1, 2`, and run **Bubble Sort** with recording
   enabled. The result is `[1, 2, 3]`, with three comparisons and two swaps.
3. Move through the sorting events using **Next**, **Previous**, the slider, and
   **Reset steps**. Initial and final states are included; the index is zero-based.
4. With the same dataset, choose rank `2` and run **Quickselect**. The answer is `2`.
5. Visit **Data Structures**, select a structure and operation, enter its requested
   arguments, and press **Run operation**. Inspect the result and current contents.
6. Visit **Performance Analysis** to view the saved measurements, choose a pattern
   filter, inspect repeat summaries, and download the complete run CSV.

The app preserves dataset, playback, and structure models while navigating in
one browser session. A separate session has independent state. These exploration
models are in memory; closing a session or restarting the app can discard them.
Benchmark CSVs are saved on disk.

## 3. Algorithms and inputs

Enter comma-separated or whitespace-separated integers, for example
`7, 2, 7, -1, 4`. Decimals, bracket expressions, code, and missing comma values
are rejected. No expression evaluation is used. Values must be within ±1 billion;
the text field is limited to 100,000 characters.

| Feature | Example and behavior | Interface limit |
|---|---|---|
| Bubble Sort with steps | `3,1,2` → `[1,2,3]`; inspect every comparison and swap | 50 integers |
| Bubble Sort without steps | Disable recording for execution-only sorting | 1,000 integers |
| Quickselect | `7,2,7,-1,4`, k=3 → `4`; k=4 → `7` | 5,000 integers |

Quickselect uses **one-based** ranks. Duplicates count as repeated positions, and
an empty list or rank larger than the list is invalid. Empty Bubble Sort input is
valid. Both core algorithms preserve the caller's list. Editing the dataset clears
stale results and resets playback; changing only the rank clears selection output.

Compared indices and completed swaps have both color highlights and descriptive
text. Negative bars extend below zero. Recording is bounded because full immutable
snapshots can have O(n³) worst-case storage/time; untraced Bubble Sort has O(n²)
average/worst-case time and O(n) best-case time with its early exit.

## 4. Use all six structures

Select **Data Structures → Structure → Operation**. The form changes to request
the arguments for the selected operation. The table below gives small examples;
perform the additions before the inspections or removals.

| Structure | Try this | Main behavior |
|---|---|---|
| Custom Set | Add `1`, add `2`; union with `2,3` gives `[1,2,3]`; intersection gives `[2]` | Unique membership; derived algebra preserves the stored set |
| Stack | Push `10`, push `20`, then peek/pop | `20` is returned first: last in, first out |
| Queue | Enqueue `10`, enqueue `20`, then front/dequeue | `10` is returned first: first in, first out |
| Binary Search Tree | Insert `2`, `1`, `3`; run inorder or search for `3` | Inorder gives `[1,2,3]`; duplicate insertions are ignored |
| Graph | Add edges `0–1`, `1–2`; run BFS/DFS from `0` | Undirected/unweighted; missing endpoints are created; traversal visits the reachable component |
| Hash Table | Insert integer key `1` with text `hello`; find, update, then delete it | Separate chains handle collisions; UI capacity is eight buckets |

Set difference and symmetric difference are also available. All structures expose
size, empty-state, and contents. Stack display is bottom-to-top; Queue display is
front-to-rear. Tree preorder/postorder and Graph adjacency inspection are available.
Graph vertices and table keys are integers in this UI; table values are text.
The core Python APIs support broader documented payloads/key types.

Empty Stack/Queue inspection or removal and missing members, vertices, or keys
produce readable errors. **Reset all structures** replaces all six models and
clears their previous result. Growth is bounded to 200 items/members/vertices;
existing-key updates that do not grow a model remain allowed. The BST is
unbalanced, and the custom Hash Table does not resize automatically.

## 5. Read the measurements correctly

The saved default study has **1,080 observed rows** and **eight guarded skip rows**.
It covers sizes 10, 100, 1,000, and 5,000; random, sorted, reverse, and duplicate
patterns; and five timing plus five separate allocation trials per eligible case.
Seed 506 fixes input generation. Graph BFS uses an n-vertex path profile.

- Timing is operation elapsed milliseconds; fixture construction and result
  checking are excluded, while copying/output creation inside the operation count.
- Allocation is peak **Python-tracked operation allocation**, including results
  and excluding prebuilt fixtures. It is not total RAM or total structure storage.
- Whiskers/min–max describe the observed repeats, not confidence intervals.
- Guarded Bubble Sort/BST cases above 1,000 are skipped with blank metrics.
- Sorting and selecting one rank are different tasks. Compare their scaling and
  trade-offs without treating them as interchangeable competitors.
- Repeated keys can reduce a stored fixture's unique size. The CSV records that
  size and hash capacity rather than assuming every fixture contains n keys.

The separate **60-observation controlled hash study** compares capacity 1 against
2n for unique integer keys. It has its own CSV and is used in the report; it is
not mixed into the app's default-run charts. Five figure pairs (PNG/SVG) and all
228 summary groups are in `results/`.

The dashboard initially reads the saved study. Running benchmarks in the UI or
with the commands below replaces that evidence. To reproduce the submitted
analysis, keep the saved CSVs and rebuild from them. To collect a new study:

```powershell
& .\.venv\Scripts\python.exe -m performance.benchmark --trials 5 --seed 506
& .\.venv\Scripts\python.exe -m scripts.measure_hash_collisions
```

Regenerate summaries and figures, then update reports/slides after collecting new data;
otherwise documents can describe an earlier run. Environment sidecars record
source hashes, revision, Python/packages, seeds, and configuration. The analysis
manifest checks raw data and figure integrity. See the full
[measurement methodology](documentation/benchmark_methodology.md).

## 6. Reports, slides, and the APA Word edition

| File | Purpose |
|---|---|
| [APA Word report](documentation/performance_analysis_report.docx) | Editable APA 7 student-paper edition with citations, references, and five figures |
| [APA PDF preview](documentation/performance_analysis_report_apa.pdf) | Word-rendered view of the APA edition |
| [Original analysis PDF](documentation/performance_analysis_report.pdf) | The ten-page Day 4 report, including eight substantive body pages |
| [PowerPoint](documentation/portfolio_presentation.pptx) | Twelve slides with authentic screenshots, measured charts, and speaker notes |
| [Slide PDF preview](documentation/portfolio_presentation_preview.pdf) | Native PowerPoint export for readers without Office |
| [Presentation walkthrough](documentation/presentation_walkthrough.md) | Suggested 8–10 minute script covering the assignment deliverables |

The APA edition uses letter paper, one-inch margins, 12-point Times New Roman,
double spacing, paragraph indents, top-right page numbers, and an alphabetized
reference list with hanging indents. Figures are numbered sequentially and placed
on separate pages after references. Its analysis and numbers come from the same
verified source used for the original report.

Edit the DOCX directly in Word or a compatible editor to add the full author
name, institution/department if required, instructor, and actual assignment due
date. Bracketed missing fields are deliberate prompts. Export the edited report
to PDF to refresh its preview. Edit the PPTX directly and export its preview in
the same way. The finished documents need no Python document-generation tools.

Optional benchmark plot regeneration:

```powershell
& .\.venv\Scripts\python.exe -m pip install -r requirements-analysis.txt
& .\.venv\Scripts\python.exe -m scripts.analyze_results
& .\.venv\Scripts\python.exe -m scripts.validate_release --analysis
```

The remaining helper scripts measure the controlled hash profile, regenerate
CSV/JSON summaries and standalone figures, and check evidence integrity. Plotting
uses optional Matplotlib; the app and benchmark runner do not require it. The
repository no longer includes Word/PowerPoint/PDF builders, duplicate templates,
or their package locks. Historical generators are available from commit
`3d8019f` if needed later.

## 7. Run tests and inspect the core APIs

From the project root in PowerShell:

```powershell
& .\.venv\Scripts\python.exe -m pytest tests/ -v
& .\.venv\Scripts\python.exe -m compileall -q algorithms data_structures visualization performance ui scripts app.py
& .\.venv\Scripts\python.exe -m scripts.validate_release
```

The release suite contains 195 tests. Optional browser QA uses Playwright and an
installed Microsoft Edge. Start the app first, then in another terminal run:

```powershell
& .\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
& .\.venv\Scripts\python.exe -m tests.browser_smoke --url http://127.0.0.1:8501 --skip-benchmark
```

`--skip-benchmark` preserves the saved measurements. Browser QA writes authentic
screenshots. Omitting the flag runs new measurements and replaces the saved CSV.

Core algorithms and structures can be used without launching Streamlit:

```python
from algorithms.bubble_sort import bubble_sort
from algorithms.quickselect import quickselect
from data_structures.custom_set import CustomSet
from data_structures.manager import DataStructureManager

values = [3, 1, 2]
result = bubble_sort(values)
assert result.sorted_values == (1, 2, 3)
assert quickselect(values, 2) == 2
assert values == [3, 1, 2]

left = CustomSet([1, 2])
assert left.union(CustomSet([2, 3])).display() == [1, 2, 3]
assert left.display() == [1, 2]

manager = DataStructureManager()
manager.execute("stack", "push", value=10)
assert manager.execute("stack", "pop") == 10
```

## 8. Troubleshooting

| Symptom | What to check |
|---|---|
| `python` is not recognized | Use the installed Python executable (`py -3.14` or `python3`, where available) and verify its version |
| `app.py` or requirements cannot be found | Change into the AlgoNexis root folder before running commands |
| PowerShell blocks activation | Use `.venv\Scripts\python.exe` directly as shown above |
| `ModuleNotFoundError` | Install requirements with the same environment's Python that launches the app |
| Browser cannot connect | Keep the server terminal open and use its printed address/port; a busy port can be changed with `--server.port 8502` |
| Input/action is rejected | Use integers and a valid one-based rank; check trace, dataset, and structure bounds |
| Empty structure or missing key error | Add the item/key first, or choose a valid graph starting vertex |
| Unexpected old UI behavior after source edits | Stop and restart the development server to refresh imported modules |
| pandas binary import fails on this Windows setup | Use the tested lock (pandas 3.0.6); the Day 4 record documents the local 3.1.1 policy block |
| Evidence validator reports stale files | Inspect whether measured source/data changed; rerun the full study and rebuild analysis together when intentional |
| APA preview differs from edited DOCX | Export the updated DOCX to PDF again; the preview is a saved rendering |

## 9. Find your way around

| Location | Contents |
|---|---|
| `app.py`, `ui/` | App entry point, views, strict parsing, and session state |
| `algorithms/`, `visualization/` | Sorting, selection, immutable records, and step retrieval |
| `data_structures/` | Six models and explicit manager dispatch |
| `performance/` | Correctness-checked timing, allocation, CSV, and summaries |
| `tests/` | Algorithm, structure, UI, evidence, and browser checks |
| `scripts/` | Benchmark analysis, controlled hash measurements, and evidence validation |
| `results/` | Raw observations, provenance, summaries, figure assets, and manifest |
| `documentation/` | Reports, slides, architecture, detailed guides, verification, and retrospective |

Read [README.md](README.md) for requirements and progress,
[architecture.md](documentation/architecture.md) for design decisions,
[data_structures.md](documentation/data_structures.md) for API contracts and
attribution, and the [release checklist](documentation/release_checklist.md) for
the eight deliverables. This root guide is the single usage guide. Earlier
Graphify analysis, temporary QA checkouts, and rendered slide PNG previews were
development aids and have been removed from the working repository.

The tagged [v1.0.0 snapshot](https://github.com/Shreyash2942/AlgoNexis/tree/v1.0.0)
preserves the original completed Day 4 release. Later documentation additions live
on `main`. Keep virtual environments, caches, and credentials out of commits;
use `git status` and review intended files before committing your own changes.
