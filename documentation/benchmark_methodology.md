# Benchmark methodology — final Day 4 evidence

The framework calls core APIs directly; Streamlit rendering is outside every
measurement. These are operation microbenchmarks, not end-to-end application
latency or whole-structure memory footprints.

## Reproduce a run

```powershell
& .\.venv\Scripts\python.exe -m performance.benchmark --trials 5 --seed 506
```

Defaults are sizes 10, 100, 1,000, and 5,000; random, sorted, reverse, and
duplicate-heavy integer lists; and five timing plus five allocation trials per
eligible case. A checked, unrecorded warm-up precedes each case. Results are
written to `results/benchmark_results.csv` and the matching
`results/benchmark_results.environment.json`.

Every dataset is generated outside measurement with `Random(seed)`. Sorted and
reverse patterns reorder the same seeded random list. Duplicates draw from -3
through 3. Quickselect measures rank `(n+1)//2`, including duplicate positions;
its pivot seed is `seed + trial`, shared by the corresponding timing/allocation
pair and recorded explicitly. Repeating seeds repeats inputs/pivots, not wall time.

## Workloads and setup boundaries

| Implementation | Operation | Prebuilt fixture / expected result |
|---|---|---|
| Bubble Sort | Complete sort with tracing disabled | Input list; sorted reference computed beforehand |
| Quickselect | Select middle one-based rank | Input list and seeded generator; reference computed beforehand |
| CustomSet | Membership probe for every input value | Unique members; all probes must succeed |
| Stack | Pop every item | Preloaded stack; returned order must reverse the input |
| Queue | Dequeue every item | Preloaded queue; returned order must equal the input |
| BST | Search every input value | Prebuilt unique-integer unbalanced tree; every search must succeed |
| Graph | One BFS over an n-vertex path | Prebuilt undirected path; traversal must equal 0 through n-1 |
| HashTable | Find every input key | Prebuilt table; each stored value equals its key |

Except for graph paths, structure probes use the chosen integer pattern.
`input_size` is the input/probe count; `fixture_items` records actual stored size
where duplicates reduce uniqueness. Hash-table capacity is `max(8, 2*n)` in this
profile and is recorded in each row; this is a low-load profile, not the UI's
default-capacity-8 profile. Graph paths run once per size, with pattern `path`.

Fixture construction, input generation, correctness checks, environment capture,
CSV serialization, and charts are excluded from measurement. Building result
lists inside a measured operation is included. Algorithm input-copy work is also
included, as it is part of their public API. A fresh fixture is used for every
timing trial, every allocation trial, and warm-up; destructive pop/dequeue cases
therefore begin with equivalent state.

## Time, allocation, and correctness

Timing uses `perf_counter_ns()` and reports milliseconds. Allocation trials use
`tracemalloc` separately and report **peak Python-tracked bytes allocated during
the operation**, including returned outputs. Prebuilt datasets/fixtures are not
traced. This metric is neither whole-process RAM nor total structure storage.
Tracing is process-wide, so unrelated threads may contribute; avoid concurrent
activity when drawing conclusions. Existing tracing is rejected without resetting
someone else's instrumentation. The framework serializes its measurement calls.

The expected answer and post-operation state are checked after every trial, not
only warm-up. A failure raises an error and prevents that run from being returned
or saved. No fabricated observations replace failed operations.

Bubble Sort and BST cases above 1,000 inputs are deliberately guarded because
quadratic work can dominate interactive runs. A skipped row records trial 0,
status/measurement `skipped`, and its reason, with blank measurement fields.
Skipped rows are excluded from chart summaries rather than plotted as zero.

## Evidence and interpretation

Each row records run ID, UTC timestamp, implementation/operation, input size and
pattern, trial and measurement kind, actual value, dataset/pivot seeds, rank,
Bubble Sort counts when exposed, fixture size/capacity, Python/OS/processor,
Git revision, and a digest of core source contents. The environment JSON includes
package versions, per-file SHA-256 values, config, and observed/skipped counts.
It must be matched to CSV by run ID. CSV cells for the other measurement kind
remain blank; timing/allocation trials are not paired as one simultaneous sample.

Tables/charts summarize repeats by run, implementation, operation, size, pattern,
and measurement. Mean, median, minimum, and maximum describe observed variation;
min/max are not confidence intervals. Filtering changes only the displayed subset;
the download contains the full run. The machine observations may vary with Python,
processor, system load, and instrumentation overhead, especially for tiny cases.

Bubble Sort sorts a complete list; Quickselect selects one rank. Structure
workloads also differ in purpose and setup. Compare scaling and method tradeoffs,
not raw timings as proof that one different-purpose operation replaces another.
Day 4 analysis must use these real observations and their limits.
# Day 4 final evidence and controlled supplement

The final default run is `c6f11506577d47dc87eddb2fc4391644`, measured with
Python 3.14.4 and pandas 3.0.6 at source revision `388fbf8`. It contains 1,080
observations (540 timing and 540 allocation rows), eight guard skips, and 216
separate summary groups. The 60-row supplemental hash run contributes another
12 groups, for 228 groups in `results/summary_statistics.csv`.

`python -m scripts.measure_hash_collisions` measures unique keys `range(n)` at
n=10,100,1000, with capacity 1 versus 2n, five timing and five separate memory
trials, fresh prebuilt fixtures, a warm-up, and exact result checks. Capacity 1
forces collisions; the particular integer keys occupy separate buckets at 2n.
This controlled supplement is distinct from the default random/duplicate input
profile. Neither profile measures fixture construction or automatic resizing.

`python -m scripts.analyze_results` validates coverage/provenance and produces
mean, median, minimum, maximum, trial counts, CSV/JSON summaries, and five PNG/SVG
figures. Whiskers are observed min–max, not confidence intervals; logarithmic
axes are labeled. The manifest hashes raw CSVs, environment sidecars, summaries,
hardware details, and figures. `python -m scripts.validate_release --analysis`
checks saved evidence hashes and summary totals without document-building packages.

To reproduce a new study, rerun the two measurement commands, then analysis.
Finished reports/slides are edited directly; update their values and figures
when replacing the underlying CSV source. Optional plotting dependencies are in
`requirements-analysis.txt`. Measurements naturally vary across runs. Existing Day 3 verification
records are historical and identify their own prior run.
