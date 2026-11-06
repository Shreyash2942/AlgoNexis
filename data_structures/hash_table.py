"""Custom fixed-capacity hash buckets with separate chaining.

Keys are hashable and must keep a stable hash/equality while stored. Python
identity/equality semantics apply. Values may be arbitrary, including None.
No dict stores entries. Capacity never resizes: expected operations cost
O(1 + n / capacity) under distributed hashing, worst O(n) for collisions.
Storage is O(capacity + n). Adapts the Module 5 heaphash-nexus bucket pattern.
"""

from collections.abc import Hashable
from typing import Any


class HashTable:
    def __init__(self, capacity: int = 8) -> None:
        if isinstance(capacity, bool) or not isinstance(capacity, int):
            raise TypeError("capacity must be an integer, excluding booleans")
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._buckets: list[list[tuple[Hashable, Any]]] = [[] for _ in range(capacity)]
        self._size = 0

    @property
    def capacity(self) -> int:
        return len(self._buckets)

    @property
    def load_factor(self) -> float:
        return self._size / self.capacity

    def _locate(self, key: Hashable) -> tuple[list[tuple[Hashable, Any]], int | None]:
        bucket = self._buckets[hash(key) % self.capacity]
        for index, (existing_key, _) in enumerate(bucket):
            if existing_key is key or existing_key == key:
                return bucket, index
        return bucket, None

    def insert(self, key: Hashable, value: Any) -> bool:
        """Insert/update; True for a new key, False for an update."""
        bucket, index = self._locate(key)
        if index is not None:
            bucket[index] = (bucket[index][0], value)
            return False
        bucket.append((key, value))
        self._size += 1
        return True

    def find(self, key: Hashable) -> Any:
        """Return the stored value, including None; raise KeyError if missing."""
        bucket, index = self._locate(key)
        if index is None:
            raise KeyError(key)
        return bucket[index][1]

    def delete(self, key: Hashable) -> Any:
        """Remove/return the value; raise KeyError if missing."""
        bucket, index = self._locate(key)
        if index is None:
            raise KeyError(key)
        _, value = bucket.pop(index)
        self._size -= 1
        return value

    def contains(self, key: Hashable) -> bool:
        return self._locate(key)[1] is not None

    def display(self) -> list[tuple[Hashable, Any]]:
        """Detached key/value pairs in bucket order, then chain insertion order."""
        return [pair for bucket in self._buckets for pair in bucket]

    def buckets(self) -> list[list[tuple[Hashable, Any]]]:
        """Detached bucket and chain containers for collision inspection."""
        return [list(bucket) for bucket in self._buckets]

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size
