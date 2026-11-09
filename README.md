# AlgoNexis

**An Interactive Algorithms & Data Structures Portfolio**

New here? Start with [guide.md](guide.md) for installation, examples, troubleshooting,
tests, and benchmark analysis. The editable [APA Word report](documentation/performance_analysis_report.docx)
and its [PDF preview](documentation/performance_analysis_report_apa.pdf) complement
the original Day 4 artifacts. Edit the Word title page directly to add the full
author name, instructor, and actual assignment due date before submission.

> **Project stage:** Day 4 complete; G1–G4 passed. The portfolio has 195 passing tests, 1,080 default observations plus eight guarded skips, and 60 controlled collision observations. The final report has eight substantive body pages; the presentation has twelve slides. See the [release checklist](documentation/release_checklist.md), [verification record](documentation/day4_verification.md), and [user guide](guide.md).
>
> **Execution plan:** [`AlgoNexis_4_Day_Implementation_Plan.md`](./AlgoNexis_4_Day_Implementation_Plan.md) — the detailed task-by-task source of truth for the four development days and quality gates. **Keep this file in the repository root beside `README.md`.**

## 1. At a glance

| Item | Project specification |
|---|---|
| **Name** | AlgoNexis |
| **Purpose** | Demonstrate course mastery of algorithms, sets, and fundamental data structures in one interactive portfolio. |
| **Primary audience** | Course evaluator, student developer, and learners exploring algorithms. |
| **Core algorithms** | Bubble Sort with step tracking and Quickselect for the kth-smallest element. |
| **Data structures** | Custom Set, Stack, Queue, Binary Search Tree, Graph, and Hash Table. |
| **Interface** | Local Streamlit application for hands-on testing and comparisons. |
| **Performance analysis** | Repeatable timing, Python-tracked memory measurements, operation counts, tables, charts, and CSV exports. |
| **Technology** | Python 3.11+, Streamlit, pytest, Python standard library; add charting dependencies only as needed. |
| **Development strategy** | Four-day lightweight Hybrid Agile plan with PSEPF-style quality gates G1–G4. |
| **Commit targets** | Day 1: 5; Day 2: 6; Day 3: 7; Day 4: 4 (**22 planned meaningful commits**). |
| **Final academic artifacts** | Source code, functional app, 5+ page performance analysis report, slides **or** video, and full usage/design documentation. |

## 2. Project goal

AlgoNexis is **one cohesive application**, not a collection of unrelated scripts. A user should be able to:

1. Enter an integer list, run **Bubble Sort**, and inspect each comparison and swap in sequence.
2. Enter an integer list and a **1-based rank `k`** to find the kth-smallest value using **Quickselect**.
3. Create and manipulate a **Custom Set**, including union, intersection, difference, and symmetric difference.
4. Experiment with a **Stack, Queue, Binary Search Tree, Graph, and Hash Table** through interactive controls.
5. View **measured** runtime and memory behavior and understand where algorithmic trade-offs matter.
6. Reproduce the results using documented setup steps, tests, and exported benchmark data.

The portfolio should demonstrate **correctness, algorithmic understanding, integration, usability, and evidence-based performance analysis**.

## 3. Requirements and acceptance criteria

| ID | Feature | Acceptance evidence |
|---|---|---|
| F-01 | Bubble Sort | Correctly sorts integers including empty/negative/duplicate inputs; recorded steps match real comparisons and swaps. |
| F-02 | Quickselect | Returns `sorted(values)[k - 1]` for valid `1 <= k <= len(values)` without sorting the whole list as its implementation; rejects invalid input. |
| F-03 | Custom Set | Enforces uniqueness and correctly implements **union, intersection, difference, symmetric difference**; documents mutations versus derived operations. |
| F-04 | Stack | Correct `push`, `pop`, `peek`, and empty-state behavior (**LIFO**). |
| F-05 | Queue | Correct `enqueue`, `dequeue`, `front`, and empty-state behavior (**FIFO**). |
| F-06 | Binary Search Tree | Correct insertion, search, inorder, preorder, and postorder traversal. |
| F-07 | Graph | Add vertices/edges and perform correct BFS and DFS traversals. |
| F-08 | Hash Table | Insert/update, find, and delete keys; collisions are handled correctly. |
| F-09 | Unified manager | Data structure operations are accessible through consistent, tested dispatch logic. |
| F-10 | Interactive interface | All required components are accessible; inputs are validated; state persists and resets correctly. |
| F-11 | Performance tools | Actual reproducible measurements, labeled charts/tables, and usable CSV evidence. |
| F-12 | Academic submission | A **5+ substantive-page report**, final presentation, complete source, and complete user/design documentation. |

