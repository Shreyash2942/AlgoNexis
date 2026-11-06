"""Persistent structure instances behind an explicit operation allowlist.

No eval, dynamic attribute lookup, or UI imports. Results are ordinary values,
lists, or dictionaries; derived CustomSets are converted to detached lists.
Separate manager instances own separate structures.
"""

from collections.abc import Callable
from functools import partial
from inspect import signature
from typing import Any

from data_structures.custom_set import CustomSet
from data_structures.graph import Graph
from data_structures.hash_table import HashTable
from data_structures.queue import Queue
from data_structures.stack import Stack
from data_structures.tree import BinarySearchTree


class DataStructureManager:
    def __init__(self, *, hash_capacity: int = 8) -> None:
        custom_set, stack, queue = CustomSet(), Stack(), Queue()
        tree, graph, table = BinarySearchTree(), Graph(), HashTable(hash_capacity)
        self._structures = {
            "set": custom_set, "stack": stack, "queue": queue,
            "tree": tree, "graph": graph, "hash_table": table,
        }
        self._operations: dict[str, dict[str, Callable[..., Any]]] = {
            "set": {
                "add": custom_set.add, "remove": custom_set.remove,
                "discard": custom_set.discard, "contains": custom_set.contains,
                "union": lambda values: custom_set.union(CustomSet(values)),
                "intersection": lambda values: custom_set.intersection(CustomSet(values)),
                "difference": lambda values: custom_set.difference(CustomSet(values)),
                "symmetric_difference": lambda values: custom_set.symmetric_difference(CustomSet(values)),
            },
            "stack": {"push": stack.push, "pop": stack.pop, "peek": stack.peek},
            "queue": {"enqueue": queue.enqueue, "dequeue": queue.dequeue, "front": queue.front},
            "tree": {
                "insert": tree.insert, "search": tree.search, "inorder": tree.inorder,
                "preorder": tree.preorder, "postorder": tree.postorder,
            },
            "graph": {
                "add_vertex": graph.add_vertex, "add_edge": graph.add_edge,
                "bfs": graph.bfs, "dfs": graph.dfs, "vertices": graph.vertices,
            },
            "hash_table": {
                "insert": table.insert, "find": table.find, "delete": table.delete,
                "contains": table.contains, "capacity": lambda: table.capacity,
                "load_factor": lambda: table.load_factor, "buckets": table.buckets,
            },
        }
        # Bind each instance without exposing it as an overridable keyword.
        for name, instance in self._structures.items():
            self._operations[name].update({
                "display": instance.display,
                "is_empty": instance.is_empty,
                "size": partial(len, instance),
            })

    def available_operations(self) -> dict[str, list[str]]:
        """Detached registry metadata for UI choices; exposes no bound methods."""
        return {name: list(operations) for name, operations in self._operations.items()}

    def execute(self, structure: str, operation: str, **kwargs: Any) -> Any:
        """Dispatch a named operation with keyword arguments and preserve state.

        Unknown names raise ValueError. Bad name/argument types raise TypeError.
        Domain errors (IndexError, KeyError, TypeError) keep their original type.
        """
        if not isinstance(structure, str) or not isinstance(operation, str):
            raise TypeError("structure and operation names must be strings")
        if structure not in self._operations:
            raise ValueError(f"unsupported structure {structure!r}; choose from {list(self._operations)}")
        operations = self._operations[structure]
        if operation not in operations:
            raise ValueError(f"unsupported operation {operation!r} for {structure!r}; choose from {list(operations)}")
        method = operations[operation]
        try:
            signature(method).bind(**kwargs)
        except TypeError as error:
            raise TypeError(f"invalid arguments for {structure}.{operation}: {error}") from error
        result = method(**kwargs)
        return result.display() if isinstance(result, CustomSet) else result
