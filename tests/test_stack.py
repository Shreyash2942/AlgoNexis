"""LIFO, error, and detached-inspection contracts."""

from random import Random

import pytest

from data_structures.stack import Stack


def test_lifo_peek_size_and_detached_input_display():
    original = [1, 2]
    stack = Stack(original)
    original.append(99)
    stack.push(3)
    assert len(stack) == 3 and stack.peek() == 3
    view = stack.display()
    view.clear()
    assert stack.display() == [1, 2, 3]
    assert [stack.pop(), stack.pop(), stack.pop()] == [3, 2, 1]
    assert stack.is_empty()


@pytest.mark.parametrize("operation", ["pop", "peek"])
def test_empty_operations_raise_index_error(operation):
    with pytest.raises(IndexError, match="empty stack"):
        getattr(Stack(), operation)()


def test_seeded_mixed_workload_matches_list_model():
    rng, stack, model = Random(506), Stack(), []
    for _ in range(500):
        if not model or rng.randrange(2):
            value = rng.randrange(-10, 11)
            stack.push(value)
            model.append(value)
        else:
            assert stack.peek() == model[-1]
            assert stack.pop() == model.pop()
        assert stack.display() == model and len(stack) == len(model)
