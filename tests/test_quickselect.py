"""One-based selection correctness and reproducible partition policy checks."""

from itertools import product
from random import Random, getstate

import pytest

from algorithms.quickselect import quickselect


@pytest.mark.parametrize(
    "values",
    [[8], [1, 2, 3, 4], [4, 3, 2, 1], [-4, 5, -1, 0], [2, 2, 1, 2], [7] * 8],
)
def test_all_valid_ranks_match_oracle_without_mutating_input(values):
    original = values.copy()
    for k, expected in enumerate(sorted(values), start=1):
        assert quickselect(values, k, rng=Random(42)) == expected
        assert values == original


def test_exhaustive_short_lists_at_every_rank():
    for size in range(1, 6):
        for values in product((-1, 0, 1), repeat=size):
            for k, expected in enumerate(sorted(values), start=1):
                assert quickselect(list(values), k, rng=Random(506)) == expected


def test_seeded_random_lists_first_middle_and_last_ranks():
    rng = Random(506)
    for _ in range(100):
        values = [rng.randrange(-100, 101) for _ in range(rng.randrange(1, 80))]
        ordered = sorted(values)
        for k in {1, (len(values) + 1) // 2, len(values)}:
            assert quickselect(values, k, rng=Random(37)) == ordered[k - 1]


@pytest.mark.parametrize("k", [-1, 0, 4])
def test_invalid_rank_bounds(k):
    with pytest.raises(ValueError, match="1 <= k"):
        quickselect([1, 2, 3], k)


def test_empty_input_is_rejected():
    with pytest.raises(ValueError, match="nonempty"):
        quickselect([], 1)


@pytest.mark.parametrize("k", [True, False, 1.0, "1", None])
def test_noninteger_ranks_are_rejected(k):
    with pytest.raises(TypeError, match="k must be an integer"):
        quickselect([1, 2], k)


@pytest.mark.parametrize("values", [None, (1, 2), "12", [1.0], [True], [1, "2"]])
def test_invalid_values_are_rejected(values):
    with pytest.raises(TypeError, match="integers"):
        quickselect(values, 1)


def test_invalid_generator_is_rejected():
    with pytest.raises(TypeError, match="rng"):
        quickselect([1], 1, rng=42)


class RecordingRandom(Random):
    """Observe the public RNG contract without duplicating selection logic."""

    def __init__(self, seed):
        super().__init__(seed)
        self.choices = []

    def randrange(self, start, stop=None, step=1):
        value = super().randrange(start, stop, step)
        self.choices.append((start, stop, value))
        return value


def test_pivot_choices_repeat_with_a_fresh_seeded_generator():
    values = list(range(30, -1, -1))
    first = RecordingRandom(42)
    second = RecordingRandom(42)
    assert quickselect(values, 12, rng=first) == quickselect(values, 12, rng=second) == 11
    assert first.choices and first.choices == second.choices


def test_equal_values_are_handled_in_one_partition():
    rng = RecordingRandom(42)
    assert quickselect([7] * 10000, 5000, rng=rng) == 7
    assert len(rng.choices) == 1


def test_large_ordered_input_needs_no_recursive_call_stack():
    assert quickselect(list(range(10000)), 5000, rng=Random(42)) == 4999


def test_default_generator_does_not_change_global_random_state():
    before = getstate()
    assert quickselect([4, 2, 1, 3], 2) == 2
    assert getstate() == before