**Done means verified:** An implemented feature is not considered complete until its relevant automated tests pass, its integration behavior has been checked, and the changes are genuinely committed.

## 4. Architecture

```text
                           +--------------------------+
                           | Streamlit UI (app.py)    |
                           | inputs, views, state     |
                           +-------------+------------+
                                         |
                    +--------------------+--------------------+
                    |                                         |
         +----------v-----------+                 +-----------v------------+
         | Algorithm modules    |                 | DataStructureManager   |
         | Bubble Sort          |                 | registry + dispatch    |
         | Quickselect          |                 +-----------+------------+
         +----------+-----------+                             |
                    |                            +------------v-------------+
         +----------v-----------+                | CustomSet / Stack / Queue |
         | Sorting-step         |                | BST / Graph / HashTable  |
         | visualization data   |                +------------+-------------+
         +----------+-----------+                             |
                    +-------------------+---------------------+
                                        |
                             +----------v-----------+
                             | Performance layer    |
                             | timing, memory, CSV  |
                             +----------+-----------+
                                        |
                                  tables / charts
```

**Design rules:** Keep core algorithms and data structures independent of Streamlit. The UI calls these modules; it must not contain their underlying algorithm implementations. Measure algorithm operations **outside** rendering logic. Use plain results and explicit errors to support tests and UI integration.

### Implemented repository layout (principal files)

> Principal source and submission artifacts are shown below. `scripts/` contains benchmark analysis and evidence checks; `ui/` contains the application views.

```text
AlgoNexis/
├── README.md
├── guide.md
├── AlgoNexis_4_Day_Implementation_Plan.md
├── .gitignore
├── requirements.txt
├── app.py
├── algorithms/
│   ├── __init__.py
│   ├── bubble_sort.py
│   └── quickselect.py
├── data_structures/
│   ├── __init__.py
│   ├── custom_set.py
│   ├── stack.py
│   ├── queue.py
│   ├── tree.py
│   ├── graph.py
│   ├── hash_table.py
│   └── manager.py
├── visualization/
│   ├── __init__.py
│   └── sorting_visualizer.py
├── performance/
│   ├── __init__.py
│   ├── benchmark.py
│   └── metrics.py
├── tests/
│   ├── test_bubble_sort.py
│   ├── test_quickselect.py
│   ├── test_custom_set.py
│   ├── test_stack.py
│   ├── test_queue.py
│   ├── test_tree.py
│   ├── test_graph.py
│   ├── test_hash_table.py
│   ├── test_manager.py
│   └── test_app_integration.py
├── documentation/
│   ├── architecture.md
│   ├── data_structures.md
│   ├── performance_analysis_report.pdf
│   ├── portfolio_presentation.pptx
│   └── retrospective.md
└── results/
    └── benchmark_results.csv
```

The release includes [the PDF report](documentation/performance_analysis_report.pdf), [editable PowerPoint slides](documentation/portfolio_presentation.pptx), and a [PowerPoint-rendered PDF preview](documentation/portfolio_presentation_preview.pdf). The [presentation walkthrough](documentation/presentation_walkthrough.md) accompanies the slides.

## 5. Key implementation contracts

These defaults follow the four-day implementation plan. Record any final choices in `documentation/architecture.md` and keep tests, UI, and documentation consistent.

