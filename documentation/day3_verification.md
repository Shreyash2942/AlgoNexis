# Day 3 verification and gate G3

Verification date: 2026-11-06 (America/New_York). Measurement timestamps are actual
UTC timestamps and may fall on the following UTC date. Scope: D3.1-D3.7 only.

## Actual test and browser evidence

The final full regression completed with **191 passed in 4.65s** on CPython 3.14.4
and pytest 9.2.0: all 143 Day 1-2 tests plus 48 Day 3 tests. No test failures remain.
The suite includes real Streamlit AppTest execution, not only mocked UI calls.
Compilation, Python 3.11 grammar parsing, dependency checks, and CSV/source-hash
consistency checks also passed. Installed runtime packages declare Python 3.11+
support; this session executed on 3.14.4, not every supported Python version.

A fresh Streamlit process responded successfully at `/_stcore/health`. A real
headless Microsoft Edge walkthrough exercised navigation, both algorithms, every
step of a known sort, invalid integer input, all six structure panels, reset,
performance charts, a complete default benchmark run, and the CSV download.
Downloaded CSV text matched the saved file. A subsequent walkthrough preserved
the measurements while capturing focused screenshots. Browser checks and screenshot
inspection are separate from the 191 pytest cases; no manual human walkthrough
is claimed.

| Work package | Acceptance evidence |
|---|---|
| D3.1 | Four sections render; AppTest object-identity spike proves manager persistence; HTTP health and fresh Edge launch pass |
| D3.2 | Strict integer samples/text parsing; real results/counts; empty/invalid input and k errors; dataset/rank invalidation |
| D3.3 | Every compare/swap plus boundaries retained; Previous/Next/Reset/slider; final state correctness; navigation persistence; trace cap of 50 |
| D3.4 | All structures routed through manager; all set binary operations; mutations/inspection; missing/empty errors; atomic growth guard; reset |
| D3.5 | Seeded inputs/pivots; fresh fixtures; checked warm-ups and every trial; independent timing/allocation rows; guarded large cases |
| D3.6 | Actual repeat summaries, separate units, explicit operation labels, counts only for Bubble Sort, skipped-case reasons, full CSV download |
| D3.7 | 191 tests, fresh browser walkthrough, real CSV/environment evidence, authentic screenshots, user guide and limitations |

## Measured artifacts

`results/benchmark_results.csv` has **1,080 measured observations and eight skipped
cases** (1,088 rows excluding the header). There are 116 requested cases, 108
eligible cases, five timing and five allocation trials per eligible case, and
216 repeat-summary groups. Every measured result passed its operation-specific
correctness check. The eight guarded cases are Bubble Sort/BST at size 5,000,
across four integer patterns; their numeric cells are blank, not zero.

The matching environment JSON identifies the same run ID and records config,
Python/OS/processor, package versions, revision, and core source hashes. The
recorded core hashes were checked against current files. The final UI-generated
run identifies feature commit `f7b0feb`; later documentation/browser-capture edits
do not alter the measured core. Source digests provide the precise contents.

Raw rows, the download, and dashboard summaries use the same data. The methodology
documents operation/setup boundaries, input versus unique fixture sizes, hash
capacity profile, timing variation, tracemalloc limitations, and different-purpose
workloads. These are real observations, not a completed Day 4 analysis report.

## Authentic screenshots

- `screenshots/dashboard.png` and `dashboard-mobile.png`: navigation/overview and
  the responsive mobile layout.
- `screenshots/algorithms.png`: actual sorting/selection results.
- `screenshots/sorting-steps.png`: active swap highlights and recorded counters.
- `screenshots/structures.png`: live structure contents and collision buckets.
- `screenshots/performance-overview.png` and `performance.png`: saved-run metadata,
  measured curves, and repeat summaries.

These are browser captures, not generated illustrations. The verified local
development servers are stopped during teardown; launch instructions are in the
user guide. Development-server module caching was resolved by restarting before
final checks. The final browser checks used freshly launched source.

## Commits and gate decision

1. `dccfa09` - `feat: build Streamlit dashboard and navigation`
2. `4879625` - `feat: integrate bubble sort and quickselect interfaces`
3. `2eca1b0` - `feat: add interactive bubble sort visualization`
4. `873c925` - `feat: build interactive data structure controls`
5. `94a17ca` - `perf: implement execution time and memory benchmarking`
6. `f7b0feb` - `feat: add performance charts and benchmark dashboard`

The seventh commit contains the final UI/browser integration checks, captured
evidence, documentation/progress updates, and refreshed graph:
`test: validate UI integration and performance tools`. Read its resulting hash
from `git log --oneline 7fa29e5..HEAD`; no self-referential hash is embedded here.

**G3: passed.** The complete local portfolio and verified measurement evidence are
ready for Day 4. No critical workflow failure remains in the executed checks.
Known limits are documented: local session-only structure state, explicit UI/work
caps, an unbalanced BST, different UI/benchmark hash capacity profiles, and
incremental process-wide Python allocation tracing rather than total RAM.

The implementation plan was updated within Day 3 only. G4 remains unverified.
Next work package: **D4.1 - Final regression and integration QA**, followed by final
measurements, the five-page report, presentation, documentation, and release work.
