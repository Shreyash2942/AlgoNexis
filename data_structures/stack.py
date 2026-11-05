"""List-backed LIFO stack, adapted from the Module 4 LinearDS-Suite pattern.

The API uses snake_case and detached display lists. Push/pop are amortized O(1),
peek/size/empty checks O(1), display O(n), and storage O(n).
"""

from collections.abc import Iterable
from typing import Any


class Stack:
    def __init__(self, values: Iterable[Any] = ()) -> None:
        self._items = list(values)

    def push(self, value: Any) -> None:
        self._items.append(value)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("cannot pop from an empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("cannot peek at an empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def display(self) -> list[Any]:
        """Shallow copy in bottom-to-top order."""
        return list(self._items)

    def __len__(self) -> int:
        return len(self._items)