| Module | Contract and important edge cases |
|---|---|
| **Bubble Sort** | Accept a list of integers; use adjacent comparisons and an early-exit optimization. Return sorted output plus accurate ordered step records and comparison/swap counts. Prefer not to mutate the caller's list. Provide initial and final states for the visualizer. |
| **Quickselect** | Accept integers and **1-based `k`**; use partitioning and preferably a randomized pivot. The kth rank **counts duplicates**. Validate empty input and out-of-range `k`; preferably do not mutate caller input. Expected `O(n)`, worst `O(n²)`. |
| **Custom Set** | Use a custom class (`CustomSet`). Avoid delegating required set algebra directly to Python `set` operators as the implementation. Enforce uniqueness; derived operations should return new sets without modifying operands. Support add/remove and membership. |
| **Stack / Queue** | Stateful classes; raise a consistent, documented error on empty removals/inspections. Prefer `collections.deque` for efficient queue operations. |
| **BST** | Use an ordinary unbalanced binary search tree; choose a deterministic duplicate policy (recommended: ignore duplicates) and document skewed-tree behavior. |
| **Graph** | Start with an **undirected, unweighted adjacency list**, deterministic neighbor order, BFS/DFS, and clear handling of disconnected vertices/invalid starts. |
| **Hash Table** | Custom bucket storage with **separate chaining**; define supported key types and consistent missing-key behavior. Verify collisions deliberately. |
| **Manager** | Central operation registry; suggested API: `execute(structure, operation, **kwargs)`. Allow only known operations; **never use `eval()`**. Preserve the state of each structure instance. |
| **Streamlit UI** | Keep interactive state in `st.session_state`; invalidate stale algorithm results when inputs change; offer reset controls and readable errors. |
| **Benchmarks** | Use `time.perf_counter()` for time and `tracemalloc` for **Python-tracked allocations** (not total RAM). Use reproducible datasets and multiple trials. Check correctness before reporting timings. |

### Important conceptual distinctions

- **Bubble Sort sorts** an entire list; **Quickselect selects** one ranked value. Benchmark timing differences do **not** mean they perform the same task.
- **Static/derived set operations** produce or inspect results; **dynamic operations** change membership through insertion/removal. Match the course's preferred terminology if its definition is more specific.
- An **unbalanced BST** may degrade to linear-time searches, and hash-table performance depends on collisions and load factor.
- For set comparisons and BFS/DFS traversal, define equality/order expectations clearly so tests are meaningful.

## 6. Four-day execution roadmap

Complete tasks in the linked implementation plan **in order**. The daily milestones are dependencies, not merely presentation headings.

| Day | Goal | Primary files/work | Gate | Planned commits |
|---|---|---|---|---:|
| **Day 1** | Foundation and core algorithms | Project setup; Bubble Sort + steps; Quickselect; algorithm tests; initial docs | **G1:** Algorithm and step-record tests pass | **5** |
| **Day 2** | Sets and data structures | Custom Set; Stack, Queue, BST, Graph, Hash Table; manager; tests/docs | **G2:** All structure operations and manager dispatch pass | **6** |
| **Day 3** | Interactive application and measurements | Streamlit navigation; algorithm/UI panels; visualizer; data structure controls; benchmarks and charts | **G3:** All components work in UI; actual benchmark outputs generated | **7** |
| **Day 4** | Submission-ready release | Regression QA; final benchmark runs; **5+ page report**; presentation; guides; packaging | **G4:** All eight assignment deliverables verified | **4** |

### Daily progress tracker

> **Agent maintenance:** After inspecting the *actual* repository, replace unverified entries with accurate statuses. Do not mark a gate passed because its day appears in the calendar.

| Day | Status (verify in repository) | Gate evidence | Commits actually created |
|---|---|---|---|
| Day 1 | G1 passed | 71 original tests retained in the full regression; [verification](documentation/day1_verification.md) | Five Day 1 commits; `git log --oneline f2409c4` |
| Day 2 | G2 passed | 143 original tests retained; all 49 manager routes; [verification](documentation/day2_verification.md) | Six Day 2 commits; `git log --oneline f2409c4..7fa29e5` |
| Day 3 | G3 passed | 191 tests, real Edge walkthrough/screenshots, 1,080 observations + 8 skips; [verification](documentation/day3_verification.md) | Seven Day 3 commits; `git log --oneline 7fa29e5..c44dd50` |
| Day 4 | G4 passed | 195 tests, clean-install and browser checks, verified report/slides/evidence; [verification](documentation/day4_verification.md) | Four release commits; `git log --oneline c44dd50..v1.0.0`; later documentation additions follow on `main` |

### Planned Conventional Commit sequence

