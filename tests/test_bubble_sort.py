"""Correctness, event replay, operation counts, and immutable snapshot checks."""

from dataclasses import FrozenInstanceError
from itertools import product
from random import Random

import pytest

from algorithms.bubble_sort import bubble_sort


@pytest.mark.parametrize(
    "values",
    [[], [7], [1, 2, 3], [3, 2, 1], [-4, 2, -1, 0], [2, 1, 2, 1], [5, 5, 5]],
)
def test_sort_matches_oracle_without_mutation(values):
    original = values.copy()
    result = bubble_sort(values)
    assert result.sorted_values == tuple(sorted(original))
    assert values == original
    assert result.steps[0].event == "initial"
    assert result.steps[0].values == tuple(original)
    assert result.steps[-1].event == "final"
    assert result.steps[-1].values == result.sorted_values


def test_exact_trace_for_known_execution():
    result = bubble_sort([3, 1, 2])
    observed = [
        (step.event, step.values, step.compared_indices, step.comparisons, step.swaps)
        for step in result.steps
    ]
    assert observed == [
        ("initial", (3, 1, 2), None, 0, 0),
        ("compare", (3, 1, 2), (0, 1), 1, 0),
        ("swap", (1, 3, 2), (0, 1), 1, 1),
        ("compare", (1, 3, 2), (1, 2), 2, 1),
        ("swap", (1, 2, 3), (1, 2), 2, 2),
        ("compare", (1, 2, 3), (0, 1), 3, 2),
        ("final", (1, 2, 3), None, 3, 2),
    ]


def assert_replay(values):
    """Independently replay the emitted actions rather than another sort loop."""
    result = bubble_sort(values)
    replay = values.copy()
    comparisons = swaps = 0
    pending_swap = None
    for step in result.steps[1:-1]:
        assert step.compared_indices is not None
        left, right = step.compared_indices
        assert 0 <= left < right < len(values) and right == left + 1
        if step.event == "compare":
            assert pending_swap is None
            assert step.values == tuple(replay)
            comparisons += 1
            if replay[left] > replay[right]:
                pending_swap = (left, right)
        else:
            assert step.event == "swap"
            assert pending_swap == (left, right)
            replay[left], replay[right] = replay[right], replay[left]
            swaps += 1
            pending_swap = None
            assert step.values == tuple(replay)
        assert (step.comparisons, step.swaps) == (comparisons, swaps)
    assert pending_swap is None
    assert tuple(replay) == result.sorted_values == tuple(sorted(values))
    assert (comparisons, swaps) == (result.comparisons, result.swaps)
    assert (result.steps[-1].comparisons, result.steps[-1].swaps) == (comparisons, swaps)
    assert len(result.steps) == comparisons + swaps + 2
    # Each adjacent exchange removes exactly one inversion.
    inversions = sum(
        values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values))
    )
    assert swaps == inversions


def test_exhaustive_short_lists_replay_every_event():
    for size in range(6):
        for values in product((-1, 0, 1), repeat=size):
            assert_replay(list(values))


def test_seeded_random_traces_match_oracle_and_inversion_count():
    rng = Random(506)
    for _ in range(50):
        assert_replay([rng.randrange(-20, 21) for _ in range(rng.randrange(25))])


def test_early_exit_and_reverse_counts():
    assert bubble_sort(list(range(12))).comparisons == 11
    assert bubble_sort([4] * 12).comparisons == 11
    reverse = bubble_sort(list(range(11, -1, -1)))
    assert reverse.comparisons == reverse.swaps == 12 * 11 // 2


def test_results_and_snapshots_remain_immutable_and_detached():
    values = [2, 1]
    result = bubble_sort(values)
    values[0] = 99
    assert result.steps[0].values == (2, 1)
    assert result.sorted_values == (1, 2)
    with pytest.raises(FrozenInstanceError):
        result.swaps = 0
    with pytest.raises(FrozenInstanceError):
        result.steps[0].event = "final"
    with pytest.raises(TypeError):
        result.steps[0].values[0] = 99


@pytest.mark.parametrize("values", [[], [1], [3, 2, 1], [-1, 2, -1], [4] * 4])
def test_explicit_untraced_mode_preserves_output_and_counts(values):
    traced = bubble_sort(values)
    untraced = bubble_sort(values, track_steps=False)
    assert untraced.steps == ()
    assert untraced.sorted_values == traced.sorted_values
    assert (untraced.comparisons, untraced.swaps) == (traced.comparisons, traced.swaps)


@pytest.mark.parametrize("values", [None, (1, 2), "12", [1.0], [True], [1, "2"]])
def test_invalid_values_have_clear_errors(values):
    with pytest.raises(TypeError, match="integers"):
        bubble_sort(values)


@pytest.mark.parametrize("track_steps", [None, 0, 1, "yes"])
def test_trace_flag_requires_bool(track_steps):
    with pytest.raises(TypeError, match="track_steps"):
        bubble_sort([2, 1], track_steps=track_steps)
