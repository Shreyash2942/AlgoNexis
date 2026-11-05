# AlgoNexis

**An Interactive Algorithms & Data Structures Portfolio**

> **Project stage:** Day 1 implementation in progress. The repository/environment foundation is being established; the target application, data structures, benchmark evidence, report, and presentation belong to later work packages. See the progress tracker for verified completion.
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
| **Planned stack** | Python 3.11+, Streamlit, pytest, Python standard library; add charting dependencies only as needed. |
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

### Planned repository layout

> The tree below is a **target structure**, not a statement that these files currently exist. Create files in the appropriate work package; do not add empty report/slides or fabricate benchmark data.

```text
AlgoNexis/
├── README.md
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
│   ├── user_guide.md
│   ├── performance_analysis_report.pdf
│   ├── portfolio_presentation.pptx
│   └── retrospective.md
└── results/
    └── benchmark_results.csv
```

The final presentation may be a **video instead of slides** if that submission option is selected. Place generated files in `documentation/` only once they are actually created.

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
| Day 1 | ☐ Unverified | Test output + reviewed APIs/step records | _check `git log`_ |
| Day 2 | ☐ Unverified | Data structure/manager tests | _check `git log`_ |
| Day 3 | ☐ Unverified | App walkthrough + benchmark evidence | _check `git log`_ |
| Day 4 | ☐ Unverified | Full QA + final artifacts | _check `git log`_ |

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

> The environment setup is available. Algorithm tests and APIs are delivered during Day 1; `app.py` and interactive launch remain planned for Day 3.

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
compatible Python/platform. The initial environment uses CPython 3.14.4 on Windows.
Prior-course reuse candidates for Day 2 are listed in
[`documentation/data_structures.md`](documentation/data_structures.md).

### Run and test

```bash
# Run automated tests after their modules exist
python -m pytest tests/ -v

# Launch the interactive app after Day 3 integration
streamlit run app.py

# Final syntax check (after implementation)
python -m compileall -q algorithms data_structures visualization performance app.py
```

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
| 8 | Complete documentation | This README, `documentation/architecture.md`, `data_structures.md`, `user_guide.md`, and design decisions |

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

- [ ] Bubble Sort correctly sorts and displays every required step; Quickselect correctly finds valid kth values.
- [ ] Custom Set operations and all five additional data structures function correctly.
- [ ] Every required component is available in the interactive UI; errors and resets work.
- [ ] All applicable automated tests pass; the app launches from a clean environment.
- [ ] Benchmark charts are supported by saved real measurements and correctly labeled.
- [ ] The performance report has **at least five substantive pages** and analyzes meaningful trade-offs.
- [ ] The final presentation demonstrates real system features and course learning.
- [ ] Setup, usage, architecture, and design decisions are documented.
- [ ] The final repository is clean of secrets, caches, and unnecessary files; deliverables open correctly.
- [ ] Commits accurately reflect completed development; tag `v1.0.0` **only after** G4 passes.

---

**Implementation details, per-day checklists, acceptance tests, and the full commit plan:** [`AlgoNexis_4_Day_Implementation_Plan.md`](./AlgoNexis_4_Day_Implementation_Plan.md).