**Commit messages are targets, not a script to run all at once.** Commit only real, tested changes; if the work legitimately needs a different split, update the plan and maintain an accurate history.

| # | Day | Commit message |
|---:|---:|---|
| 01 | 1 | `chore: initialize AlgoNexis project structure` |
| 02 | 1 | `feat: implement bubble sort with step tracking` |
| 03 | 1 | `feat: add sorting visualization engine` |
| 04 | 1 | `feat: implement quickselect with input validation` |
| 05 | 1 | `test: add core algorithm tests and documentation` |
| 06 | 2 | `feat: implement custom set operations` |
| 07 | 2 | `feat: add stack and queue implementations` |
| 08 | 2 | `feat: implement binary search tree and graph` |
| 09 | 2 | `feat: add hash table with collision handling` |
| 10 | 2 | `feat: integrate data structures through unified manager` |
| 11 | 2 | `test: verify data structures and document operations` |
| 12 | 3 | `feat: build Streamlit dashboard and navigation` |
| 13 | 3 | `feat: integrate bubble sort and quickselect interfaces` |
| 14 | 3 | `feat: add interactive bubble sort visualization` |
| 15 | 3 | `feat: build interactive data structure controls` |
| 16 | 3 | `perf: implement execution time and memory benchmarking` |
| 17 | 3 | `feat: add performance charts and benchmark dashboard` |
| 18 | 3 | `test: validate UI integration and performance tools` |
| 19 | 4 | `test: complete final regression and integration testing` |
| 20 | 4 | `perf: finalize benchmarks and performance analysis` |
| 21 | 4 | `docs: add comprehensive performance analysis report` |
| 22 | 4 | `docs: finalize presentation and release documentation` |

## 7. Local development and verification

> The local application and all eight submission deliverables are implemented and verified. Launch and rebuild commands are below.

### Environment setup

```bash
# From the repository root
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows PowerShell (instead of the line above)
# .venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
```

When PowerShell script execution prevents activation, use the environment's Python
directly; activation is not required:

```powershell
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe -m pytest tests/ -v
```

`requirements.lock.txt` records the tested development environment. Install it
instead of `requirements.txt` to reproduce those exact dependency versions on a
compatible Python/platform. The final verified environment uses CPython 3.14.4 on Windows and pandas 3.0.6. The Day 4 record explains the tested pandas maintenance-series choice.
Reviewed prior-course adaptations and structure APIs are listed in
[`documentation/data_structures.md`](documentation/data_structures.md).

### Run and test

```bash
# Run automated tests
python -m pytest tests/ -v

# Launch the local interactive app
python -m streamlit run app.py

# Syntax check
python -m compileall -q algorithms data_structures visualization performance ui tests app.py
```

The four sections are Dashboard, Algorithms, Data Structures, and Performance
Analysis. Dataset/rank changes clear stale algorithm results; structure state and
sorting position persist across navigation. Visualized sorts are limited to 50
values, untraced sorts to 1,000, selections to 5,000, and interactive structures to
200 items. See the [user guide](guide.md) for controls and errors.

Reproduce the measured evidence:

```powershell
& .\.venv\Scripts\python.exe -m performance.benchmark --trials 5 --seed 506
```

Results are saved to [`results/benchmark_results.csv`](results/benchmark_results.csv)
and its [environment/source record](results/benchmark_results.environment.json).
The dashboard uses these same observations for separate time/allocation charts and
CSV download. Read the [measurement method](documentation/benchmark_methodology.md)
before drawing conclusions: timing and allocation trials are separate, prebuilt
fixtures are excluded, allocations are not total RAM, and different-purpose
operations are not substitutes. No skipped case is plotted as zero.


### Benchmark analysis and finished documents

The reports and slides are finished submission files. Edit the DOCX and PPTX
in Word/PowerPoint (or compatible editors) and export their PDF previews after
changes. Document-generation scripts, templates, and their dependencies were
removed during repository cleanup. They remain available in the Git history.

Benchmark reproduction and evidence checks remain supported:

```bash
# Optional; needed only to regenerate the standalone plots:
python -m pip install -r requirements-analysis.txt
python -m scripts.analyze_results
python -m scripts.validate_release --analysis
```

