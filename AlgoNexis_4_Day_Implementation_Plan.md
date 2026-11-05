# AlgoNexis — Complete Four-Day Implementation Plan

**Project:** AlgoNexis — Interactive Algorithms & Data Structures Portfolio  
**Plan version:** 1.0  
**Duration:** Four development days (approximately 26–31 hours total)  
**Approach:** Lightweight Hybrid Agile with daily PSEPF quality gates  
**Technology baseline:** Python, Streamlit, pytest, standard-library benchmarking utilities  
**Planned Git history:** **22 meaningful commits** — Day 1: **5**, Day 2: **6**, Day 3: **7**, Day 4: **4**  
**Progress:** ☐ Not started · ☐ In progress · ☐ Complete

> **How to use this plan:** Complete each day's work packages in order, run the listed verification steps, and create the corresponding Git commit **only after the work exists and passes the relevant checks**. Dates are intentionally not assigned because no start date was supplied. Planned commit counts are targets, not a reason to make empty or artificial commits.

---

## Contents

1. [Project assessment and scope](#1-project-assessment-and-scope)
2. [PSEPF assessment and development approach](#2-psepf-assessment-and-development-approach)
3. [Architecture and implementation decisions](#3-architecture-and-implementation-decisions)
4. [Four-day roadmap and milestones](#4-four-day-roadmap-and-milestones)
5. [Day 1 — Foundation and core algorithms](#5-day-1--foundation-and-core-algorithms)
6. [Day 2 — Custom sets and data structures](#6-day-2--custom-sets-and-data-structures)
7. [Day 3 — Interactive application and benchmarking](#7-day-3--interactive-application-and-benchmarking)
8. [Day 4 — Final QA, report, presentation, release](#8-day-4--final-qa-report-presentation-release)
9. [Complete Git commit schedule](#9-complete-git-commit-schedule)
10. [Testing, benchmarking, and security strategy](#10-testing-benchmarking-and-security-strategy)
11. [Deliverable-to-requirement traceability](#11-deliverable-to-requirement-traceability)
12. [Documentation and presentation artifacts](#12-documentation-and-presentation-artifacts)
13. [Risks, dependencies, and contingency plan](#13-risks-dependencies-and-contingency-plan)
14. [Final release checklist and retrospective](#14-final-release-checklist-and-retrospective)

---

## 1. Project assessment and scope

### 1.1 Problem statement

Build a **single interactive portfolio** that demonstrates understanding of sorting, selection, sets, stacks, queues, trees, graphs, and hash tables. The system must let users execute operations, understand their behavior, and examine performance trade-offs rather than merely present disconnected source files.

### 1.2 Users, constraints, and assumptions

| Item | Planning decision |
|---|---|
| Primary users | Course evaluator, student developer, and anyone exploring basic algorithms |
| Team size | Assumed one developer; revise if collaborating |
| Schedule | Four development days; estimates are planning aids rather than deadlines |
| Language | Python 3.11+ recommended |
| Application | Streamlit web interface running locally |
| Tests | `pytest` plus standard-library reference results where appropriate |
| Charts | Streamlit charts or an existing supported plotting dependency |
| Reuse policy | Reuse prior-module implementations after reviewing correctness, interfaces, and attribution |
| Submission | Source code, interactive application, **5+ page** analysis report, slides **or** video, and documentation |
| Unknowns | Course-specific rubric, exact PSEPF level definitions, start date, and prior code availability were not provided |

### 1.3 Required functional scope

| ID | Capability | Required behavior |
|---|---|---|
| F-01 | Bubble Sort | Sort integers; capture comparisons, swaps, and ordered visualization states |
| F-02 | Quickselect | Return the **1-based** kth smallest value; validate inputs and duplicates |
| F-03 | Custom Set | Unique values, add/remove, union, intersection, difference, symmetric difference |
| F-04 | Stack | Push, pop, peek, inspect current contents |
| F-05 | Queue | Enqueue, dequeue, front, inspect current contents |
| F-06 | Tree | BST insertion/search and inorder, preorder, postorder traversals |
| F-07 | Graph | Add vertices/edges; BFS and DFS |
| F-08 | Hash Table | Insert, lookup, delete; handle collisions |
| F-09 | Unified integration | Consistent access through a manager and one application |
| F-10 | Interactive UI | Accept inputs, show outputs/errors, preserve state, navigate features |
| F-11 | Performance analysis | Time, memory, operation counts where applicable; export real results |

### 1.4 Nonfunctional requirements

- **Correctness:** All required normal and edge cases pass automated tests.
- **Usability:** Users can find every implementation from the interface and understand accepted input formats.
- **Maintainability:** Algorithms, structures, interface, benchmarks, and tests are separated into modules.
- **Reproducibility:** Benchmarks record dataset seed, size, input pattern, trial count, environment, and measurement method.
- **Safety:** Validate numeric input, invalid `k`, unsupported operations, and dataset limits; do not use `eval()`.
- **Academic integrity:** Report only observed measurements, distinguish illustrative examples, and cite outside references correctly.

### 1.5 Definition of done

A feature is done when it is implemented, independently tested, usable through its intended interface (when applicable), documented sufficiently for a reader, and committed with a truthful message. The project is done when all eight assignment deliverables pass the Day 4 release checklist.

---

## 2. PSEPF assessment and development approach

### 2.1 Provisional project level

**Provisional PSEPF level: L2 (lightweight, multi-module academic application).** This is a **working classification**, not a claim about an official level definition. The supplied PSEPF prompt asks for L1–L5 but does **not** define the levels; confirm the course's actual mapping if one is available.

**Rationale:** One assumed developer; four-day schedule; several connected features; limited security and deployment complexity; required testing, report, and presentation. This warrants structured daily gates and traceable commits, but not enterprise-scale governance artifacts.

### 2.2 Process comparison

| Process | Fit | Assessment |
|---|---|---|
| Waterfall | Moderate | Stable assignment requirements, but UI integration issues may require rapid changes |
| Agile/Scrum | Moderate | Short iterations help, but Scrum ceremonies are excessive for four days / one developer |
| Prototype-driven | Good for UI | Quickly tests visual interaction; less suitable by itself for assuring algorithm correctness |
| **Hybrid Agile** | **Best** | Fixed deliverables and daily quality gates, with iterative coding/testing and an early UI spike |

**Selected process:** Lightweight **Hybrid Agile** with one mini-iteration per day. Start each day by checking dependencies, implement vertical slices, run tests, and pass a gate before proceeding.

### 2.3 PSEPF modifiers (appropriately scaled)

| Modifier | Apply? | Lightweight action |
|---|---|---|
| Prototype | Yes | Day 3 initial Streamlit navigation prototype before connecting every module |
| Architecture Gate | Yes | Day 1 choose APIs, folders, error rules, and data structure interfaces |
| Technical Spike | Yes | Verify Streamlit session state and timing/memory collection on a small sample |
| Change Control | Light | Record meaningful scope or interface changes in a brief decision log |
| Security Engineering | Basic safeguards only | Validate inputs, bound workload, exclude secrets; no full security program needed |
| Operations Readiness | Yes, minimal | Clean-environment startup test, dependency instructions, and release package verification |

### 2.4 Required planning artifacts

Keep these deliberately small: this Markdown plan, a README, module/API documentation, an architecture diagram or text diagram, automated tests, benchmark CSV/charts, the report, presentation, and a short retrospective. A separate large backlog, change-approval board, or production operations manual is **not** necessary.

---

## 3. Architecture and implementation decisions

### 3.1 Proposed architecture

```text
                    +-------------------------------+
                    |         app.py / UI           |
                    |  navigation, input, visuals   |
                    +---------------+---------------+
                                    |
                    +---------------+------------------+
                    |                                  |
              Algorithms                        DataStructureManager
          bubble_sort, quickselect                       |
                    |                    +---------------+---------------+
             step records                   CustomSet, Stack, Queue,
                    |                        BST, Graph, HashTable
            Sorting visualizer                       |
                    +---------------+------------------+
                                    |
                        Benchmark / metrics layer
                                    |
                          CSV, tables, charts
```

The performance layer calls implementation APIs directly; the UI displays results. **Benchmark measurement must not include chart rendering** unless explicitly evaluating UI responsiveness.

### 3.2 Planned project tree

```text
AlgoNexis/
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
├── results/
│   └── benchmark_results.csv
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Note:** Generate the PDF and slides on Day 4. They are **future deliverables**, not files that should exist on Day 1. UI helper modules may be added if `app.py` becomes difficult to maintain.

### 3.3 Interfaces and behavior to settle before coding

1. **Bubble Sort:** input list of integers; return sorted values and optional ordered steps containing array snapshot, compared indices, whether a swap occurred, comparison count, and swap count. Do not silently drop steps.
2. **Quickselect:** input list plus `k` with **1 ≤ k ≤ n**; return kth smallest **including duplicate ranks**; clearly document whether the implementation copies the input (recommended: do not mutate caller data). Use randomized pivot selection if practical.
3. **Custom Set:** enforce uniqueness; support hashable elements internally, with integer-oriented UI examples. Implement operation logic in the custom class rather than delegating directly to Python's set-algebra operators. Define whether operations return a new set (recommended) or mutate the existing set.
4. **Static vs dynamic set behavior:** in documentation, distinguish read-only set queries/derived-set operations from add/remove mutations; align the exact terminology with the course if definitions differ.
5. **Stack/Queue:** stateful instances; empty pop/dequeue/peek/front follow one consistent exception policy (e.g., `IndexError`).
6. **BST:** deterministic duplicate policy (e.g., ignore duplicates); note worst-case degradation when unbalanced.
7. **Graph:** initially undirected, unweighted, adjacency-list representation; deterministic neighbor order for testable BFS/DFS output.
8. **Hash Table:** separate chaining with a documented collision policy and missing-key behavior.
9. **Manager:** `execute(structure, operation, **kwargs)` dispatches known operations, returns results, and rejects unsupported requests gracefully.
10. **UI state:** store structure instances and visualization index in `st.session_state`, and reset appropriately when dataset changes.

---

## 4. Four-day roadmap and milestones

### 4.1 Week-by-week view

The project fits in **one four-day development week**. The week's goal is to progress from independently correct algorithms to a testable unified application, measurable performance evidence, and a complete submission package.

| Day | Primary daily objective | Hours (estimate) | Major milestone | Planned commits |
|---|---|---:|---|---:|
| **1** | Establish architecture and build the two core algorithms | 5–7 | **M1:** Algorithms and visualization records verified | **5** |
| **2** | Build six data structures and integrate through manager | 6–8 | **M2:** Data structure operations integrated and tested | **6** |
| **3** | Deliver interactive app and reproducible benchmark tools | 6–8 | **M3:** End-to-end interactive portfolio operational | **7** |
| **4** | Verify, analyze, present, document, and package | 7–9 | **M4:** Submission-ready release | **4** |
| **Total** | | **24–33** | | **22** |

*Estimates are ranges; the schedule assumes the previous-module code can be reviewed or adapted rather than entirely rewritten.*

### 4.2 Transition quality gates

- **Gate G1, after Day 1:** Bubble Sort and Quickselect tests pass; step records match real sorting actions; interfaces fixed for integration.
- **Gate G2, after Day 2:** All required set operations and five additional structures pass tests; manager dispatches consistently.
- **Gate G3, after Day 3:** Every component works through the UI; benchmarks produce real, labeled measurements and CSV export.
- **Gate G4, after Day 4:** Regression tests pass; report is at least five substantive pages; presentation, documentation, and submission files verified.

---

## 5. Day 1 — Foundation and core algorithms

**One major objective:** Create a maintainable project foundation and deliver tested Bubble Sort, Quickselect, and sorting-step data.  
**Estimate:** ~5 h 45 min, plus contingency.  
**Start condition:** Requirements and relevant prior-module work are available for review.

### Work package D1.1 — Repository and environment (~45 min)

- [ ] Create GitHub repository **AlgoNexis**, initialize Git locally, and choose the default branch.
- [ ] Create directories and `__init__.py` files shown in the project tree.
- [ ] Create `.venv`, record Python version, add `.gitignore` for venv, caches, secrets, and IDE files.
- [ ] Add `requirements.txt` with required direct dependencies (`streamlit`, `pytest`; plotting/testing extras as used).
- [ ] Add initial `README.md` with goal, scope, planned features, and launch/test placeholders clearly marked as not yet implemented.
- [ ] Inventory any existing stack, queue, tree, graph, and hash-table implementations for reuse on Day 2.

**Acceptance:** Repository has clean layout; Python environment activates; dependencies install; `git status` shows only intended tracked files.  
**Commit 01:** `chore: initialize AlgoNexis project structure`

### Work package D1.2 — Bubble Sort algorithm (~75 min)

- [ ] Implement adjacent-element compare/swap logic for integer lists.
- [ ] Add early-exit optimization when a pass completes without swaps.
- [ ] Capture a consistent, immutable snapshot for each comparison and/or swap event.
- [ ] Count comparisons and swaps accurately and return final sorted output.
- [ ] Specify whether the input is copied (recommended) or sorted in place; test that contract.
- [ ] Document best `O(n)` with early exit, average/worst `O(n²)`, and auxiliary-space implications.

**Acceptance:** Correct for ordinary, sorted, reversed, duplicate, negative, empty, and one-element lists; step count/values align with actual execution.  
**Commit 02:** `feat: implement bubble sort with step tracking`

### Work package D1.3 — Visualization engine (data layer) (~45 min)

- [ ] Create `visualization/sorting_visualizer.py` for preparing step descriptions.
- [ ] Provide stable metadata for highlighted indices and swap events.
- [ ] Expose total step count and an index-based step retrieval function.
- [ ] Represent initial state and final sorted state clearly.
- [ ] Check that advancing through recorded steps ends at the actual sorted list.

**Acceptance:** A non-UI test or example can iterate the steps in order; no Streamlit dependency is required yet.  
**Commit 03:** `feat: add sorting visualization engine`

### Work package D1.4 — Quickselect algorithm (~75 min)

- [ ] Implement partition-based selection for a **1-based** `k` parameter.
- [ ] Choose/document pivot policy; use randomized pivoting for expected linear performance if feasible.
- [ ] Reject empty input and `k < 1` or `k > n` with a clear exception.
- [ ] Handle repeated values, negatives, sorted lists, and reversed lists.
- [ ] Avoid unexpected caller-list mutation by copying internally or document/test a different policy.
- [ ] Document expected `O(n)` and worst `O(n²)` time for randomized Quickselect and relevant space costs.

**Acceptance:** `quickselect(values, k) == sorted(values)[k - 1]` across all valid test scenarios.  
**Commit 04:** `feat: implement quickselect with input validation`

### Work package D1.5 — Automated tests (~60 min)

- [ ] Create `tests/test_bubble_sort.py` and `tests/test_quickselect.py`.
- [ ] Test Bubble Sort on sorted/reverse/empty/single/negative/duplicate lists.
- [ ] Assert that recorded comparisons and swaps reconstruct the expected step sequence.
- [ ] Test Quickselect for first, median/middle, last, duplicates, and invalid `k`.
- [ ] Compare outputs with Python's `sorted()` as a reference oracle.
- [ ] Run `python -m pytest tests/ -v` and fix any failures.

**Acceptance:** All Day 1 tests pass, with no known critical algorithm defects.

### Work package D1.6 — Documentation and gate review (~45 min)

- [ ] Add usage examples for both algorithms to README or module docstrings.
- [ ] Explain inputs, outputs, errors, mutability, and complexity.
- [ ] Record the chosen API and pivot-policy decisions in `documentation/architecture.md`.
- [ ] Verify the visualization contract needed by Day 3 is consistent.
- [ ] Review Git diff, remove temporary debugging code, and commit tested files.

**Acceptance:** G1 passes and the algorithms can be imported without launching the UI.  
**Commit 05 (D1.5 + D1.6):** `test: add core algorithm tests and documentation`

#### Day 1 verification commands

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest tests/ -v
git status
```

#### Day 1 deliverables and gate G1

- [ ] `algorithms/bubble_sort.py` passes correctness and step-tracking tests.
- [ ] `algorithms/quickselect.py` passes selection and validation tests.
- [ ] `visualization/sorting_visualizer.py` exposes ordered, accurate step data.
- [ ] README and architecture notes describe the interfaces.
- [ ] **5 meaningful commits** represent completed work.

**Go/no-go decision:** Proceed to Day 2 only if core algorithm tests pass; otherwise correct defects before adding new functionality.

---

## 6. Day 2 — Custom sets and data structures

**One major objective:** Implement and verify the Custom Set plus Stack, Queue, BST, Graph, and Hash Table through one consistent manager.  
**Estimate:** ~7 h 30 min, including documentation/review.  
**Start condition:** Gate G1 passed.

### Work package D2.1 — Custom Set (~90 min)

- [ ] Create `CustomSet` with a documented storage strategy and uniqueness rules.
- [ ] Implement `add`, `remove`/`discard`, membership, size, and inspect/display.
- [ ] Implement `union` and `intersection` returning new sets.
- [ ] Implement `difference` and `symmetric_difference` returning new sets.
- [ ] Confirm results do not unexpectedly mutate operands.
- [ ] Test empty sets, overlap, disjoint sets, duplicates, and order-independent equality.
- [ ] Explain read-only/derived-set operations versus mutations in the documentation.

**Acceptance:** All four required operations match mathematical set semantics.  
**Commit 06:** `feat: implement custom set operations`

### Work package D2.2 — Stack and Queue (~60 min)

- [ ] Review/reuse previous-module code where appropriate.
- [ ] Implement Stack `push`, `pop`, `peek`, `is_empty`.
- [ ] Implement Queue `enqueue`, `dequeue`, `front`, `is_empty`.
- [ ] Choose a queue representation that avoids repeated `list.pop(0)` costs (e.g., `collections.deque`).
- [ ] Handle empty-state operations with consistent, documented errors.
- [ ] Provide a read-only way to display contents for the UI.

**Acceptance:** Stack obeys LIFO; Queue obeys FIFO; both handle empty states.  
**Commit 07:** `feat: add stack and queue implementations`

### Work package D2.3 — Binary Search Tree and Graph (~90 min)

- [ ] Implement BST node structure and insertion with a stated duplicate policy.
- [ ] Implement BST search and inorder/preorder/postorder traversals.
- [ ] Test empty, skewed, and multi-node trees.
- [ ] Implement Graph adjacency-list storage and add-vertex/add-edge operations.
- [ ] Implement BFS and DFS with a visited set and deterministic traversal ordering.
- [ ] Verify disconnected components and invalid starting vertices are handled clearly.
- [ ] Document graph type (undirected/unweighted) and BST balance limitations.

**Acceptance:** BST inorder traversal is ordered under chosen duplicate policy; BFS/DFS visit the expected reachable vertices.  
**Commit 08:** `feat: implement binary search tree and graph`

### Work package D2.4 — Hash Table (~60 min)

- [ ] Create hash-bucket storage for key-value pairs.
- [ ] Implement insertion/update, lookup, and deletion.
- [ ] Handle collisions using separate chaining.
- [ ] Define supported keys and missing-key behavior.
- [ ] Test collision cases deliberately, not only typical keys.
- [ ] Document average-case and worst-case search/insert/delete characteristics.

**Acceptance:** Colliding keys remain independently retrievable and deletable.  
**Commit 09:** `feat: add hash table with collision handling`

### Work package D2.5 — Unified manager (~60 min)

- [ ] Add `data_structures/manager.py` with a central registry of structures.
- [ ] Map allowed operation names to methods without `eval()` or dynamic execution.
- [ ] Define `execute(structure, operation, **kwargs)` or an equivalent documented API.
- [ ] Preserve instances for stateful operation sequences.
- [ ] Return plain, UI-friendly results and useful error messages.
- [ ] Verify every required structure and operation is reachable through the manager.

**Acceptance:** Integration calls work without the Streamlit UI; unsupported names are rejected cleanly.  
**Commit 10:** `feat: integrate data structures through unified manager`

### Work package D2.6 — Tests and regression (~60 min)

- [ ] Create tests for Set, Stack, Queue, BST, Graph, and Hash Table.
- [ ] Test manager dispatch and persistence of state between operations.
- [ ] Cover empty structures, duplicates, invalid requests, and collision scenarios.
- [ ] Re-run Day 1 tests to check for regressions.
- [ ] Fix detected defects and capture any behavior changes in docs.

**Acceptance:** All Day 1 and Day 2 unit tests pass.

### Work package D2.7 — Documentation and gate review (~30 min)

- [ ] Write `documentation/data_structures.md` with supported operations and examples.
- [ ] Add big-O expectations and important assumptions (tree balance, hash collision handling).
- [ ] Note which previous-module implementations were reused or adapted.
- [ ] Update architecture overview to include the manager.
- [ ] Verify G2, inspect diff, and commit completed work.

**Acceptance:** Interfaces are consistent and ready for Day 3 UI integration.  
**Commit 11 (D2.6 + D2.7):** `test: verify data structures and document operations`

#### Day 2 deliverables and gate G2

- [ ] `custom_set.py`, `stack.py`, `queue.py`, `tree.py`, `graph.py`, `hash_table.py` complete.
- [ ] `manager.py` can invoke all supported operations.
- [ ] Tests pass for correctness, edge conditions, and manager integration.
- [ ] Data structure documentation includes time/space trade-offs.
- [ ] **6 meaningful commits** represent completed work.

**Go/no-go decision:** Do not proceed to broad UI wiring until all manager operations have passing tests.

---

## 7. Day 3 — Interactive application and benchmarking

**One major objective:** Deliver a complete local interactive application, step-by-step Bubble Sort visualization, and reproducible performance measurement tools.  
**Estimate:** ~7 hours.  
**Start condition:** Gate G2 passed.

### Work package D3.1 — Streamlit shell (~60 min)

- [ ] Install/confirm Streamlit and create a working `app.py` entry point.
- [ ] Add navigation: Dashboard, Algorithms, Data Structures, Performance Analysis.
- [ ] Add short explanations and consistent input/output panels.
- [ ] Provide user-friendly exceptions rather than raw tracebacks where appropriate.
- [ ] Do a technical spike confirming `st.session_state` preserves a sample object.
- [ ] Launch with `streamlit run app.py` and check navigation.

**Acceptance:** App starts and each section renders without crashing.  
**Commit 12:** `feat: build Streamlit dashboard and navigation`

### Work package D3.2 — Algorithm UI (~60 min)

- [ ] Add text/sample dataset input with strict integer parsing.
- [ ] Connect Bubble Sort execution and show original/sorted lists.
- [ ] Show comparison and swap counts from real algorithm outputs.
- [ ] Add Quickselect input, `k` selector, and range validation.
- [ ] Display the kth smallest result and appropriate complexity notes.
- [ ] Reset stale results/steps if the input dataset changes.

**Acceptance:** Both algorithms run from the UI and display correct outputs and helpful errors.  
**Commit 13:** `feat: integrate bubble sort and quickselect interfaces`

### Work package D3.3 — Sorting visualization (~60 min)

- [ ] Connect Day 1 step records to a bar-chart or equivalent visual view.
- [ ] Highlight compared elements and swaps in the active step.
- [ ] Add Previous, Next, Reset, and current-step/total-step controls.
- [ ] Store the visualization index and dataset identity in session state.
- [ ] Show the initial and final states distinctly.
- [ ] Cap visualized input size (e.g., 50 elements) to avoid excessive step storage.
- [ ] Confirm navigating all steps ends at the sorted result.

**Acceptance:** A user can inspect the algorithm's progression in order without inconsistent UI resets.  
**Commit 14:** `feat: add interactive bubble sort visualization`

### Work package D3.4 — Data structure controls (~90 min)

- [ ] Provide Set input and buttons for all four binary operations plus add/remove.
- [ ] Add Stack push/pop/peek and Queue enqueue/dequeue/front views.
- [ ] Add BST insertion/search/traversal controls.
- [ ] Add Graph vertex/edge controls plus BFS/DFS start selection.
- [ ] Add Hash Table insert/search/delete controls.
- [ ] Route actions through the manager or the documented public APIs.
- [ ] Persist structure state across Streamlit reruns; provide a reset control.
- [ ] Display current contents and useful validation/error messages.

**Acceptance:** All six data structures work end to end through the UI.  
**Commit 15:** `feat: build interactive data structure controls`

### Work package D3.5 — Benchmark framework (~60 min)

- [ ] Implement timing with `time.perf_counter_ns()` or `time.perf_counter()`.
- [ ] Implement Python-tracked peak allocation measurement with `tracemalloc`.
- [ ] Separate timing trials from memory-measurement trials when feasible to reduce instrumentation bias.
- [ ] Define dataset sizes **10, 100, 1,000, 5,000** where practical; guard Bubble Sort workload.
- [ ] Support random, sorted, reverse-sorted, and duplicate-heavy lists.
- [ ] Use fixed random seeds, a warm-up where useful, and repeated trials (e.g., 5).
- [ ] Capture implementation, operation, size, pattern, trial, elapsed time, peak tracked bytes, seed, and environment.
- [ ] Check benchmark correctness after each trial and export CSV-ready rows.

**Acceptance:** Repeatable runs produce actual numeric measurements, not illustrative or hard-coded results.  
**Commit 16:** `perf: implement execution time and memory benchmarking`

### Work package D3.6 — Performance dashboard (~45 min)

- [ ] Create execution-time tables and charts by dataset size.
- [ ] Create tracked-memory tables/charts with the measurement definition displayed.
- [ ] Show counts (comparisons/swaps) only for algorithms that expose them.
- [ ] Include operation-level comparisons for data structures with clear labels.
- [ ] Provide download/export of `results/benchmark_results.csv`.
- [ ] Explain that Bubble Sort and Quickselect solve **different problems**, so timings are not proof one replaces the other.

**Acceptance:** Charts use measured values and labels are not misleading.  
**Commit 17:** `feat: add performance charts and benchmark dashboard`

### Work package D3.7 — End-to-end validation (~45 min)

- [ ] Test navigation and each algorithm/data structure through the actual app.
- [ ] Test invalid integers, invalid `k`, empty values, unsupported operations, and resets.
- [ ] Verify session state does not leak prior datasets into new results.
- [ ] Check visualization last-step correctness and benchmark CSV values.
- [ ] Run the complete pytest suite and fix integration regressions.
- [ ] Record any limitations for the final report and user guide.

**Acceptance:** G3 passes; no critical user workflow is broken.  
**Commit 18:** `test: validate UI integration and performance tools`

#### Day 3 verification commands

```bash
python -m pytest tests/ -v
streamlit run app.py
# In the application: manually exercise algorithms, all structures, charts, and CSV export.
```

#### Day 3 deliverables and gate G3

- [ ] Working Streamlit portfolio with all required sections.
- [ ] Bubble Sort step-through visualization and Quickselect input/result interface.
- [ ] Working Set, Stack, Queue, BST, Graph, and Hash Table interactions.
- [ ] Reproducible benchmark framework and real measured outputs.
- [ ] Accurate tables/charts plus CSV export.
- [ ] **7 meaningful commits** represent completed work.

**Go/no-go decision:** Day 4 writing must use verified Day 3 measurements; fix missing benchmark or UI data before drafting conclusions.

---

## 8. Day 4 — Final QA, report, presentation, release

**One major objective:** Verify every deliverable and produce a complete, academically defensible, submission-ready portfolio.  
**Estimate:** ~7 h 20 min, plus contingency.  
**Start condition:** Gate G3 passed.

### Work package D4.1 — Final regression and integration QA (~75 min)

- [ ] Run all tests from a fresh environment, record pass/fail results.
- [ ] Verify Bubble Sort, Quickselect, Set operations, and all five data structures.
- [ ] Verify visualization indices, UI navigation, state persistence, and reset paths.
- [ ] Exercise failure cases and ensure bounded input handling.
- [ ] Run `python -m compileall -q algorithms data_structures visualization performance app.py`.
- [ ] Fix critical defects and re-run affected and full suites.
- [ ] Record known noncritical limitations in documentation.

**Acceptance:** No critical defects; reproducible tests pass.  
**Commit 19:** `test: complete final regression and integration testing`

### Work package D4.2 — Final benchmark runs and evidence (~60 min)

- [ ] Confirm software/hardware/Python environment details for the report.
- [ ] Run timed trials across approved input sizes and patterns.
- [ ] Run separate peak tracked-allocation trials where feasible.
- [ ] Check each operation's result for correctness before recording performance.
- [ ] Compute representative summary statistics (mean, optionally median and spread).
- [ ] Save `results/benchmark_results.csv` and generated chart assets if used.
- [ ] Identify effects of input order, repeated values, tree skew, and hash collisions where observed.

**Acceptance:** Raw data, chart labels, and reported summary values agree.  
**Commit 20:** `perf: finalize benchmarks and performance analysis`

### Work package D4.3 — Comprehensive performance report (~120 min)

**Target:** **At least five substantive pages**, excluding an unusually large title page/reference-only filler. Follow specific course page and APA requirements if provided.

- [ ] **Introduction (~½ page):** objective, system scope, and why performance analysis matters.
- [ ] **Algorithm/data structure overview (~1 page):** describe the actual implementations and complexity expectations.
- [ ] **Methodology (~1 page):** environment, input patterns/sizes, seeds, repetitions, timing, memory limits, and caveats.
- [ ] **Results (~1½ pages):** insert actual CSV-derived tables/charts; discuss patterns and variability.
- [ ] **Trade-offs (~1 page):** Bubble Sort simplicity vs quadratic behavior, Quickselect pivot sensitivity, unbalanced BST, hash collisions, BFS/DFS complexity, Set/Queue representation.
- [ ] **Conclusion (~½ page):** evidence-based findings, limitations, and future improvements.
- [ ] **References:** use required course style (APA 7 if applicable); properly attribute algorithms, libraries, and outside claims.
- [ ] Review academic style: define terms before evaluating them; prefer third person, original paraphrasing, analytical reasoning, and accurate in-text citations.

**Mandatory cautions for the report:**

- Bubble Sort and Quickselect perform **different tasks**; discuss their scaling without calling them equivalent competitors.
- Distinguish theoretical complexity from observed benchmark measurements.
- `tracemalloc` reports **Python-tracked allocations**, not whole-process resident memory.
- For a BST, average vs worst-case performance depends on balance; for hash tables, collision policy and load factor matter.
- No invented timings, memory readings, source citations, test counts, or screenshots.

**Acceptance:** `documentation/performance_analysis_report.pdf` opens, has 5+ substantive pages, and all figures match recorded data.  
**Commit 21:** `docs: add comprehensive performance analysis report`

### Work package D4.4 — Final portfolio presentation (~75 min)

- [ ] Prepare **PowerPoint slides or video** (slides are the default here unless the course requests video).
- [ ] Create a 10–12-slide narrative: title, purpose, architecture, Bubble Sort, Quickselect, Set, linear structures, tree/graph/hash, UI, benchmarks, learning outcomes, conclusion.
- [ ] Use authentic screenshots of the finished app and actual benchmark charts.
- [ ] Explain why each data structure was chosen and its main performance trade-off.
- [ ] Verify fonts, layouts, readable charts, title information, and slide order.
- [ ] Rehearse a concise walkthrough that explicitly covers all assignment requirements.

**Acceptance:** `documentation/portfolio_presentation.pptx` opens correctly and demonstrates both implementation and learning outcomes.

### Work package D4.5 — Final technical documentation (~45 min)

- [ ] Complete README: overview, features, technology, structure, setup, launch, usage, test, and limitations.
- [ ] Complete `documentation/user_guide.md` with inputs and instructions for every UI section.
- [ ] Complete `documentation/architecture.md` with module diagram and design decisions.
- [ ] Confirm `documentation/data_structures.md` includes operation examples and assumptions.
- [ ] Confirm documentation uses commands that work from a fresh clone.
- [ ] Update dependency list to match installed packages and remove unused packages.

**Acceptance:** An unfamiliar reader can install, run, test, and use the portfolio without guessing.

### Work package D4.6 — Release readiness (~45 min)

- [ ] Run full tests once more after all edits.
- [ ] Test a clean install and `streamlit run app.py`.
- [ ] Verify every expected submission file opens and is not empty/corrupted.
- [ ] Inspect Git for secrets, temporary files, caches, venvs, large unintended assets, and debug output.
- [ ] Create a ZIP of required files **if** the course requests a single archive; exclude `.venv`, `.git`, caches, and unnecessary intermediates.
- [ ] Confirm commits, repo status, and the eight required deliverables.

**Acceptance:** G4 release checklist passes, with no unstaged submission changes.

### Work package D4.7 — Short retrospective (~20 min)

- [ ] Record what was delivered against the initial scope.
- [ ] Summarize the most important algorithm and integration challenges.
- [ ] Explain how defects and performance-measurement issues were resolved.
- [ ] Record what worked well in the four-day process.
- [ ] Identify two or three realistic improvements for a future version.

**Acceptance:** `documentation/retrospective.md` captures learning and known limitations.  
**Commit 22 (D4.4–D4.7):** `docs: finalize presentation and release documentation`

#### Day 4 release commands

```bash
python -m pytest tests/ -v
python -m compileall -q algorithms data_structures visualization performance app.py
streamlit run app.py
git status
git log --oneline -22
# Only after G4 passes and all files are committed:
git tag -a v1.0.0 -m "AlgoNexis Portfolio v1.0.0"
```

#### Day 4 deliverables and gate G4

- [ ] Full source code and working UI.
- [ ] All tests pass and major workflows manually verified.
- [ ] Verified benchmark CSV plus performance charts.
- [ ] **5+ page** substantive performance analysis report.
- [ ] Final slides **or** video showing real system capabilities.
- [ ] Complete README, architecture notes, user guide, and design decisions.
- [ ] Retrospective and final release checklist.
- [ ] **4 meaningful commits** representing completed work; version tag only after release.

---

## 9. Complete Git commit schedule

### 9.1 Commit accounting

| Day | Count | Number range | Cumulative |
|---|---:|---|---:|
| Day 1 | **5** | 01–05 | 5 |
| Day 2 | **6** | 06–11 | 11 |
| Day 3 | **7** | 12–18 | 18 |
| Day 4 | **4** | 19–22 | **22** |

### 9.2 Ordered commit messages and expected changes

| # | Day | Commit message | Scope that must exist before commit |
|---:|---|---|---|
| 01 | 1 | `chore: initialize AlgoNexis project structure` | Repo, folders, requirements, README, ignores |
| 02 | 1 | `feat: implement bubble sort with step tracking` | Sort logic, statistics, steps |
| 03 | 1 | `feat: add sorting visualization engine` | Consumable step data and navigation helpers |
| 04 | 1 | `feat: implement quickselect with input validation` | Partitioning, valid ranks, errors |
| 05 | 1 | `test: add core algorithm tests and documentation` | Algorithm tests and usage/complexity notes |
| 06 | 2 | `feat: implement custom set operations` | Set class, uniqueness, four operations |
| 07 | 2 | `feat: add stack and queue implementations` | LIFO/FIFO operations and errors |
| 08 | 2 | `feat: implement binary search tree and graph` | BST traversal/search; Graph BFS/DFS |
| 09 | 2 | `feat: add hash table with collision handling` | Key/value CRUD and separate chaining |
| 10 | 2 | `feat: integrate data structures through unified manager` | Manager dispatch and stateful access |
| 11 | 2 | `test: verify data structures and document operations` | All structures/manager tests, docs |
| 12 | 3 | `feat: build Streamlit dashboard and navigation` | App shell, sections, startup |
| 13 | 3 | `feat: integrate bubble sort and quickselect interfaces` | Algorithm controls and results |
| 14 | 3 | `feat: add interactive bubble sort visualization` | Step chart and navigation |
| 15 | 3 | `feat: build interactive data structure controls` | All six structure panels |
| 16 | 3 | `perf: implement execution time and memory benchmarking` | Measurement and repeatable datasets |
| 17 | 3 | `feat: add performance charts and benchmark dashboard` | Tables/charts/export |
| 18 | 3 | `test: validate UI integration and performance tools` | Integration checks and fixes |
| 19 | 4 | `test: complete final regression and integration testing` | Final code QA and fixes |
| 20 | 4 | `perf: finalize benchmarks and performance analysis` | Verified raw/summary benchmark evidence |
| 21 | 4 | `docs: add comprehensive performance analysis report` | Final PDF report |
| 22 | 4 | `docs: finalize presentation and release documentation` | Slides, guides, retrospective, release checks |

### 9.3 Safe Git workflow per completed work package

```bash
# Inspect exactly what changed
git status
git diff

# Stage only relevant files (example; replace paths with files actually changed)
git add algorithms/bubble_sort.py

# Commit only completed, verified work
git commit -m "feat: implement bubble sort with step tracking"

# Confirm actual history
git log --oneline -5
```

Commit messages are a **schedule**, not commands to run in bulk. Do not pre-create commits, invent functionality, change timestamps to simulate activity, or add empty commits to hit the target count. If the implementation legitimately needs a different split, update the plan and keep each commit meaningful.

---

## 10. Testing, benchmarking, and security strategy

### 10.1 Test matrix

| Feature | Normal cases | Edge cases / failure cases | Reference check |
|---|---|---|---|
| Bubble Sort | Mixed integers, ascending result | Empty, single, sorted, reverse, duplicates, negatives | `sorted(values)` |
| Step records | Each compare/swap is represented | Zero swaps, repeated values | Replay states → final sorted list |
| Quickselect | First/middle/last rank | Empty, invalid k, duplicates | `sorted(values)[k-1]` |
| Custom Set | Four required operations | Empty, disjoint, identical, duplicates | Mathematical set semantics (test oracle only) |
| Stack | Push/pop/peek | Empty pop/peek | LIFO order |
| Queue | Enqueue/dequeue/front | Empty dequeue/front | FIFO order |
| BST | Insert/search/traverse | Empty, duplicates, skew | Inorder consistency |
| Graph | Vertex/edge/BFS/DFS | Disconnected, invalid start, cycles | Expected reachable set/order |
| Hash Table | Add/update/get/delete | Collisions, missing key | Expected key/value behavior |
| Manager | All dispatch paths | Unknown structure/operation | Correct target method/error |
| UI | Input and display for each feature | Bad parsing, stale state, reset | Manual end-to-end cases |
| Benchmarks | Multiple sizes/trials | Bounds, invalid samples | Recomputed outputs and CSV/chart agreement |

### 10.2 Benchmark measurement protocol

1. **Environment:** Record Python version, OS, processor description if available, installed relevant package versions, and benchmark date.
2. **Inputs:** Fixed-seed datasets of 10, 100, 1,000, and 5,000 values when feasible. Include random, sorted, reverse-sorted, and duplicate-heavy patterns. Document any skipped large Bubble Sort runs.
3. **Repetitions:** At least five timed trials for suitable operations, with warm-up as appropriate; report mean and ideally median/spread.
4. **Measurement:** Use `perf_counter` for elapsed time. Use `tracemalloc` separately for Python-tracked peak allocations; do not relabel it as total system RAM.
5. **Correctness check:** Confirm every timed operation returns an expected result. Discard and investigate failed runs rather than recording misleading values.
6. **Comparability:** Separate algorithm selection from sorting and separate unrelated data structure operations. Use scaling trends and theoretical analysis when operations differ in purpose.
7. **Bias control:** Do not include Streamlit widget rendering or chart creation in algorithm timings. Avoid large input generation inside timed regions unless input generation is explicitly the measured activity.
8. **Evidence:** Preserve raw observations in CSV; calculate summaries transparently; generate charts from the same dataset.

**Suggested CSV fields:** `timestamp,algorithm_or_structure,operation,input_size,input_pattern,seed,trial,elapsed_ms,peak_tracemalloc_bytes,comparisons,swaps,python_version,notes`.

### 10.3 Basic security and reliability measures

- Parse submitted integer lists explicitly; **never** execute user-provided code or use `eval()`.
- Validate `k`, graph vertices, missing keys, and unsupported manager operations.
- Limit maximum UI list length and benchmark size to keep the local app responsive.
- Do not check in `.env`, API keys, student credentials, or unrelated personal data.
- Keep dependencies minimal and test a clean installation.
- Treat CSV output as generated evidence and avoid unsafe path construction from user input.
- State limits openly; this is an educational local application, not a production service.

---

## 11. Deliverable-to-requirement traceability

| # | Required deliverable | Planned evidence | Day completed | Acceptance check |
|---:|---|---|---:|---|
| 1 | Bubble Sort source with visualization | `algorithms/bubble_sort.py`, `visualization/sorting_visualizer.py`, UI | 1 + 3 | Correct sorting and inspectable sequential steps |
| 2 | Quickselect source | `algorithms/quickselect.py` | 1 | Correct kth value, validated input |
| 3 | Complete Set class | `data_structures/custom_set.py`, docs/tests | 2 | Four set operations correct and documented |
| 4 | Integrated portfolio | `data_structures/manager.py` and app integrations | 2 + 3 | All course structures accessible |
| 5 | Interactive user interface | `app.py` | 3 | User can test algorithms and structures |
| 6 | Performance report (5+ pages) | `documentation/performance_analysis_report.pdf` | 4 | Actual comparisons, charts, meaningful trade-offs |
| 7 | Final presentation | `documentation/portfolio_presentation.pptx` **or** video | 4 | Demonstrates working system and learning |
| 8 | Complete documentation | `README.md`, user guide, architecture, DS docs | 4 | Setup, usage, design decisions are clear |

**Assignment-level success criteria:** Bubble Sort sorts and visualizes, Quickselect selects efficiently, sets operate correctly, all structures integrate, the analysis conveys trade-offs, and the final presentation explains technical achievement and learning.

---

## 12. Documentation and presentation artifacts

### 12.1 Required / recommended files

| Artifact | Purpose | Owner/day |
|---|---|---|
| `README.md` | Project overview, install, run, test, known limitations | Start D1, finalize D4 |
| `documentation/architecture.md` | Module map, APIs, interface and design decisions | Start D1, update D2–D4 |
| `documentation/data_structures.md` | Supported operations, definitions, use cases, complexity | D2 |
| `documentation/user_guide.md` | How to use algorithms, structures, visualizer, benchmarks | D4 |
| `results/benchmark_results.csv` | Reproducible measurement evidence | D3–D4 |
| `documentation/performance_analysis_report.pdf` | 5+ page analysis | D4 |
| `documentation/portfolio_presentation.pptx` | Visual system demonstration; substitute video if chosen | D4 |
| `documentation/retrospective.md` | Challenges, decisions, learning, enhancements | D4 |

### 12.2 Essential architecture documentation

Include one simple diagram (ASCII/Markdown is acceptable), the manager dispatch interface, module dependencies, data ownership, session-state decisions, and short notes on representation choices. Avoid elaborate UML unless specifically requested.

### 12.3 Academic style checklist for the report

- [ ] Third-person, formal academic writing; define terms before deeper analysis.
- [ ] Analytical explanations: why measurements differ, which assumptions matter, where an approach is useful.
- [ ] Paraphrase responsibly; cite external technical facts and sources.
- [ ] Use page/paragraph/section locators for any direct quote where required.
- [ ] Center the **References** heading; alphabetize references in the required format.
- [ ] Label actual evidence, theoretical expectations, and limitations separately.
- [ ] Confirm report and reference format against course-specific instructions.

---

## 13. Risks, dependencies, and contingency plan

| Risk | Likelihood / impact | Early signal | Response |
|---|---|---|---|
| Prior-module code unavailable or inconsistent | Medium / High | D1 inventory reveals missing APIs | Implement minimal correct operations first; prioritize required methods |
| Scope too large for four days | Medium / High | D2 takes longer than planned | Reuse tested modules, defer cosmetic enhancements, preserve all required functionality |
| Streamlit session state errors | Medium / Medium | UI loses operations on rerun | Prototype state on D3.1 before full control integration |
| Benchmark runs are too slow | Medium / Medium | Bubble Sort size 5,000 causes delays | Cap sizes, run batch offline, document bounded sample selection |
| Unstable timing results | High / Medium | Large trial-to-trial variance | Repeat, summarize distributions, control seeds, describe limitations |
| Misleading algorithm comparison | Medium / High | Report calls Quickselect “faster sort” | Compare scaling but distinguish distinct tasks |
| Report or slides rushed | Medium / High | Day 3 lacks verified charts | Begin report outline before Day 4; reserve Day 4 for verified results and clear interpretation |
| Wrong citation/format requirements | Medium / Medium | Course rubric differs from assumptions | Reconcile requirements before final PDF/slides export |

**Priority if time is limited:** (1) correct core algorithms/sets/structures, (2) working unified UI, (3) validated measurements, (4) required 5+ page report and presentation, (5) aesthetic refinements. Never replace missing required deliverables with optional polish.

---

## 14. Final release checklist and retrospective

### 14.1 Functional completion

- [ ] Bubble Sort produces correct output and meaningful step-by-step visualization.
- [ ] Quickselect returns correct 1-based kth smallest value on validated inputs.
- [ ] Custom Set supports union, intersection, difference, symmetric difference.
- [ ] Stack, Queue, BST, Graph, and Hash Table work individually and through unified integration.
- [ ] Streamlit app exposes all required operations, handles invalid inputs, and maintains state.
- [ ] Benchmark tools produce repeatable, labeled execution-time and memory evidence.

### 14.2 Submission completion

- [ ] All tests and clean-environment startup checks pass.
- [ ] `performance_analysis_report.pdf` is at least five substantive pages.
- [ ] Report interpretations match the recorded CSV and chart values.
- [ ] Presentation (slides **or** video) demonstrates the finished application and learning outcomes.
- [ ] README, installation instructions, user guide, and design decisions are complete.
- [ ] No secrets, caches, venvs, unused large files, or false placeholder results are included.
- [ ] Source and document files open correctly after packaging.
- [ ] All **22 planned commits**, if they match genuine completed work, are present in sequence.
- [ ] Final release tag `v1.0.0` is created only after all G4 checks pass.

### 14.3 Retrospective prompts

In `documentation/retrospective.md`, briefly answer:

1. Which requirement was hardest to implement, and why?
2. Which edge case or integration defect revealed an important design issue?
3. What did benchmark results show about theoretical vs observed performance?
4. What went well across the four daily gates?
5. What would be improved next (e.g., balanced trees, additional algorithms, richer visuals, stronger benchmark controls)?

---

## Final acceptance statement

**AlgoNexis is ready for submission when Gate G4 passes and all eight assignment deliverables are present and verified.** The project should demonstrate algorithm correctness, an interactive end-to-end portfolio, defensible performance analysis, a clear final presentation, and reproducible installation/testing instructions.

**Planning references:** The project requirements, deliverables, and success criteria supplied in the conversation; the supplied *PSEPF Project Implementation Prompt* (sections on assessment, levels, methodology, modifiers, daily tasks, Git history, gates, and release); and the supplied *Updated Feedback Notes for Future Assignments* (academic writing, analysis, and APA review). These sources are planning inputs; no unverified benchmark results or course-specific grading rules are assumed.
