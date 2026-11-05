"""Adjacent-element Bubble Sort with an optional complete, immutable trace.

The caller's list is never mutated. Without tracing, early exit gives O(n) best
and O(n**2) average/worst time; copying the input uses O(n) auxiliary space.
With tracing, each event copies n elements: O(n * (comparisons + swaps + 1))
time and stored elements, up to O(n**3). Even sorted-input tracing is O(n**2).

Example:
    >>> result = bubble_sort([3, 1, 2])
    >>> result.sorted_values
    (1, 2, 3)
    >>> (result.comparisons, result.swaps)
    (3, 2)
"""

from dataclasses import dataclass
from typing import Literal

from algorithms._validation import copy_integer_list

StepEvent = Literal["initial", "compare", "swap", "final"]


@dataclass(frozen=True, slots=True)
class SortingStep:
    """One observed event; counters are cumulative as of this snapshot.

    A compare event precedes its possible swap; its comparison is already
    counted. A swap event follows the exchange and increments swaps only.
    Initial/final events carry no highlighted indices, including n < 2.
    """

    event: StepEvent
    values: tuple[int, ...]
    compared_indices: tuple[int, int] | None
    comparisons: int
    swaps: int


@dataclass(frozen=True, slots=True)
class BubbleSortResult:
    """Sorted values, exact operation totals, and an optional event sequence."""

    sorted_values: tuple[int, ...]
    comparisons: int
    swaps: int
    steps: tuple[SortingStep, ...]


def bubble_sort(values: list[int], *, track_steps: bool = True) -> BubbleSortResult:
    """Return a nonmutating sort result; duplicates keep their relative order.

    ``track_steps=True`` records initial, every comparison, every actual swap,
    then final. It never truncates events. False produces an empty steps tuple
    with identical output and totals, suitable for later execution benchmarks.

    Raises:
        TypeError: Input is not a list of integers, includes bool, or
            track_steps is not a bool.
    """
    working = copy_integer_list(values)
    if not isinstance(track_steps, bool):
        raise TypeError("track_steps must be a boolean")

    comparisons = 0
    swaps = 0
    steps: list[SortingStep] = []
    if track_steps:
        steps.append(SortingStep("initial", tuple(working), None, 0, 0))

    for end in range(len(working) - 1, 0, -1):
        swapped_this_pass = False
        for left in range(end):
            right = left + 1
            comparisons += 1
            if track_steps:
                steps.append(
                    SortingStep(
                        "compare", tuple(working), (left, right), comparisons, swaps
                    )
                )
            if working[left] > working[right]:
                working[left], working[right] = working[right], working[left]
                swaps += 1
                swapped_this_pass = True
                if track_steps:
                    steps.append(
                        SortingStep(
                            "swap", tuple(working), (left, right), comparisons, swaps
                        )
                    )
        if not swapped_this_pass:
            break

    sorted_values = tuple(working)
    if track_steps:
        steps.append(SortingStep("final", sorted_values, None, comparisons, swaps))
    return BubbleSortResult(sorted_values, comparisons, swaps, tuple(steps))
