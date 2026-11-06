# Day 2 verification and gate G2

Verification date: 2026-11-05. Scope: D2.1-D2.7, with Day 1 regression.

## Actual results

`python -m pytest tests/ -v` completed with **143 passed in 0.66s** on
CPython 3.14.4 / pytest 9.2.0. This includes all 71 Day 1 cases and 72 new
Day 2 cases. Syntax compilation, Python 3.11 grammar parsing, both examples in
the operations guide, and `python -m pip check` also passed. Core integration
runs under `python -S`, without installed Streamlit or other site packages.

| Work package | Verified evidence |
|---|---|
| D2.1 | CustomSet algebra matches reference results across 256 subset pairs per operation; operands remain unchanged; uniqueness, equality, errors, and inspection tested |
| D2.2 | LIFO/FIFO order, consistent IndexError on empty operations, copied input/display, and seeded mixed workloads |
| D2.3 | Known BST traversals, duplicate policy, random insertion oracle, 1,200-node skewed trees; graph cycles, disconnection, insertion order, 1,501-vertex path, and seeded reference comparisons |
| D2.4 | Deliberately colliding keys, independent updates/deletion, None values, invalid keys/capacity, detached buckets, and seeded dict-model workload |
| D2.5 | All six structures persist through the fixed registry; unsupported/private names and wrong keywords fail; metadata/results do not expose internal containers |
| D2.6 | Every one of the 49 registered operation routes is invoked and asserted; size routes bind to distinct instances; full prior tests pass |
| D2.7 | Operations/examples, complexity assumptions, capacity/duplicate/traversal policies, shallow inspection behavior, architecture, and reviewed coursework attribution documented |

CustomSet, Stack/Queue, BST/Graph, HashTable, and initial manager checks passed
before their feature commits. Full manager integration and graph reference tests
were added in the final verification work package. No line-coverage percentage
or runtime/memory benchmark claim is inferred from these tests.

## Decisions and adaptations

The reviewed Module 4 stack/queue patterns were adapted, with deque replacing
the prior queue's front deletion. Module 6 iterative BST patterns now store unique
integers. Module 7 adjacency/traversal patterns are unweighted and independent
of trace/UI objects. Module 5 separate-chaining patterns now accept hashable keys
and explicit missing-key errors. CustomSet is new. Prior project files were not
modified, and no external source directory is imported at runtime.

Known design limits are deliberate: the BST is unbalanced; hash-table capacity is
fixed, so its average operation cost depends on load; and inspection copies
containers rather than arbitrary payload objects. These are documented contracts,
not unresolved critical defects. UI workload validation is Day 3 work.

## Actual commit history and gate

1. `8af9511` - `feat: implement custom set operations`
2. `829c240` - `feat: add stack and queue implementations`
3. `9d9f6c5` - `feat: implement binary search tree and graph`
4. `2aa90f1` - `feat: add hash table with collision handling`
5. `6bab65c` - `feat: integrate data structures through unified manager`

The sixth Day 2 commit contains the final integration tests, documentation,
progress updates, and refreshed graph:
`test: verify data structures and document operations`. Its hash is read after
creation; inspect `git log --oneline f2409c4..HEAD` for all six commits.

**G2: passed.** Required structure operations and manager dispatch meet the
automated checks and are ready for Day 3 integration. Existing local edits to the
implementation plan were preserved; only its Day 2 checklist/status was updated.
Git status and the remote branch are checked after the final commit/push.

Next work package: **D3.1 - Streamlit shell**. G3/G4 remain unverified. No app,
application performance CSV, report PDF, presentation, or release tag is claimed.
