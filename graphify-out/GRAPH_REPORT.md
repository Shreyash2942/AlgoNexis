# Graph Report - AlgoNexis Day 1  (2026-11-04)

## Corpus Check
- Corpus is ~14,814 words - fits in a single context window. You may not need a graph.

## Summary
- 138 nodes · 260 edges · 12 communities detected
- Extraction: 81% EXTRACTED · 16% INFERRED · 3% AMBIGUOUS · INFERRED: 42 edges (avg confidence: 0.6)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Quickselect Implementation and Tests
- Sorting Frames and Playback
- Portfolio Delivery and Measurement
- Verified Day One Contracts
- Bubble Sort and Trace Tests
- Future Structures and Coursework
- Shared Integer Validation
- Algorithm Package Boundary
- Structure Package Boundary
- Performance Package Boundary
- Test Package Boundary
- Visualization Package Boundary

## God Nodes (most connected - your core abstractions)
1. `bubble_sort()` - 19 edges
2. `quickselect()` - 18 edges
3. `AlgoNexis Portfolio` - 16 edges
4. `SortingVisualizer` - 14 edges
5. `71 Passing Day 1 Tests` - 13 edges
6. `BubbleSortResult` - 12 edges
7. `Implemented SortingVisualizer` - 12 edges
8. `Verified Day 1 Foundation and Algorithms` - 11 edges
9. `Planned Day 2 Structures and Manager` - 11 edges
10. `Implemented Bubble Sort` - 10 edges

## Surprising Connections (you probably didn't know these)
- `Frozen SortingStep` --references--> `SortingStep`  [EXTRACTED]
  documentation/architecture.md → algorithms\bubble_sort.py
- `Prepare immutable Bubble Sort frames without a Streamlit dependency.  Example:` --uses--> `BubbleSortResult`  [AMBIGUOUS]
  visualization\sorting_visualizer.py → algorithms\bubble_sort.py
- `UI-ready metadata; values reuse the algorithm's immutable snapshot.` --uses--> `BubbleSortResult`  [AMBIGUOUS]
  visualization\sorting_visualizer.py → algorithms\bubble_sort.py
- `Read-only, index-based view of a traced BubbleSortResult.      Indices are zero-` --uses--> `BubbleSortResult`  [AMBIGUOUS]
  visualization\sorting_visualizer.py → algorithms\bubble_sort.py
- `Number of available frames, including initial and final states.` --uses--> `BubbleSortResult`  [AMBIGUOUS]
  visualization\sorting_visualizer.py → algorithms\bubble_sort.py

## Hyperedges (group relationships)
- **Verified Sorting Record and Frame Flow** — readme_bubble, arch_result, arch_step, readme_visualizer, arch_frame [EXTRACTED 1.00]
- **Sequential Daily Quality Gates** — readme_g1, readme_g2, readme_g3, readme_g4 [EXTRACTED 1.00]
- **Day 1 Verified Algorithm and Playback Evidence** — readme_bubble, readme_quickselect, readme_visualizer, readme_tests, arch_imports [EXTRACTED 1.00]

## Communities

### Community 0 - "Quickselect Implementation and Tests"
Cohesion: 0.17
Nodes (20): quickselect(), Iterative randomized Quickselect with one-based ranks and duplicate support.  Un, Return the kth-smallest integer without sorting or changing caller data.      Ra, Random, test_seeded_random_traces_match_oracle_and_inversion_count(), One-based selection correctness and reproducible partition policy checks., Observe the public RNG contract without duplicating selection logic., RecordingRandom (+12 more)

### Community 1 - "Sorting Frames and Playback"
Cohesion: 0.14
Nodes (17): BubbleSortResult, Sorted values, exact operation totals, and an optional event sequence., Prepare immutable Bubble Sort frames without a Streamlit dependency.  Example:, UI-ready metadata; values reuse the algorithm's immutable snapshot., Read-only, index-based view of a traced BubbleSortResult.      Indices are zero-, Number of available frames, including initial and final states., Return the requested frame without altering playback or result state., Yield every frame in execution order, without keeping a cursor. (+9 more)

### Community 2 - "Portfolio Delivery and Measurement"
Cohesion: 0.15
Nodes (23): Verified Evidence and No Placeholder Results, Iterative Randomized Three-Way Partition, Repeatable Pivots Without Global RNG Mutation, Independent Core and Future UI, Planned Day 3 UI and Measurements, Planned Day 4 Submission Preparation, Controlled Quickselect Pivot Randomness, Reproducible Measurement Protocol (+15 more)

### Community 3 - "Verified Day One Contracts"
Cohesion: 0.16
Nodes (22): Caller Input Preservation, Frozen SortingFrame, Standard-Library-Only Core Imports, Avoid Snapshot Costs in Large Execution Trials, Frozen BubbleSortResult, Frozen SortingStep, Full Snapshot Time and Storage Costs, Explicit Trace-Disabled Benchmark Mode (+14 more)

### Community 4 - "Bubble Sort and Trace Tests"
Cohesion: 0.17
Nodes (16): bubble_sort(), Adjacent-element Bubble Sort with an optional complete, immutable trace.  The ca, One observed event; counters are cumulative as of this snapshot.      A compare, Return a nonmutating sort result; duplicates keep their relative order.      ``t, SortingStep, assert_replay(), Correctness, event replay, operation counts, and immutable snapshot checks., Independently replay the emitted actions rather than another sort loop. (+8 more)

