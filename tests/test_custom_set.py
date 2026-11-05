"""Mathematical reference checks and mutation contracts for CustomSet."""

from itertools import combinations

import pytest

from data_structures.custom_set import CustomSet


def test_uniqueness_display_and_order_independent_equality():
    values = CustomSet([3, 1, 3, 2])
    assert values.display() == [3, 1, 2]
    assert len(values) == 3 and not values.is_empty()
    assert values == CustomSet([2, 1, 3])
    assert values != CustomSet([1, 2])
    assert values != [3, 1, 2]


def test_mutations_membership_and_missing_values():
    values = CustomSet()
    assert values.is_empty()
    assert values.add(2) is True and values.add(2) is False
    assert 2 in values and values.contains(2)
    assert values.discard(3) is False
    assert values.remove(2) is None and values.is_empty()
    with pytest.raises(KeyError):
        values.remove(2)
    values.add(3)
    assert values.discard(3) is True and values.is_empty()


@pytest.mark.parametrize(
    "operation,oracle",
    [("union", set.union), ("intersection", set.intersection),
     ("difference", set.difference), ("symmetric_difference", set.symmetric_difference)],
)
def test_all_subset_pairs_match_builtin_oracle_and_preserve_operands(operation, oracle):
    subsets = [list(c) for n in range(5) for c in combinations(range(4), n)]
    for left_values in subsets:
        for right_values in subsets:
            left, right = CustomSet(left_values), CustomSet(right_values)
            result = getattr(left, operation)(right)
            assert set(result) == oracle(set(left_values), set(right_values))
            assert left.display() == left_values and right.display() == right_values
            assert result is not left and result is not right
            result.add(99)
            assert 99 not in left and 99 not in right


def test_hashable_values_follow_python_equality_and_inspection_is_detached():
    values = CustomSet([1, True, None, "a", (1, 2)])
    assert len(values) == 4
    view = values.display()
    view.clear()
    assert len(values) == 4


@pytest.mark.parametrize("operation", ["add", "contains", "remove", "discard"])
def test_unhashable_values_fail_without_changing_members(operation):
    values = CustomSet([1])
    with pytest.raises(TypeError):
        getattr(values, operation)([])
    assert values.display() == [1]


@pytest.mark.parametrize("operation", ["union", "intersection", "difference", "symmetric_difference"])
def test_derived_operations_require_custom_set_operands(operation):
    with pytest.raises(TypeError, match="CustomSet"):
        getattr(CustomSet([1]), operation)([2])
