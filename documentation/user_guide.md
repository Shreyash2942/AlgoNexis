# AlgoNexis user guide

## Start locally

Use Python 3.11+ (the verified environment is CPython 3.14.4 on Windows).
From the repository root:

```powershell
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the printed local URL, normally http://localhost:8501. PowerShell activation
is optional when using the environment executable directly. On macOS/Linux use
`.venv/bin/python` instead. `requirements.lock.txt` records the tested environment,
including optional browser-QA packages; `requirements-dev.txt` installs the latter.

The sidebar has Dashboard, Algorithms, Data Structures, and Performance Analysis.
A browser session retains exploration state and structure instances as you navigate.
A different browser session has independent state. Closing the session loses these
in-memory structures; the saved benchmark CSV remains on disk.

## Algorithms

Choose a sample and press **Load sample**, or enter comma-/whitespace-separated
integers. Decimals, code, brackets, missing comma entries, and out-of-range values
are rejected. Integer values are bounded to +/- 1 billion and text to 100,000
characters. Editing the dataset invalidates both prior results and the playback
index; changing rank invalidates only the selection result.

- **Bubble Sort:** Run with step recording enabled for up to 50 values. Original
  and sorted values, comparisons, and swaps come from the core result. Disable
  recording for execution-only inputs up to 1,000 values. Empty input is valid.
- **Quickselect:** Enter one-based rank k; duplicates count as separate positions.
  Selection supports up to 5,000 values and rejects empty input or k greater than
  the input size. The exploration pivot seed is 506. Caller data is preserved.

The stepper records initial state, every comparison, every actual swap, and final
state without dropping events. Use Previous, Next, Reset steps, or the slider.
The index is zero-based; the caption also shows current/total counts. Amber marks
compared indices and teal a completed swap. Event text supplies the same meaning
without relying only on color. Negative values extend below zero. Empty input
still has initial/final states, with no bars. Playback position survives navigation
and resets for a new dataset/run. With recording disabled, no trace is invented.

## Data structures

Choose one of six structures, an operation, and the requested arguments, then
press **Run operation**. All controls use the persistent manager. Contents and the
last successful operation are shown separately; a new error clears that result.

- **Custom Set:** Add/remove/discard integer members, inspect membership, or supply
  another integer list for union/intersection/difference/symmetric difference.
  Derived results leave the stored set unchanged.
- **Stack:** Push, pop, peek, and inspect bottom-to-top contents (LIFO).
- **Queue:** Enqueue, dequeue, front, and inspect front-to-rear contents (FIFO).
- **BST:** Insert/search integers and choose inorder/preorder/postorder traversal.
  Duplicate inserts do not increase size. The tree is unbalanced.
- **Graph:** Add integer vertices or edges; an edge creates missing endpoints.
  The graph is undirected/unweighted, duplicate edges are idempotent, and self-loops
  are allowed. BFS/DFS use the starting component and neighbor insertion order.
- **Hash Table:** Use integer keys and text values. Insert updates an existing key;
  find/delete report missing keys clearly. Bucket inspection shows collisions.
  The UI capacity is fixed at 8.

Size, empty-state, and display operations are available for every structure. Empty
stack/queue removals or inspections and missing members/starts/keys produce readable
messages. **Reset all structures** replaces all six instances and clears the result.
Interactive structures are limited to 200 members/items/vertices; existing-key
updates still work at the limit. See `data_structures.md` for core APIs and their
more general payload/key support, complexity, and shallow inspection contracts.

## Performance Analysis

The page initially loads the saved CSV. Its run ID, timestamp, seed, observed-row
count, and guarded-case count identify the actual evidence being displayed.
Opening benchmark controls and changing them does not relabel the saved run.

To measure again, choose sizes (10/100/1,000/5,000), patterns, algorithms, whether
structures are included, a seed, and 5-10 trials per measurement kind. Press
**Run benchmarks**. The app creates fresh fixtures, checks every result, and saves
the completed run to `results/benchmark_results.csv` plus its environment JSON.
Invalid settings or failed correctness checks do not replace the previous run.

Timing and allocation trials are separate. Chart filters select an input pattern
and workloads; tables show mean/median and observed min/max from the same rows.
Graph BFS uses a path profile rather than the integer-list patterns. Guarded large
Bubble Sort/BST cases are listed with reasons and never plotted as zero.
Comparison/swap counts are shown only for Bubble Sort.

**Download full run CSV** exports the complete saved run, not only a chart-filtered
subset. The default recorded Day 3 run has 1,080 measured observations plus eight
skipped cases. CSV timing rows have blank allocation cells, and vice versa.

Peak Python-tracked allocation means allocations during the measured operation,
including outputs, excluding prebuilt datasets/fixtures. It is not total RAM or
whole-structure memory. The hash-table benchmark uses capacity max(8, 2*n), unlike
the fixed-capacity-8 exploration panel. Bubble Sort and Quickselect solve different
problems; structure operation batches also differ. Compare scaling and tradeoffs,
not different tasks as interchangeable substitutes. Tiny cases are sensitive to
measurement overhead and system load. Read `benchmark_methodology.md` before
using the numbers in the final report.

## Reproduce measurements and checks

```powershell
& .\.venv\Scripts\python.exe -m performance.benchmark --trials 5 --seed 506
& .\.venv\Scripts\python.exe -m pytest tests/ -v
```

The framework runs independently of the UI. Source hashes, Git revision, config,
package versions, Python/OS/processor, seeds, trial kinds, and operation definitions
make the run inspectable; timings are expected to vary across machines/runs.

Optional browser QA (install `requirements-dev.txt` and Microsoft Edge first):

```powershell
# Start the app in another terminal, then:
& .\.venv\Scripts\python.exe -m tests.browser_smoke --url http://127.0.0.1:8501
# Preserve the existing measurements while verifying controls/screenshots:
& .\.venv\Scripts\python.exe -m tests.browser_smoke --url http://127.0.0.1:8501 --skip-benchmark
```

The full walkthrough runs actual benchmarks and replaces the saved CSV. AppTest
checks in pytest use isolated temporary benchmark storage. Browser screenshots in
`screenshots/` are authentic app captures, including mobile layout and measured
charts. Restart a running development server after source edits if imported modules
remain cached. The finished app was verified from a fresh launch; no Site hosting
or external deployment is needed.
