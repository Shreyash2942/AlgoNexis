# Day 2 reuse inventory

Inventory date: 2026-11-04. Existing coursework was located under the parent
CSC506 course directory. Paths below are relative to the AlgoNexis repository.
These are candidates for review, not imported or verified AlgoNexis components.
No existing coursework was modified during Day 1.

| Structure | Candidate implementation | Associated tests | Day 2 review needed |
|---|---|---|---|
| Stack | `../../Module 4/LinearDS-Suite/datastructure_src/stack/stack.py` | `tests/test_stack.py` in that project | LIFO, empty errors, stateful API, attribution |
| Queue | `../../Module 4/LinearDS-Suite/datastructure_src/queue/queue.py` | `tests/test_queue.py` in that project | FIFO, representation, empty errors, attribution |
| BST | `../../Module 6/treemap/src/treemap/core/bst.py` and `traversals.py` | `tests/test_bst.py`, `tests/test_traversals.py` in that project | Unbalanced behavior, duplicate policy, required traversals |
| Graph | `../../Module 7/VertexTrace/graph/adjacency_list.py` and `algorithms/traversal.py` | `tests/test_list.py`, `tests/test_traversal.py` in that project | Undirected edges, deterministic BFS/DFS, invalid starts |
| Hash table | `../../Module 5 Critical Thinking/heaphash-nexus/src/data_structures/hash_table/hash_table.py` and its operations | `tests/unit/test_hash_table.py` in that project | Separate chaining, collision tests, missing keys, capacity |
| CustomSet | No dedicated set implementation located in this Python-file inventory | To be written in AlgoNexis | Implement required algebra in the custom class |

Additional simple stack/queue implementations exist in
`../../Critical Thinking - 1/datastruct-lab/src/structures/`. Day 2 must compare
candidate interfaces and tests before deciding what to adapt. Keep AlgoNexis
self-contained; do not import from paths outside this repository at runtime.
