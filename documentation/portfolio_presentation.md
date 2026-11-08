# AlgoNexis — final presentation

## 1. AlgoNexis

- An interactive algorithms & data structures portfolio
- Shreyash · CSU Global · CSC506
- November 7, 2026 · Portfolio v1.0.0

Evidence image: `documentation/screenshots/dashboard.png`

Source: AlgoNexis implementation and recorded measurements

## 2. One portfolio, four ways to explore

- Dashboard: scope and guide
- Algorithms: sort, select, inspect steps
- Data Structures: six persistent models
- Performance: measurements and CSV

Evidence image: `documentation/screenshots/dashboard-mobile.png`

Source: AlgoNexis implementation and recorded measurements

## 3. Architecture keeps the core independently testable



- Streamlit views and session state call plain Python APIs.
- Algorithms emit immutable frames; the manager owns six structures.
- Direct core benchmarks produce CSV, figures, report, and slides.

Source: AlgoNexis implementation and recorded measurements

## 4. Bubble Sort: make every comparison inspectable

- Adjacent compare and swap
- Early exit: O(n) best case
- O(n²) average / worst, untraced
- Immutable snapshots; trace limit 50

Evidence image: `documentation/screenshots/sorting-steps.png`

Algorithm background: OpenDSA, Bubble sort; project early-exit and trace contracts

## 5. Quickselect: ask for one rank

- One-based k; duplicates retain ranks
- Randomized three-way partition
- Expected O(n); worst O(n²)
- Copy preserves the caller’s input

Evidence image: `results/figures/quickselect.png`

Selection background: Sedgewick & Wayne, Quick.java; means/min–max from final CSV

## 6. Custom Set: membership defines equality

- Dictionary-backed membership
- Explicit union / intersection loops
- Difference and symmetric difference
- Derived results preserve both operands

Source: AlgoNexis implementation and recorded measurements

## 7. Stack and Queue: order determines representation

- Stack: list end → LIFO, amortized O(1) push
- Queue: deque ends → FIFO, O(1) removal
- Empty removal raises a clear IndexError
- Draining n elements is an O(n) batch

Python Software Foundation, collections — deque end operations and list front-removal costs

## 8. Tree, Graph, Hash Table: expose the trade-offs

- BST: ordered keys; shape controls search
- Graph: undirected adjacency; BFS / DFS
- Hash Table: fixed separate chains
- One bucket / 2n lookup means: 68.20×

Evidence image: `results/figures/hash_collisions.png`

Sedgewick & Wayne: BST.java, BreadthFirstPaths.java, SeparateChainingHashST.java; controlled CSV

## 9. The interface is part of correctness

- Strict integer parsing; no eval
- Separate model and widget state
- Explicit growth and trace limits
- Navigation, failures, resets checked in Edge

Evidence image: `documentation/screenshots/algorithms.png`

Source: AlgoNexis implementation and recorded measurements

## 10. Measure the work that the label describes

- 1,080 observed rows + 8 guarded skips
- Five timing + five allocation repeats per case
- Setup / checking excluded; output included
- Separate 60-row controlled collision profile

Evidence image: `results/figures/bubble_sort.png`

Final run c6f11506577d47dc87eddb2fc4391644 · mean with observed min–max

## 11. Findings need boundaries

- BST sorted / random means: 26.47×
- Repeated keys reduce effective fixture size
- Tracked operation allocation ≠ total RAM
- One machine, five repeats, selected workloads

Evidence image: `results/figures/allocations.png`

Python Software Foundation, tracemalloc; final measured summaries; prebuilt fixtures excluded

## 12. Learning outcomes and release

- Contracts connect algorithms, UI, tests, and evidence
- 195 automated tests + real browser walkthrough
- Report: 8 substantive pages; slides: 12
- Next: balanced tree, resizing hash, broader datasets

Source: AlgoNexis implementation and recorded measurements
