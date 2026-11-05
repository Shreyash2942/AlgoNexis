"""Deque-backed FIFO queue, adapted from Module 4's list-backed queue API.

Deque replaces list.pop(0): enqueue/dequeue/front/size/empty checks are O(1).
Display is O(n), storage O(n); display does not expose the internal container.
"""

from collections import deque
from collections.abc import Iterable
from typing import Any


class Queue:
    def __init__(self, values: Iterable[Any] = ()) -> None:
        self._items = deque(values)

    def enqueue(self, value: Any) -> None:
        self._items.append(value)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("cannot dequeue from an empty queue")
        return self._items.popleft()

    def front(self) -> Any:
        if self.is_empty():
            raise IndexError("cannot inspect the front of an empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return not self._items

    def display(self) -> list[Any]:
        """Shallow copy in front-to-rear order."""
        return list(self._items)

    def __len__(self) -> int:
        return len(self._items)
