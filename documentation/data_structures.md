# Data structures and manager guide

Verified Day 2 scope, 2026-11-05: CustomSet, Stack, Queue, BinarySearchTree,
Graph, HashTable, and DataStructureManager. All implementations use only the
standard library. UI and performance measurement are planned for Day 3.

## Shared conventions

Constructors create independent state. `len(instance)` gives size and
`is_empty()` gives a bool. Manager routes use `size` instead of Python's `len`.
`display()` copies the container for inspection; it does not deep-copy arbitrary
payload objects. Editing a returned list/dict cannot edit structure membership,
links, or buckets. Arbitrary mutable payloads remain shared references.

Hashable set members, graph vertices, and table keys use Python hash/equality
rules, including `1 == True`. Their hash/equality must remain stable while stored.
Unhashable keys/members raise `TypeError`. BST values are integers excluding bool.
Stack/Queue and table values accept arbitrary payloads, including `None`.

| Structure | Storage and inspection order | Operations and results |
|---|---|---|
| `CustomSet(values=())` | Dict-backed unique members; insertion-ordered display | `add(value) -> bool`; `remove(value) -> None`; `discard(value) -> bool`; `contains(value) -> bool`; four new-set operations |
| `Stack(values=())` | List; display bottom-to-top | `push(value) -> None`; `pop() -> value`; `peek() -> value` |
| `Queue(values=())` | `collections.deque`; display front-to-rear | `enqueue(value) -> None`; `dequeue() -> value`; `front() -> value` |
| `BinarySearchTree(values=())` | Ordinary unbalanced nodes; display is inorder | `insert(value) -> bool`; `search(value) -> bool`; `inorder()`, `preorder()`, `postorder() -> list[int]` |
| `Graph()` | Undirected/unweighted adjacency dicts, vertex/neighbor insertion order | `add_vertex(vertex) -> bool`; `add_edge(source, target) -> bool`; `bfs(start)`, `dfs(start)`, `vertices() -> list` |
| `HashTable(capacity=8)` | Fixed array of separate-chaining bucket lists; bucket/chain display order | `insert(key, value) -> bool`; `find(key) -> value`; `delete(key) -> value`; `contains(key) -> bool`; `buckets() -> list[list[tuple]]` |

## CustomSet: queries, derived operations, and mutations

Uniqueness is enforced by the dict storage. Required algebra is implemented with
explicit loops and membership checks, without delegating to built-in set algebra.
`add`/`discard` report whether membership changed. Missing `remove` raises
`KeyError`; missing `discard` returns False. Membership, size, equality, and display
are read-only queries. Equality between CustomSets ignores insertion order.

`union(other)`, `intersection(other)`, `difference(other)`, and
`symmetric_difference(other)` require another CustomSet and return a new CustomSet.
They preserve both operands, including when operands are identical or empty.
Intersection/difference retain left order; union appends new right members;
symmetric difference retains left-only then right-only members.

These queries/derived operations are the read-only or static behavior discussed
in the plan; add/remove/discard are dynamic mutations. A derived result can later
be changed independently of its operands.

```python
from data_structures.custom_set import CustomSet

left, right = CustomSet([3, 1, 3]), CustomSet([1, 2])
assert left.union(right).display() == [3, 1, 2]
assert left.intersection(right).display() == [1]
assert left.difference(right).display() == [3]
assert left.symmetric_difference(right).display() == [3, 2]
assert left.display() == [3, 1] and right.display() == [1, 2]
assert left == CustomSet([1, 3])
```

## Edge conditions and representations

- **Stack/Queue:** empty pop/peek/dequeue/front raise `IndexError`. Constructor
  iterables are copied. Queue uses popleft, never repeated list front deletion.
- **BST:** duplicate insert returns False and leaves size unchanged. Invalid value
  types raise `TypeError`. Empty traversals return empty lists; missing search is
  False. Insertion/search and all traversals are iterative, including skewed trees.
  No balancing or deletion is promised.
- **Graph:** edges create missing endpoints after both endpoints are validated.
  Duplicate edges are idempotent (False); a new edge returns True. Self-loops are
  allowed once. Traversals visit the start's component only; an unknown start
  raises `KeyError`. Deterministic neighbor insertion order works with mixed
  hashable types without sorting. DFS retains neighbor iterators to match recursive
  preorder without relying on recursion depth. Display is a detached adjacency
  mapping with copied neighbor lists.
- **Hash table:** capacity is a positive integer excluding bool (`ValueError` for
  nonpositive values, `TypeError` for bad types). No resizing is performed. Python
  hash modulo capacity chooses a bucket; linear chain search compares identity
  or equality. Updating a key returns False and preserves size; new insertion
  returns True. Missing find/delete raises `KeyError`, keeping a stored `None`
  distinct from absence. Read-only properties expose capacity and load factor.

