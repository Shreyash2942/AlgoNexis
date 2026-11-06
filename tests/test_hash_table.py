"""Collision chains, missing keys, updates, and mapping-model workloads."""

from random import Random

import pytest

from data_structures.hash_table import HashTable


class CollidingKey:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 7

    def __eq__(self, other):
        return isinstance(other, CollidingKey) and self.value == other.value


def test_colliding_keys_update_find_and_delete_independently():
    table = HashTable(2)
    keys = [CollidingKey(value) for value in range(5)]
    for index, key in enumerate(keys):
        assert table.insert(key, index) is True
    assert len(table) == 5 and table.load_factor == 2.5
    assert table.insert(CollidingKey(2), 99) is False and len(table) == 5
    assert table.find(keys[2]) == 99
    assert table.delete(CollidingKey(2)) == 99
    assert [table.find(keys[i]) for i in [0, 1, 3, 4]] == [0, 1, 3, 4]
    for index in [0, 4, 1, 3]:
        assert table.delete(keys[index]) == index
    assert table.is_empty()


def test_none_values_missing_keys_and_detached_buckets():
    table = HashTable(1)
    assert table.insert("key", None) is True
    assert table.find("key") is None and table.contains("key")
    view, buckets = table.display(), table.buckets()
    view.clear()
    buckets[0].clear()
    assert table.find("key") is None and len(table) == 1
    assert table.delete("key") is None
    for operation in (table.find, table.delete):
        with pytest.raises(KeyError):
            operation("key")
    assert not table.contains("key")


def test_supported_hashable_keys_and_identity_equality_semantics():
    table = HashTable()
    for key in [None, -4, "four", (1, 2)]:
        table.insert(key, repr(key))
        assert table.find(key) == repr(key)
    table.insert(True, "first")
    assert table.insert(1, "updated") is False
    assert table.find(True) == "updated"
    nan = float("nan")
    table.insert(nan, "nan value")
    assert table.find(nan) == "nan value"


@pytest.mark.parametrize("capacity", [0, -1])
def test_nonpositive_capacity(capacity):
    with pytest.raises(ValueError, match="positive"):
        HashTable(capacity)


@pytest.mark.parametrize("capacity", [True, 1.5, "8", None])
def test_invalid_capacity_type(capacity):
    with pytest.raises(TypeError, match="capacity"):
        HashTable(capacity)


@pytest.mark.parametrize("operation", ["insert", "find", "delete", "contains"])
def test_unhashable_keys_fail_without_mutation(operation):
    table = HashTable()
    with pytest.raises(TypeError):
        if operation == "insert":
            table.insert([], 1)
        else:
            getattr(table, operation)([])
    assert table.is_empty()


def test_seeded_mutations_match_dict_reference_with_fixed_capacity():
    rng, table, expected = Random(506), HashTable(3), {}
    for _ in range(600):
        key = rng.randrange(-20, 21)
        if rng.randrange(3):
            value = rng.choice([None, -1, 0, 1])
            assert table.insert(key, value) == (key not in expected)
            expected[key] = value
        elif key in expected:
            assert table.delete(key) == expected.pop(key)
        else:
            with pytest.raises(KeyError):
                table.delete(key)
        assert len(table) == len(expected)
        assert dict(table.display()) == expected and table.capacity == 3
