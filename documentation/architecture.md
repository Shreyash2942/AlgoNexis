# AlgoNexis architecture and decisions

## Foundation

The root README and four-day implementation plan define the target system.
Days 1-4 deliver importable core algorithms, data structures, manager, Streamlit
views, verified operation measurements, and completed academic artifacts.

- Existing Git repository and `origin` are preserved; the default branch is `main`.
- GitHub repository: https://github.com/Shreyash2942/AlgoNexis (verified existing).
- Development Python: CPython 3.14.4 on Windows; source targets Python 3.11+.
- `.venv` isolates dependencies. `requirements.txt` lists direct dependencies;
  `requirements.lock.txt` records the tested environment after installation.
- Core modules must import without importing Streamlit or starting a UI.
- Reviewed prior-course adaptations and current structure contracts are recorded
  in `data_structures.md`. No external project is imported at runtime.

## Package boundaries

`algorithms` owns sorting and selection. `visualization` consumes immutable
sorting records. `data_structures` owns the six structures and their persistent
manager. `performance` measures core operations independently of Streamlit;
`ui` owns input parsing, session helpers, views, and chart rendering. `app.py`
selects four sections. `results` stores real CSV observations and environment
metadata. `scripts` supplies optional benchmark analysis, controlled hash measurements,
and evidence validation. Finished documents are edited directly in Word/PowerPoint.

```text
app.py -> ui views / session state
             |                      |
      algorithms                 manager -> six structures
             |                      |
      immutable steps               |
             |                      |
       visualization        performance benchmark (direct core calls)
                                    |
                        CSV + environment/source provenance
                                    |
                       summaries + PNG/SVG figures
                                    |
                      report PDF + presentation PPTX
```

## Release evidence decisions (Day 4)

- The runtime stays limited to Streamlit, pandas, Altair, pytest and their
  dependencies. Optional `requirements-analysis.txt` adds only Matplotlib for
  regenerating standalone benchmark plots. Document-building dependencies have
  been removed with the one-time generators.
- pandas 3.0.6 is the tested maintenance version after a new 3.1.1 Windows wheel
  was blocked by local Application Control. No system policy was changed.
- `scripts.validate_release` verifies configured trial coverage, provenance,
  unchanged measured sources, the controlled hash profile, saved figure hashes,
  and summary-group totals using the standard library. `.gitattributes` keeps source LF and preserves
  generated evidence bytes across platforms so checkout conversion cannot break
  provenance hashes or the exact CSV download contract.
- The report was generated from measured summaries. Its editable DOCX and the
  presentation PPTX are now maintained directly; one-time builders and templates
  have been removed. The presentation uses the same values, authentic browser
  screenshots, and charts. Its editable outline and speaker notes accompany the
  PPTX. Microsoft PowerPoint opened and rendered the deck for visual inspection.
- The supplementary hash profile deliberately varies capacity using fixed unique
  keys; it remains separate from the default random/duplicate profile. Neither
  experiment measures prebuilt-fixture storage or construction.

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

## Unified manager (D2.5)

`DataStructureManager(hash_capacity=8)` owns six persistent instances under
`set`, `stack`, `queue`, `tree`, `graph`, and `hash_table`. Its fixed bound-method
registry is the only dispatch authority; there is no eval or arbitrary attribute
lookup. `execute(structure, operation, **kwargs)` binds keyword arguments before
execution and returns plain values/lists/dicts. Derived-set results become lists
without replacing the stored set. `available_operations()` returns detached
metadata for UI controls. All structures expose manager routes for `display`,
`size`, and `is_empty`, alongside their required domain operations.

Unknown names raise `ValueError`; nonstring names or invalid keyword arguments
raise `TypeError`. Domain exceptions retain their type for readable UI handling.
Separate managers own separate instances. Inspection snapshots copy containers,
not arbitrary payload objects. Day 3 should keep one manager in session state;
constructing a new manager provides a full reset without leaking prior state.

Day 2 gate evidence is in `day2_verification.md`. Tests exercise all registered
routes and preserve Day 1 behavior; no Streamlit app or benchmark output is
claimed at G2. UI code should translate documented domain errors to user messages,
keep manager lifetime in session state, and apply workload limits before calling
the structures. No UI dependency is introduced into core packages.

## Streamlit session and rendering contracts (Day 3)

One manager lives in session state. `ui.state` initializes absent fields only,
invalidates algorithm results on dataset change, resets playback for a new sort,
and replaces all six structures on reset. Widget keys are separate from persistent
dataset/rank/playback model values so widget cleanup on navigation does not erase
the model. Quickselect rank changes invalidate only its result. Tests exercise
navigation, resets, samples, invalid input, and independent state.

`ui.inputs` accepts comma/whitespace-separated ASCII integers, with no eval,
bracket expressions, floats, or partial coercion. UI limits are 100,000 text
characters, values within +/- 1e9, 5,000 selection values, 1,000 untraced sort
values, 50 traced sort values, and 200 items per interactive structure. Growth
checks run before mutations and allow existing-key updates at capacity.

`ui.sorting_view` consumes immutable frames unchanged. Previous/Next/Reset/slider
update a persistent zero-based index; initial/final events, highlights, current
counts, and ordered bars come from the recorded trace. Boundary buttons disable
appropriately; no events are truncated. Native Streamlit controls and a consistent
teal/light theme provide keyboard labels and responsive layout.

## Measurement and evidence contracts (Day 3)

`performance.metrics` separates perf_counter_ns timing from tracemalloc peak
allocation trials. `performance.benchmark` creates fresh fixtures/seeded inputs
outside measurement, checks each result, and returns a complete run before saving.
Core files are hashed; revision, environment, config, and seeds are recorded.
Bubble Sort/BST cases above 1,000 are explicit skips with blank metric cells.

`performance.summary` groups observed repeats by run, workload, size, pattern,
measurement kind, and hash capacity. Skips are excluded. Charts use these same
rows; units are separated, and the full-run CSV download matches the saved data.
The allocation metric excludes prebuilt fixtures, includes operation outputs,
and is not whole-process RAM. Hash-table measurement uses a recorded low-load
capacity profile; UI exploration remains fixed at 8. See `benchmark_methodology.md`
for operation definitions, seed policy, and limits.

G3 evidence is in `day3_verification.md`. Real Edge/browser and Streamlit AppTest
checks exercise the app; screenshots are authentic. The app remains local, while
repository commits and measured artifacts are pushed to the existing GitHub repo.
