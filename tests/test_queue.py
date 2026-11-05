"""FIFO, error, and detached-inspection contracts."""

from random import Random

import pytest

from data_structures.queue import Queue


def test_fifo_front_size_and_detached_input_display():
    original = [1, 2]
    queue = Queue(original)
    original.append(99)
    queue.enqueue(3)
    assert len(queue) == 3 and queue.front() == 1
    view = queue.display()
    view.clear()
    assert queue.display() == [1, 2, 3]
    assert [queue.dequeue(), queue.dequeue(), queue.dequeue()] == [1, 2, 3]
    assert queue.is_empty()


@pytest.mark.parametrize("operation", ["dequeue", "front"])
def test_empty_operations_raise_index_error(operation):
    with pytest.raises(IndexError, match="empty queue"):
        getattr(Queue(), operation)()


def test_seeded_mixed_workload_matches_fifo_list_model():
    rng, queue, model = Random(506), Queue(), []
    for _ in range(500):
        if not model or rng.randrange(2):
            value = rng.randrange(-10, 11)
            queue.enqueue(value)
            model.append(value)
        else:
            assert queue.front() == model[0]
            assert queue.dequeue() == model.pop(0)
        assert queue.display() == model and len(queue) == len(model)
