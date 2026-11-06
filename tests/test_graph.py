"""Deterministic component traversals, cycles, and adjacency isolation."""

import pytest

from data_structures.graph import Graph


def example_graph():
    graph = Graph()
    for source, target in [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("d", "a")]:
        graph.add_edge(source, target)
    graph.add_vertex("isolated")
    return graph


def test_known_bfs_dfs_order_with_cycles_and_disconnected_vertex():
    graph = example_graph()
    before = graph.display()
    assert graph.bfs("a") == ["a", "b", "c", "d"]
    assert graph.dfs("a") == ["a", "b", "d", "c"]
    assert graph.bfs("isolated") == graph.dfs("isolated") == ["isolated"]
    assert graph.display() == before and len(graph) == 5
    assert graph.vertices() == ["a", "b", "c", "d", "isolated"]


def test_undirected_duplicate_edges_self_loops_and_detached_display():
    graph = Graph()
    assert graph.is_empty() and graph.add_edge(1, 2) is True
    assert graph.add_edge(2, 1) is False and graph.add_vertex(1) is False
    assert graph.add_edge(1, 1) is True and graph.add_edge(1, 1) is False
    assert graph.display() == {1: [2, 1], 2: [1]}
    copy = graph.display()
    copy[1].clear()
    copy[3] = []
    assert graph.bfs(1) == graph.dfs(1) == [1, 2]


@pytest.mark.parametrize("operation", ["bfs", "dfs"])
def test_unknown_start_is_explicit(operation):
    with pytest.raises(KeyError, match="starting vertex"):
        getattr(Graph(), operation)(0)


def test_invalid_second_endpoint_does_not_add_first_endpoint():
    graph = Graph()
    with pytest.raises(TypeError):
        graph.add_edge("valid", [])
    assert graph.is_empty()
    with pytest.raises(TypeError):
        graph.add_vertex([])


def test_none_and_mixed_hashable_vertices_need_no_sorting():
    graph = Graph()
    graph.add_edge(None, 1)
    graph.add_edge(1, "two")
    assert graph.dfs(None) == graph.bfs(None) == [None, 1, "two"]


def test_long_path_needs_no_recursive_stack():
    graph = Graph()
    for vertex in range(1500):
        graph.add_edge(vertex, vertex + 1)
    assert graph.bfs(0) == graph.dfs(0) == list(range(1501))
