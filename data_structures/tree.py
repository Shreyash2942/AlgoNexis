"""Iterative unbalanced integer BST adapted from Module 6 treemap patterns.

Duplicates are ignored. Insert/search cost O(h), up to O(n) on a skewed tree.
Traversals cost O(n) time and O(h) workspace plus O(n) returned values. Iteration
avoids Python recursion limits; no balancing or deletion is promised.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(slots=True)
class _Node:
    value: int
    left: _Node | None = None
    right: _Node | None = None


class BinarySearchTree:
    def __init__(self, values: Iterable[int] = ()) -> None:
        self._root: _Node | None = None
        self._size = 0
        for value in values:
            self.insert(value)

    @staticmethod
    def _validate(value: int) -> None:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("tree values must be integers, excluding booleans")

    def insert(self, value: int) -> bool:
        """Return True if inserted, False if the value already exists."""
        self._validate(value)
        if self._root is None:
            self._root = _Node(value)
        else:
            current = self._root
            while True:
                if value == current.value:
                    return False
                if value < current.value:
                    if current.left is None:
                        current.left = _Node(value)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = _Node(value)
                        break
                    current = current.right
        self._size += 1
        return True

    def search(self, value: int) -> bool:
        self._validate(value)
        current = self._root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def inorder(self) -> list[int]:
        result, stack = [], []
        current = self._root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def preorder(self) -> list[int]:
        result = []
        stack = [self._root] if self._root is not None else []
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result

    def postorder(self) -> list[int]:
        result = []
        stack = [(self._root, False)] if self._root is not None else []
        while stack:
            node, expanded = stack.pop()
            if expanded:
                result.append(node.value)
            else:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
        return result

    def display(self) -> list[int]:
        """Detached inorder values; internal nodes are never exposed."""
        return self.inorder()

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size