## Complexity and space tradeoffs

Hash-based averages assume O(1) hash/equality and distributed hashes. Let n/m be
operand sizes, h tree height, c table capacity, and Vr/Er the reachable graph size.
Inspection/output allocation is included where stated; these are theoretical
expectations, not measured benchmark results.

| Structure | Time | Storage / workspace |
|---|---|---|
| CustomSet | Expected add/remove/membership O(1), worst O(n); union/symmetric difference expected O(n+m); intersection/difference expected O(n); equality expected O(n) | O(n) storage; derived output O(result size); display O(n) time/space |
| Stack | Push/pop amortized O(1), peek/size/empty O(1) | O(n) storage; display O(n) time/space |
| Queue | Enqueue/dequeue/front/size/empty O(1) | O(n) storage; display O(n) time/space |
| BST | Insert/search O(h): O(log n) for balanced shape, O(n) when skewed; building a sorted tree can take O(n squared); traversals O(n) | O(n) nodes; O(h) traversal workspace plus O(n) output |
| Graph | Expected vertex/edge insertion O(1); BFS/DFS O(Vr+Er); full display O(V+E) | O(V+E) storage; traversals O(Vr) workspace plus output |
| Hash table | Expected insert/find/delete O(1+n/c), worst O(n); display/bucket snapshots O(c+n) | O(c+n) storage; snapshots O(c+n); size/load/capacity O(1) |

Because table capacity is fixed, operations are not unconditionally constant-time
as n grows. Separate chaining preserves correctness at high load, but longer
chains cost more. Likewise, an unbalanced tree offers no logarithmic guarantee.

## Unified manager for Day 3

`DataStructureManager(hash_capacity=8)` owns one instance per canonical name:
`set`, `stack`, `queue`, `tree`, `graph`, `hash_table`. `available_operations()`
returns copied name/operation lists. Dispatch uses a fixed allowlist of bound
methods and controlled adapters, with no eval or arbitrary attribute lookup.

`execute(structure, operation, **kwargs)` requires the parameter names in the table
above. All structures additionally expose `display`, `size`, `is_empty` without
arguments. Set algebra takes `values=<iterable>` and returns a plain list, preserving
the stored set. Hash-table routes also include `capacity`, `load_factor`, `buckets`.
Unknown structure/operation names raise `ValueError`; nonstring names and invalid
arguments raise `TypeError`. Domain exceptions preserve their documented types.

```python
from data_structures.manager import DataStructureManager

manager = DataStructureManager(hash_capacity=1)
manager.execute("stack", "push", value=5)
assert manager.execute("stack", "peek") == 5
assert manager.execute("stack", "pop") == 5
manager.execute("set", "add", value=1)
assert manager.execute("set", "union", values=[2]) == [1, 2]
assert manager.execute("set", "display") == [1]
manager.execute("graph", "add_edge", source="a", target="b")
assert manager.execute("graph", "dfs", start="a") == ["a", "b"]
manager.execute("hash_table", "insert", key="a", value=None)
assert manager.execute("hash_table", "find", key="a") is None
```

Use one manager in session state; a new manager resets all six structures. Returned
containers are plain Python values. The Day 3 integer-oriented UI must validate
its inputs and format arbitrary payloads if it chooses to expose them.

## Reviewed prior-course adaptations

The Day 1 inventory was reviewed on 2026-11-05. Paths are relative to AlgoNexis;
these prior student coursework projects are attribution sources, not runtime
dependencies. Their source files remain unchanged. AlgoNexis has its own tests.

| Structure | Reviewed source | Adaptation decision |
|---|---|---|
| Stack | `../../Module 4/LinearDS-Suite/datastructure_src/stack/stack.py` | Adapt list-backed LIFO and explicit empty checks to snake_case and detached display |
| Queue | `../../Module 4/LinearDS-Suite/datastructure_src/queue/queue.py` | Retain FIFO contract; replace list.pop(0) with deque.popleft |
| BST | `../../Module 6/treemap/src/treemap/core/bst.py` and `traversals.py` | Adapt iterative insertion/search/traversals from key/value nodes to integer-only nodes; ignore duplicates |
| Graph | `../../Module 7/VertexTrace/graph/adjacency_list.py` and `algorithms/traversal.py` | Adapt undirected adjacency, enqueue-time discovery, and iterator-stack DFS; remove weights/trace objects; use insertion order, auto endpoints, and idempotent/self-loop edges |
| Hash table | `../../Module 5 Critical Thinking/heaphash-nexus/src/data_structures/hash_table/hash_table.py`, `operations/insert.py`, `helpers/hash_function.py` | Adapt fixed separate-chaining buckets; generalize integer keys to hashables; use explicit missing-key exceptions instead of an ambiguous None result |
| CustomSet | No dedicated candidate found in the Day 1 inventory | New implementation of membership and required algebra |
