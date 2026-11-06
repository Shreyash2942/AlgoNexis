"""Allowlisted dispatch, state persistence, and safe result ownership."""

import pytest

from data_structures.manager import DataStructureManager


def test_stateful_sequences_and_derived_sets_return_plain_values():
    manager = DataStructureManager()
    assert manager.execute("set", "add", value=1) is True
    assert manager.execute("set", "union", values=[2, 3]) == [1, 2, 3]
    assert manager.execute("set", "display") == [1]
    manager.execute("stack", "push", value=10)
    manager.execute("stack", "push", value=20)
    assert manager.execute("stack", "pop") == 20
    manager.execute("queue", "enqueue", value=10)
    manager.execute("queue", "enqueue", value=20)
    assert manager.execute("queue", "dequeue") == 10
    for value in [2, 1, 3]:
        manager.execute("tree", "insert", value=value)
    assert manager.execute("tree", "inorder") == [1, 2, 3]
    manager.execute("graph", "add_edge", source="a", target="b")
    assert manager.execute("graph", "bfs", start="a") == ["a", "b"]
    manager.execute("hash_table", "insert", key="a", value=None)
    assert manager.execute("hash_table", "find", key="a") is None


def test_managers_registry_metadata_and_display_results_are_isolated():
    first, second = DataStructureManager(), DataStructureManager()
    first.execute("set", "add", value=1)
    assert second.execute("set", "is_empty")
    view = first.execute("set", "display")
    view.clear()
    metadata = first.available_operations()
    metadata["set"].clear()
    assert first.execute("set", "contains", value=1)
    assert "add" in first.available_operations()["set"]
    assert first.execute("set", "size") == 1
    assert first.execute("stack", "size") == 0


@pytest.mark.parametrize("structure,operation", [
    ("unknown", "display"), ("stack", "__class__"),
    ("stack", "_items"), ("set", "clear"), ("stack", "eval('1')"),
])
def test_unsupported_requests_fail_without_mutation(structure, operation):
    manager = DataStructureManager()
    with pytest.raises(ValueError, match="unsupported"):
        manager.execute(structure, operation)
    assert manager.execute("stack", "is_empty")


@pytest.mark.parametrize("structure,operation", [(None, "display"), ("set", []), ([], "add")])
def test_names_must_be_strings(structure, operation):
    with pytest.raises(TypeError, match="strings"):
        DataStructureManager().execute(structure, operation)


@pytest.mark.parametrize("kwargs", [{}, {"item": 1}, {"value": 1, "extra": 2}])
def test_argument_errors_are_clear_and_do_not_mutate(kwargs):
    manager = DataStructureManager()
    with pytest.raises(TypeError, match="invalid arguments for stack.push"):
        manager.execute("stack", "push", **kwargs)
    assert manager.execute("stack", "is_empty")


def test_structure_domain_errors_preserve_exception_type():
    manager = DataStructureManager()
    with pytest.raises(IndexError):
        manager.execute("queue", "front")
    with pytest.raises(KeyError):
        manager.execute("hash_table", "find", key="missing")
    with pytest.raises(TypeError):
        manager.execute("tree", "insert", value=True)


def test_size_operation_cannot_override_its_bound_instance():
    manager = DataStructureManager()
    manager.execute("set", "add", value=1)
    with pytest.raises(TypeError, match="invalid arguments"):
        manager.execute("set", "size", instance=[])
    assert manager.execute("set", "size") == 1