To collect a new study, run `python -m performance.benchmark --trials 5 --seed 506`
and `python -m scripts.measure_hash_collisions`, then regenerate the analysis.
Update report/slide text and figures manually if you replace their source data.
The [methodology](documentation/benchmark_methodology.md) documents measurement
boundaries. `results/summary_statistics.csv` includes mean, median, min, max, and
trial counts; five figures are available as PNG and SVG.

Known scope limits include an unbalanced BST, fixed-capacity custom hashing,
undirected/unweighted graph traversal, bounded UI inputs, and single-machine
microbenchmarks. Tracked operation allocation excludes prebuilt fixtures and is
not total RAM. The [retrospective](documentation/retrospective.md) records future
work. Historical Day 1–3 verification records retain their original measurements.

### Implemented Day 1 APIs

```python
from random import Random
from algorithms.bubble_sort import bubble_sort
from algorithms.quickselect import quickselect
from visualization.sorting_visualizer import SortingVisualizer

values = [3, 1, 2]
result = bubble_sort(values)
assert result.sorted_values == (1, 2, 3)
assert values == [3, 1, 2]  # Caller input is preserved.
assert (result.comparisons, result.swaps) == (3, 2)

view = SortingVisualizer(result)
for frame in view:
    print(frame.step_index, frame.event, frame.values, frame.description)
assert view.get_step(view.total_steps - 1).values == result.sorted_values

assert quickselect([7, -1, 7, 3], 3, rng=Random(42)) == 7
```

Both algorithms accept Python integer lists, excluding booleans, and copy input.
Bubble Sort returns a frozen result with tuple output, tuple snapshots, and
cumulative comparison/swap counts. Its trace contains `initial`, every `compare`
(before any exchange), every actual `swap` (after exchange), and `final` events.
`track_steps=False` disables trace allocation explicitly while preserving results
and counts. The visualizer uses zero-based indices, immutable frames, and no UI
dependency; an untraced result is rejected rather than silently losing steps.

Quickselect returns an integer at the one-based rank, counting duplicate values.
It partitions with randomized pivots instead of sorting; pass a fresh
`Random(seed)` to repeat pivot choices. Empty input or invalid rank bounds raise
`ValueError`; invalid list/element/rank types raise `TypeError`.

Without tracing, Bubble Sort uses O(n) best and O(n²) average/worst time, with
O(n) space for its copy. Full snapshots can raise time and storage to O(n³).
Quickselect has expected O(n), worst O(n²) time and O(n) copy space; its iterative
partition workspace is O(1). See [architecture decisions](documentation/architecture.md)
for complete record fields, validation, mutability, and benchmark policies.

### Implemented Day 2 manager

```python
from data_structures.manager import DataStructureManager

manager = DataStructureManager(hash_capacity=1)
manager.execute("set", "add", value=1)
assert manager.execute("set", "union", values=[2, 3]) == [1, 2, 3]
assert manager.execute("set", "display") == [1]  # Derived result preserves state.
manager.execute("queue", "enqueue", value=10)
assert manager.execute("queue", "dequeue") == 10
manager.execute("tree", "insert", value=4)
assert manager.execute("tree", "inorder") == [4]
manager.execute("graph", "add_edge", source="a", target="b")
assert manager.execute("graph", "bfs", start="a") == ["a", "b"]
manager.execute("hash_table", "insert", key="a", value=None)
assert manager.execute("hash_table", "find", key="a") is None
```

Canonical manager names are `set`, `stack`, `queue`, `tree`, `graph`, and
`hash_table`. The registry exposes only known operations and retains separate
instances; `available_operations()` returns UI-ready operation names. Empty
stack/queue operations raise `IndexError`; absent set members, graph starts,
and table keys raise `KeyError` where documented. See the
[operations guide](documentation/data_structures.md) for all arguments, return
values, display order, theoretical costs, and prior-course attribution.

### Git workflow for each **completed** work package

```bash
git status
git diff
# Stage only files related to the completed work; example:
git add algorithms/bubble_sort.py
# Run relevant tests before committing, then create the matching commit:
git commit -m "feat: implement bubble sort with step tracking"
git log --oneline -5
```

Never use placeholder or empty commits, fabricate timestamps, or commit unverified results. The planned `v1.0.0` tag is created **only after G4 passes**.