### Community 5 - "Future Structures and Coursework"
Cohesion: 0.23
Nodes (13): Planned Day 2 Structures and Manager, Next D2.1 Custom Set Implementation, Planned Unbalanced Binary Search Tree, Planned Undirected Adjacency-List Graph, Planned Separate-Chaining Hash Table, Planned Queue, Planned Custom Set, Planned Stack (+5 more)

### Community 6 - "Shared Integer Validation"
Cohesion: 0.5
Nodes (3): copy_integer_list(), Shared input contract for integer-list algorithms., Validate a Python list of integers (excluding bool) and return a copy.

### Community 7 - "Algorithm Package Boundary"
Cohesion: 1.0
Nodes (1): UI-independent algorithms for AlgoNexis.

### Community 8 - "Structure Package Boundary"
Cohesion: 1.0
Nodes (1): Package reserved for the verified Day 2 data structures.

### Community 9 - "Performance Package Boundary"
Cohesion: 1.0
Nodes (1): Package reserved for the Day 3 performance measurement tools.

### Community 10 - "Test Package Boundary"
Cohesion: 1.0
Nodes (1): Automated AlgoNexis correctness and integration checks.

### Community 11 - "Visualization Package Boundary"
Cohesion: 1.0
Nodes (1): UI-independent visualization data for AlgoNexis.

## Ambiguous Edges - Review These
- `BubbleSortResult` → `Prepare immutable Bubble Sort frames without a Streamlit dependency.  Example:`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `UI-ready metadata; values reuse the algorithm's immutable snapshot.`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Read-only, index-based view of a traced BubbleSortResult.      Indices are zero-`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Number of available frames, including initial and final states.`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Return the requested frame without altering playback or result state.`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Yield every frame in execution order, without keeping a cursor.`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `Day 3's data-only playback contract and core import isolation.` → `SortingVisualizer`  [AMBIGUOUS]
  tests\test_sorting_visualizer.py · relation: uses

## Knowledge Gaps
- **23 isolated node(s):** `Adjacent-element Bubble Sort with an optional complete, immutable trace.  The ca`, `One observed event; counters are cumulative as of this snapshot.      A compare`, `Sorted values, exact operation totals, and an optional event sequence.`, `Return a nonmutating sort result; duplicates keep their relative order.      ``t`, `Iterative randomized Quickselect with one-based ranks and duplicate support.  Un` (+18 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Algorithm Package Boundary`** (2 nodes): `__init__.py`, `UI-independent algorithms for AlgoNexis.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Structure Package Boundary`** (2 nodes): `__init__.py`, `Package reserved for the verified Day 2 data structures.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Performance Package Boundary`** (2 nodes): `__init__.py`, `Package reserved for the Day 3 performance measurement tools.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Test Package Boundary`** (2 nodes): `__init__.py`, `Automated AlgoNexis correctness and integration checks.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Visualization Package Boundary`** (2 nodes): `__init__.py`, `UI-independent visualization data for AlgoNexis.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `BubbleSortResult` and `Prepare immutable Bubble Sort frames without a Streamlit dependency.  Example:`?**
  _Edge tagged AMBIGUOUS (relation: uses) - confidence is low._
- **What is the exact relationship between `BubbleSortResult` and `UI-ready metadata; values reuse the algorithm's immutable snapshot.`?**
  _Edge tagged AMBIGUOUS (relation: uses) - confidence is low._
- **What is the exact relationship between `BubbleSortResult` and `Read-only, index-based view of a traced BubbleSortResult.      Indices are zero-`?**
  _Edge tagged AMBIGUOUS (relation: uses) - confidence is low._
- **What is the exact relationship between `BubbleSortResult` and `Number of available frames, including initial and final states.`?**
  _Edge tagged AMBIGUOUS (relation: uses) - confidence is low._
- **What is the exact relationship between `BubbleSortResult` and `Return the requested frame without altering playback or result state.`?**
  _Edge tagged AMBIGUOUS (relation: uses) - confidence is low._
- **What is the exact relationship between `BubbleSortResult` and `Yield every frame in execution order, without keeping a cursor.`?**
  _Edge tagged AMBIGUOUS (relation: uses) - confidence is low._
- **What is the exact relationship between `Day 3's data-only playback contract and core import isolation.` and `SortingVisualizer`?**
  _Edge tagged AMBIGUOUS (relation: uses) - confidence is low._

## Verified Day 1 Outcome

D1.1-D1.6 implemented: environment and dependency lock, adjacent Bubble Sort with immutable complete event records and explicit trace opt-out, randomized three-way Quickselect with controlled RNG, non-UI sorting frames, and documented APIs. The full suite passed 71 tests; doctests, compilation, Python 3.11 grammar parsing, pip dependency checks, and standard-library-only core imports also passed.

See [Day 1 evidence](../documentation/day1_verification.md). Days 2-4 are planned/unverified; previous coursework is inventory only. No application benchmark measurements or submission artifacts are claimed.

## Graph Extraction Audit

AST plus six refreshed documents were rebuilt together, replacing stale planning-only status. Six explicit API references in architecture notes resolve to the code declarations. Package-docstring IDs were namespaced by source file to avoid identical __init__.py names merging distinct nodes. AST file-import co-occurrence edges remain heuristic: code candidates have INFERRED confidence 0.6; rationale-to-import candidates have AMBIGUOUS confidence 0.2. These are not verified function calls. Explicit source relationships have confidence 1.0.


## Estimated Retrieval Benchmark

Heuristic context-size estimates, not measured tokens, monetary savings, or an answer-quality comparison.

- Full corpus estimate: 19752 tokens
- Average graph query estimate: 3297 tokens
- Estimated reduction: 6.0x
