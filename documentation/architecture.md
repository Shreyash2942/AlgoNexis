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