## 8. Testing and benchmarking policy

### Automated test priorities

- **Algorithms:** Empty/single/duplicate/negative/sorted/reverse-sorted input; sorting-step consistency; valid and invalid `k`; compare with Python `sorted()` as a *test oracle*.
- **Sets:** Empty, identical, disjoint, overlapping, and duplicate-heavy input; no unexpected operand mutation.
- **Structures:** LIFO/FIFO behavior, empty-state exceptions, BST traversal and duplicate policy, graph cycles/disconnection/invalid source, and intentional hash collisions.
- **Integration:** All manager dispatch routes, instance persistence, unsupported operations, and Streamlit input/session-state/reset workflows.
- **Regression:** Re-run preceding days' tests at each gate and the full suite before submission.

### Measurement protocol

1. Record Python version, OS/environment, timestamp, dataset seed, data pattern, and trial count.
2. Test increasing input sizes (suggested **10, 100, 1,000, 5,000**, with safe limits for slow cases) using random, sorted, reverse-sorted, and duplicate-rich lists where relevant.
3. Use multiple repetitions (at least **five** where feasible) and report summary statistics transparently.
4. Isolate algorithm execution from input generation and Streamlit/chart rendering; measure allocations separately when practical.
5. Verify every operation's result before retaining its measurement. Preserve **real** raw observations in `results/benchmark_results.csv`.
6. Label the memory metric as **peak Python-tracked allocations**, not full-process memory.
7. Compare different-purpose operations as **scaling/trade-off examples**, not head-to-head substitutes.

**Suggested CSV columns:**

```text
timestamp,algorithm_or_structure,operation,input_size,input_pattern,seed,trial,elapsed_ms,peak_tracemalloc_bytes,comparisons,swaps,python_version,notes
```

Do not invent benchmark figures, charts, test counts, citations, screenshots, or report conclusions.

## 9. Submission deliverables

| # | Required artifact | Expected location and verification |
|---:|---|---|
| 1 | Bubble Sort source + visualization | `algorithms/bubble_sort.py`, `visualization/sorting_visualizer.py`, working UI stepper |
| 2 | Quickselect source | `algorithms/quickselect.py`, selection tests |
| 3 | Complete documented Custom Set | `data_structures/custom_set.py`, tests and operations guide |
| 4 | Integrated portfolio | Python modules + `data_structures/manager.py`, end-to-end test |
| 5 | Interactive interface | `app.py`, manual UI walkthrough |
| 6 | Comprehensive **5+ page** analysis report | `documentation/performance_analysis_report.pdf`, verified against actual CSV data |
| 7 | Final presentation (**slides or video**) | `documentation/portfolio_presentation.pptx` or a clearly identified video artifact |
| 8 | Complete documentation | This README, `documentation/architecture.md`, `data_structures.md`, `guide.md`, and design decisions |

The recommended report structure is: introduction; algorithm/data structure overview; measurement methodology; measured results; trade-offs and limitations; conclusion; references. Use formal analytical writing and **APA 7 if the course requires it**. If sources are quoted directly, include the appropriate location information; otherwise paraphrase with attribution. The presentation should show **authentic application screenshots and actual benchmark charts**, plus learning outcomes.

## 10. Basic security, reliability, and academic integrity

- Validate all numeric input and bounds (`k`, UI dataset sizes, benchmark trial limits).
- Parse integers safely; never `eval()` user-provided strings or dynamically execute operation names.
- Handle empty structures, invalid graph starting vertices, missing hash keys, and bad user actions gracefully.
- Ignore `.venv/`, caches, local environment files, credentials, and temporary artifacts in Git.
- Minimize dependencies; support a clean installation and document any setup assumptions.
- Do not claim performance results, passing tests, or completed deliverables without evidence.
- Reuse earlier course implementations where appropriate **after verifying correctness and attribution**.

## 11. AI coding agent instructions (read before changing code)

This section is intentionally explicit so a coding agent can execute the plan without guessing what to build.

### Read order and authority

