"""Day 3's data-only playback contract and core import isolation."""

from dataclasses import FrozenInstanceError
import subprocess
import sys

import pytest

from algorithms.bubble_sort import bubble_sort
from visualization.sorting_visualizer import SortingVisualizer


@pytest.mark.parametrize("values", [[], [1], [2, 1], [3, -1, 3, 0], [1, 2, 3]])
def test_frames_cover_complete_trace_and_end_at_sorted_output(values):
    result = bubble_sort(values)
    view = SortingVisualizer(result)
    frames = list(view)
    assert len(frames) == view.total_steps == len(result.steps)
    assert [f.step_index for f in frames] == list(range(view.total_steps))
    assert frames[0].event == "initial" and frames[-1].event == "final"
    assert frames[0].highlighted_indices == frames[-1].highlighted_indices == ()
    assert frames[-1].values == result.sorted_values
    assert frames[-1].comparisons == result.comparisons
    assert frames[-1].swaps == result.swaps
    for frame, step in zip(frames, result.steps):
        assert frame.values is step.values
        assert frame.highlighted_indices == (step.compared_indices or ())
        assert frame.swapped == (step.event == "swap")
        assert frame.total_steps == view.total_steps
        assert frame.description
    assert list(view) == frames  # Replaying does not retain a stale cursor.


def test_highlight_and_description_metadata_match_observed_events():
    view = SortingVisualizer(bubble_sort([2, 1]))
    compare = view.get_step(1)
    assert compare.highlighted_indices == (0, 1)
    assert compare.values == (2, 1) and not compare.swapped
    assert compare.description == "Compare indices 0 and 1: 2 and 1."
    swap = view.get_step(2)
    assert swap.values == (1, 2) and swap.swapped
    assert swap.description == "Swap indices 0 and 1."
    with pytest.raises(FrozenInstanceError):
        swap.description = "changed"


@pytest.mark.parametrize("index", [-1, 4, 100])
def test_indices_outside_trace_are_rejected(index):
    with pytest.raises(IndexError, match="outside"):
        SortingVisualizer(bubble_sort([2, 1])).get_step(index)


@pytest.mark.parametrize("index", [True, 1.0, "1", None])
def test_noninteger_indices_are_rejected(index):
    with pytest.raises(TypeError, match="index"):
        SortingVisualizer(bubble_sort([2, 1])).get_step(index)


def test_trace_disabled_result_cannot_silently_produce_an_empty_visualization():
    with pytest.raises(ValueError, match="track_steps=True"):
        SortingVisualizer(bubble_sort([2, 1], track_steps=False))


def test_wrong_result_type_is_rejected():
    with pytest.raises(TypeError, match="BubbleSortResult"):
        SortingVisualizer([1, 2])


def test_core_imports_and_playback_need_only_the_standard_library():
    # -S disables site-packages, including the installed Streamlit distribution.
    script = (
        "import sys; from algorithms.bubble_sort import bubble_sort; "
        "from algorithms.quickselect import quickselect; "
        "from visualization.sorting_visualizer import SortingVisualizer; "
        "assert list(SortingVisualizer(bubble_sort([2,1])))[-1].values == (1,2); "
        "assert quickselect([2,1], 1) == 1; assert 'streamlit' not in sys.modules"
    )
    subprocess.run([sys.executable, "-S", "-c", script], check=True, capture_output=True)
