"""Prepare immutable Bubble Sort frames without a Streamlit dependency.

Example:
    >>> from algorithms.bubble_sort import bubble_sort
    >>> visualizer = SortingVisualizer(bubble_sort([2, 1]))
    >>> [frame.event for frame in visualizer]
    ['initial', 'compare', 'swap', 'final']
    >>> visualizer.get_step(visualizer.total_steps - 1).values
    (1, 2)
"""

from collections.abc import Iterator
from dataclasses import dataclass

from algorithms.bubble_sort import BubbleSortResult, StepEvent


@dataclass(frozen=True, slots=True)
class SortingFrame:
    """UI-ready metadata; values reuse the algorithm's immutable snapshot."""

    step_index: int
    total_steps: int
    event: StepEvent
    values: tuple[int, ...]
    highlighted_indices: tuple[int, ...]
    swapped: bool
    comparisons: int
    swaps: int
    description: str


class SortingVisualizer:
    """Read-only, index-based view of a traced BubbleSortResult.

    Indices are zero-based; negative/out-of-range indices raise IndexError.
    Trace-disabled results raise ValueError. Construction and retrieval are
    O(1), apart from formatting integer text; iteration is O(number of events)
    plus that text formatting. No snapshots are copied or events discarded.
    """

    def __init__(self, result: BubbleSortResult) -> None:
        if not isinstance(result, BubbleSortResult):
            raise TypeError("result must be a BubbleSortResult")
        if not result.steps:
            raise ValueError("visualization requires bubble_sort(..., track_steps=True)")
        self._result = result

    @property
    def total_steps(self) -> int:
        """Number of available frames, including initial and final states."""
        return len(self._result.steps)

    def get_step(self, index: int) -> SortingFrame:
        """Return the requested frame without altering playback or result state."""
        if isinstance(index, bool) or not isinstance(index, int):
            raise TypeError("step index must be an integer")
        if not 0 <= index < self.total_steps:
            raise IndexError("step index is outside the recorded trace")
        step = self._result.steps[index]
        highlights = step.compared_indices or ()
        if step.event == "initial":
            description = "Initial state."
        elif step.event == "final":
            description = (
                f"Sorted state: {step.comparisons} comparisons, {step.swaps} swaps."
            )
        elif step.event == "compare":
            left, right = highlights
            description = (
                f"Compare indices {left} and {right}: "
                f"{step.values[left]} and {step.values[right]}."
            )
        else:
            left, right = highlights
            description = f"Swap indices {left} and {right}."
        return SortingFrame(
            step_index=index,
            total_steps=self.total_steps,
            event=step.event,
            values=step.values,
            highlighted_indices=highlights,
            swapped=step.event == "swap",
            comparisons=step.comparisons,
            swaps=step.swaps,
            description=description,
        )

    def __iter__(self) -> Iterator[SortingFrame]:
        """Yield every frame in execution order, without keeping a cursor."""
        for index in range(self.total_steps):
            yield self.get_step(index)