1. **Assignment requirements and success criteria** (summarized in Sections 2–3 here): authoritative for **what must be delivered**.
2. **[`AlgoNexis_4_Day_Implementation_Plan.md`](./AlgoNexis_4_Day_Implementation_Plan.md)**: authoritative for **task ordering, work packages, daily gates, and planned commits**.
3. **This `README.md`**: concise product, architectural, testing, documentation, and agent-execution guidance.
4. **Existing repository code/tests/docs**: actual implementation state. Inspect before modifying; do not overwrite completed work blindly.

If there is a contradiction with a course rubric or user instruction, follow the more explicit academic/user requirement and **record the deviation**. The PSEPF **L2** label in the plan is *provisional* because official L1–L5 definitions were not supplied.

### Initial repository inspection

Before writing code, the agent must:

1. Read both Markdown files in full, especially the *current day's* detailed work packages and quality gate.
2. Inspect the actual working tree and Git history (`git status`, `git log --oneline`) to locate the **first incomplete, unverified work package**.
3. Check whether prior-course code exists, and preserve/reuse it appropriately if it meets the requirement.
4. Identify current language/dependency constraints and existing API conventions. Do not claim files, tests, or commits exist without checking.
5. Begin with the next valid task; **for an empty repository, start with Day 1 / D1.1**.

### Task execution loop

For **each** work package:

1. Read that work package's tasks and acceptance criteria in the detailed plan.
2. Implement only the required scope (plus necessary support); maintain separation of core logic, UI, and benchmarking.
3. Add/update automated tests for correctness and failure cases; run relevant checks.
4. Document public APIs, assumptions, and decisions when introducing or changing behavior.
5. Review the diff and stage related files only; create the corresponding **real, tested** commit.
6. Update the progress tracker in this README to reflect **verified** work; if changing the tracker would create an unrelated diff, include it with the next relevant documentation commit.
7. At each daily gate, run all available prior tests and verify the gate's concrete evidence **before starting the following day**.

If implementation details are unspecified, use the recommended defaults in Section 5, keep the choice simple and testable, and record it in `documentation/architecture.md`. Avoid unrequested enhancements until all required features are complete.

### Completion report back to the user

At the end of a requested work session/day, report:

- What was implemented, with affected files.
- Which tests/checks were executed and their **actual results**.
- Which Git commits were **actually created** (hash and message when available).
- Gate status (**passed / blocked / unverified**) with evidence.
- Known issues and the **next specific work package**.

**Do not** invent commit hashes, report successful commands that were not run, or produce the Day 4 report from placeholder data.

### Copy/paste starter instruction for an AI coding agent

```text
You are the coding agent for AlgoNexis. Read README.md and
AlgoNexis_4_Day_Implementation_Plan.md completely before editing.
Inspect the repository and Git history to determine real progress.
Follow the four-day work packages in order, beginning with the first
incomplete package (D1.1 if this is a fresh repository). Implement,
test, document, and make only honest, task-relevant commits after each
package is verified. Keep the planned distribution of 5/6/7/4 commits
when the actual work supports it; do not make empty/artificial commits.
Do not proceed beyond a daily PSEPF gate if critical checks fail.
Never fabricate test outcomes, benchmark values, citations, screenshots,
or deliverables. At the end, summarize completed files, exact test
results, actual commit hashes/messages, gate status, and next task.
```

## 12. Final release gate (G4)

The project is ready for submission only after all of the following are **actually verified**:

- [x] Bubble Sort correctly sorts and displays every required step; Quickselect correctly finds valid kth values.
- [x] Custom Set operations and all five additional data structures function correctly.
- [x] Every required component is available in the interactive UI; errors and resets work.
- [x] All applicable automated tests pass; the app launches from a clean environment.
- [x] Benchmark charts are supported by saved real measurements and correctly labeled.
- [x] The performance report has **at least five substantive pages** and analyzes meaningful trade-offs.
- [x] The final presentation demonstrates real system features and course learning.
- [x] Setup, usage, architecture, and design decisions are documented.
- [x] The final repository is clean of secrets, caches, and unnecessary files; deliverables open correctly.
- [x] Commits accurately reflect completed development; tag `v1.0.0` **only after** G4 passes.

---

**Implementation details, per-day checklists, acceptance tests, and the full commit plan:** [`AlgoNexis_4_Day_Implementation_Plan.md`](./AlgoNexis_4_Day_Implementation_Plan.md).
