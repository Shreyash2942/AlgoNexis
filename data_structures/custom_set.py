"""Insertion-ordered custom set with explicitly implemented set algebra.

A dict stores hashable members and enforces Python hash/equality uniqueness
(so 1 and True denote the same member). No built-in set algebra is delegated.
Membership/add/remove are expected O(1), worst O(n) with pathological hashes.
Display copies the container, not the objects stored inside it.
"""

from collections.abc import Hashable, Iterable, Iterator


class CustomSet:
    """Mutable membership with nonmutating, new-set derived operations."""

    def __init__(self, values: Iterable[Hashable] = ()) -> None:
        self._items: dict[Hashable, None] = {}
        for value in values:
            self.add(value)

    def add(self, value: Hashable) -> bool:
        """Insert a hashable value; return True only when membership changes."""
        if value in self._items:
            return False
        self._items[value] = None
        return True

    def remove(self, value: Hashable) -> None:
        """Remove a member, raising KeyError if absent."""
        del self._items[value]

    def discard(self, value: Hashable) -> bool:
        """Remove if present; return whether membership changed."""
        if value not in self._items:
            return False
        del self._items[value]
        return True

    def contains(self, value: Hashable) -> bool:
        return value in self._items

    def is_empty(self) -> bool:
        return not self._items

    def display(self) -> list[Hashable]:
        """Return a detached member list in insertion order."""
        return list(self._items)

    @staticmethod
    def _require_set(other: "CustomSet") -> None:
        if not isinstance(other, CustomSet):
            raise TypeError("operand must be a CustomSet")

    def union(self, other: "CustomSet") -> "CustomSet":
        """New set of both operands, left members followed by new right members."""
        self._require_set(other)
        result = CustomSet(self)
        for value in other:
            result.add(value)
        return result

    def intersection(self, other: "CustomSet") -> "CustomSet":
        self._require_set(other)
        return CustomSet(value for value in self if value in other)

    def difference(self, other: "CustomSet") -> "CustomSet":
        self._require_set(other)
        return CustomSet(value for value in self if value not in other)

    def symmetric_difference(self, other: "CustomSet") -> "CustomSet":
        self._require_set(other)
        result = self.difference(other)
        for value in other:
            if value not in self:
                result.add(value)
        return result

    def __contains__(self, value: Hashable) -> bool:
        return self.contains(value)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[Hashable]:
        return iter(self._items)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CustomSet):
            return NotImplemented
        return len(self) == len(other) and all(value in other for value in self)
