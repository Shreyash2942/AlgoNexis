# AlgoNexis architecture and decisions

## Foundation

The root README and four-day implementation plan define the target system.
Day 1 establishes importable Python packages and core algorithms. Data structures,
Streamlit views, measurements, and academic deliverables belong to later days.

- Existing Git repository and `origin` are preserved; the default branch is `main`.
- GitHub repository: https://github.com/Shreyash2942/AlgoNexis (verified existing).
- Development Python: CPython 3.14.4 on Windows; source targets Python 3.11+.
- `.venv` isolates dependencies. `requirements.txt` lists direct dependencies;
  `requirements.lock.txt` records the tested environment after installation.
- Core modules must import without importing Streamlit or starting a UI.
- Prior-course reuse candidates are recorded in `data_structures.md` and require
  a separate correctness/interface review during Day 2.

## Package boundaries

`algorithms` owns sorting and selection. `visualization` consumes immutable
sorting records. `data_structures` is reserved for Day 2; `performance` for Day 3.
`results` will hold actual benchmark output once measurements are implemented.
No placeholder benchmark CSV, UI, report PDF, or presentation is created on Day 1.

## Bubble Sort contract (D1.2)

`bubble_sort(values: list[int], *, track_steps: bool = True) -> BubbleSortResult`
validates integers (booleans excluded), copies input, compares adjacent elements,
and exits after a pass without swaps. Bad types raise `TypeError`.

The frozen result contains `sorted_values: tuple[int, ...]`, `comparisons`,
`swaps`, and `steps: tuple[SortingStep, ...]`. Each frozen step contains `event`,
`values`, `compared_indices`, and cumulative counters. Events are `initial`,
`compare` (before any exchange, comparison already counted), `swap` (after the
exchange, swap already counted), and `final`. Initial/final events use `None`
indices and exist even for empty/singleton input. Every actual event is retained;
`len(steps) == comparisons + swaps + 2` when tracing is enabled.

The copying, trace-disabled API uses O(n) auxiliary space and O(n) best,
O(n**2) average/worst time. Full snapshots add O(n) work/storage per event,
up to O(n**3) trace time/storage and O(n**2) even on sorted inputs. Later
benchmarks must explicitly use `track_steps=False`; UI limits must be applied
before sorting rather than dropping recorded events. Equal values are never
swapped. This preserves the stable adjacent-sort behavior.

## Visualization data contract (D1.3)

`SortingVisualizer(result)` accepts a traced `BubbleSortResult`. `total_steps`
includes both boundary states; `get_step(index)` uses zero-based nonnegative
indices and raises `IndexError` outside the trace (`TypeError` for noninteger
indices, including bool). Passing an untraced result raises `ValueError`.
Iteration yields every frame, with no internal playback cursor.

Frozen `SortingFrame` fields are `step_index`, `total_steps`, `event`, `values`,
`highlighted_indices`, `swapped`, `comparisons`, `swaps`, and `description`.
Highlights are the compared/exchanged pair, or an empty tuple for boundaries.
Snapshots are reused by reference, not copied. No UI package is imported.
Day 3 can keep a frame index in session state, retrieve previous/next frames,
and reset the index when the input/result changes. Bounded visualization must
be a caller input policy; the engine never truncates a complete trace.

## Quickselect contract (D1.4)

`quickselect(values: list[int], k: int, *, rng: random.Random | None = None)
-> int` copies integer input (booleans excluded). Ranks are one-based and count
duplicates. Empty input and out-of-range ranks raise `ValueError`; bad list,
element, rank, or generator types raise `TypeError`. Caller data is unchanged.

An iterative three-way partition groups values less than, equal to, and greater
than a uniformly selected pivot. It only continues in the partition containing
the target index; a rank within the equal block returns immediately. No sorting
function or recursion is used. Expected time is O(n), worst O(n**2), with O(n)
space for the input copy and O(1) partition workspace.

A supplied `Random(seed)` controls pivot choices; otherwise a fresh local
generator avoids modifying global random state. Later benchmarks should record
both input seed and pivot seed, recreate the pivot generator for repeatable
trials when desired, and record the measured rank. Reusing a generator advances
its state rather than repeating a pivot sequence. Timing and allocation trials
will be separate Day 3 measurements.

## Day 2 structure contracts

`CustomSet` stores hashable members in an insertion-ordered dict. Required algebra
uses explicit membership loops, never built-in set operators. `add`/`discard`
return whether membership changed; `remove` raises `KeyError` if missing.
Derived operations accept another `CustomSet`, return a fresh set, and preserve
both operands. Equality ignores insertion order; display preserves it. Python
hash/equality rules apply (including `1 == True`). Unhashable members raise
`TypeError`. `display()` returns a shallow, detached list; `len` reports size.

`Stack` uses a list; `Queue` uses `collections.deque`. Their end operations follow
LIFO/FIFO respectively; empty pop/peek/dequeue/front raise `IndexError`. Both
accept arbitrary payloads and copy constructor iterables into their own storage.
`display()` returns a shallow list, bottom-to-top for Stack and front-to-rear for
Queue. These adapt the reviewed Module 4 LinearDS-Suite patterns to snake_case,
with deque replacing the previous queue's O(n) front deletion.

`BinarySearchTree` accepts integers excluding bool, ignores duplicate insertions,
and returns bool from insert/search. Traversals and display return detached value
lists, not nodes. All algorithms are iterative. Insert/search cost O(h), worst
O(n); traversals use O(n) time, O(h) workspace plus output. Module 6 treemap's
iterative algorithms are adapted from key/value nodes to integer-only values.

`Graph` is undirected and unweighted. Hashable vertices and neighbors retain
insertion order, so mixed types require no sorting. `add_edge` validates both
endpoints before adding missing vertices; duplicates are idempotent and self-loops
are allowed once. BFS/DFS return reachable vertices only and raise `KeyError`
for an unknown start. Iterator-stack DFS matches recursive neighbor order without
recursion. The design adapts Module 7 VertexTrace, removing weights and trace/UI
dependencies. Display copies both adjacency and neighbor containers.

`HashTable(capacity=8)` uses custom bucket lists and separate chaining. Keys may be
any hashable value with stable hash/equality; values may include `None`. Insert
returns True for a new key and False for an update. Find/delete raise `KeyError`
if absent; delete returns the removed value. Identity/equality matches dictionary
key semantics. Positive integer capacity is fixed (no implicit resizing), so
expected operation cost is O(1 + n/capacity), worst O(n), not unconditional O(1).
Display and bucket inspection copy containers. This adapts Module 5's integer-key
bucket design to general hashable keys and explicit missing-key exceptions.
