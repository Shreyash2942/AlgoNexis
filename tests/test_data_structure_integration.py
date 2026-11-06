"""Complete manager-route coverage and standard-library-only Day 2 integration."""

from collections import deque
from random import Random
import subprocess
import sys

from data_structures.graph import Graph
from data_structures.manager import DataStructureManager


def test_every_registered_operation_has_an_exercised_integration_route():
    manager = DataStructureManager(hash_capacity=1)
    covered: dict[str, set[str]] = {}

    def call(structure, operation, **kwargs):
        covered.setdefault(structure, set()).add(operation)
        return manager.execute(structure, operation, **kwargs)

    for structure in manager.available_operations():
        assert call(structure, "is_empty") is True
        assert call(structure, "size") == 0
        assert call(structure, "display") == ({} if structure == "graph" else [])

    assert call("set", "add", value=1) is True
    assert call("set", "add", value=2) is True
    assert call("set", "contains", value=1) is True
    assert call("set", "union", values=[2, 3]) == [1, 2, 3]
    assert call("set", "intersection", values=[2, 3]) == [2]
    assert call("set", "difference", values=[2, 3]) == [1]
    assert call("set", "symmetric_difference", values=[2, 3]) == [1, 3]
    assert call("set", "display") == [1, 2]
    assert call("set", "discard", value=2) is True
    assert call("set", "remove", value=1) is None
    assert call("set", "is_empty") is True

    assert call("stack", "push", value=7) is None
    assert call("stack", "peek") == call("stack", "pop") == 7
    assert call("queue", "enqueue", value=7) is None
    assert call("queue", "front") == call("queue", "dequeue") == 7

    for value in [2, 1, 3]:
        call("tree", "insert", value=value)
    assert call("tree", "search", value=3) is True
    assert call("tree", "inorder") == [1, 2, 3]
    assert call("tree", "preorder") == [2, 1, 3]
    assert call("tree", "postorder") == [1, 3, 2]

    assert call("graph", "add_vertex", vertex="isolated") is True
    assert call("graph", "add_edge", source="a", target="b") is True
    assert call("graph", "vertices") == ["isolated", "a", "b"]
    assert call("graph", "bfs", start="a") == call("graph", "dfs", start="a") == ["a", "b"]

    assert call("hash_table", "capacity") == 1
    assert call("hash_table", "insert", key=1, value="a") is True
    assert call("hash_table", "insert", key=2, value="b") is True
    assert call("hash_table", "find", key=2) == "b"
    assert call("hash_table", "contains", key=1) is True
    assert call("hash_table", "load_factor") == 2.0
    assert call("hash_table", "buckets") == [[(1, "a"), (2, "b")]]
    assert call("hash_table", "delete", key=1) == "a"
    assert call("hash_table", "find", key=2) == "b"

    for name, operations in manager.available_operations().items():
        assert covered[name] == set(operations), f"unexercised routes for {name}"


def test_common_size_routes_bind_to_each_independent_structure():
    manager = DataStructureManager()
    manager.execute("set", "add", value=10)
    for value in [10, 20]:
        manager.execute("stack", "push", value=value)
    for value in [10, 20, 30]:
        manager.execute("queue", "enqueue", value=value)
    assert [manager.execute(name, "size") for name in manager.available_operations()] == [1, 2, 3, 0, 0, 0]


def test_seeded_graph_traversals_match_independent_small_reference():
    rng = Random(506)
    for _ in range(30):
        graph, adjacency = Graph(), {vertex: [] for vertex in range(8)}
        for vertex in adjacency:
            graph.add_vertex(vertex)
        for _ in range(18):
            source, target = rng.randrange(8), rng.randrange(8)
            graph.add_edge(source, target)
            if target not in adjacency[source]:
                adjacency[source].append(target)
            if source not in adjacency[target]:
                adjacency[target].append(source)
        for start in adjacency:
            dfs_order, seen = [], set()

            def visit(vertex):
                seen.add(vertex)
                dfs_order.append(vertex)
                for neighbor in adjacency[vertex]:
                    if neighbor not in seen:
                        visit(neighbor)

            visit(start)
            queue, distances = deque([start]), {start: 0}
            while queue:
                vertex = queue.popleft()
                for neighbor in adjacency[vertex]:
                    if neighbor not in distances:
                        distances[neighbor] = distances[vertex] + 1
                        queue.append(neighbor)
            actual_bfs = graph.bfs(start)
            assert set(actual_bfs) == set(dfs_order) == set(distances)
            assert len(actual_bfs) == len(set(actual_bfs))
            assert [distances[v] for v in actual_bfs] == sorted(distances.values())
            assert graph.dfs(start) == dfs_order


def test_day1_and_all_day2_structures_run_without_installed_site_packages():
    script = (
        "import sys; from algorithms.bubble_sort import bubble_sort; "
        "from algorithms.quickselect import quickselect; "
        "from visualization.sorting_visualizer import SortingVisualizer; "
        "from data_structures.manager import DataStructureManager; "
        "m=DataStructureManager(); assert len(m.available_operations()) == 6; "
        "assert m.execute('set','add',value=1); "
        "assert m.execute('set','union',values=[2]) == [1,2]; "
        "assert list(SortingVisualizer(bubble_sort([2,1])))[-1].values == (1,2); "
        "assert quickselect([2,1],1) == 1; assert 'streamlit' not in sys.modules"
    )
    subprocess.run([sys.executable, "-S", "-c", script], check=True, capture_output=True)
