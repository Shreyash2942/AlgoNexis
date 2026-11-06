"""Undirected, unweighted graph with insertion-ordered adjacency lists.

Hashable vertices, automatic endpoint creation, idempotent edges, and self-loops
are supported. BFS/DFS visit only the starting component in neighbor insertion
order. Traversal costs O(Vr + Er) time/O(Vr) workspace; storage is O(V + E).
Algorithms adapt the Module 7 VertexTrace BFS/iterator-stack DFS patterns.
"""

from collections import deque
from collections.abc import Hashable


class Graph:
    def __init__(self) -> None:
        self._adjacency: dict[Hashable, dict[Hashable, None]] = {}

    def add_vertex(self, vertex: Hashable) -> bool:
        """Add if missing; return whether the vertex is new."""
        if vertex in self._adjacency:
            return False
        self._adjacency[vertex] = {}
        return True

    def add_edge(self, source: Hashable, target: Hashable) -> bool:
        """Validate both endpoints before mutating, then add an undirected edge."""
        hash(source)
        hash(target)
        self.add_vertex(source)
        self.add_vertex(target)
        added = target not in self._adjacency[source]
        self._adjacency[source][target] = None
        self._adjacency[target][source] = None
        return added

    def _require_start(self, start: Hashable) -> None:
        if start not in self._adjacency:
            raise KeyError(f"unknown starting vertex: {start!r}")

    def bfs(self, start: Hashable) -> list[Hashable]:
        self._require_start(start)
        visited, queue, result = {start}, deque([start]), []
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor in self._adjacency[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start: Hashable) -> list[Hashable]:
        """Match recursive preorder using neighbor iterators, without recursion."""
        self._require_start(start)
        visited, result = {start}, [start]
        stack = [iter(self._adjacency[start])]
        exhausted = object()
        while stack:
            neighbor = next(stack[-1], exhausted)
            if neighbor is exhausted:
                stack.pop()
            elif neighbor not in visited:
                visited.add(neighbor)
                result.append(neighbor)
                stack.append(iter(self._adjacency[neighbor]))
        return result

    def vertices(self) -> list[Hashable]:
        return list(self._adjacency)

    def display(self) -> dict[Hashable, list[Hashable]]:
        """Copy the adjacency mapping and each neighbor container, in order."""
        return {vertex: list(neighbors) for vertex, neighbors in self._adjacency.items()}

    def is_empty(self) -> bool:
        return not self._adjacency

    def __len__(self) -> int:
        return len(self._adjacency)
