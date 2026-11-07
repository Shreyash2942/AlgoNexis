"""Session model independent of Streamlit, with explicit reset boundaries."""

from collections.abc import MutableMapping
from typing import Any

from data_structures.manager import DataStructureManager


def initialize(state: MutableMapping[str, Any]) -> None:
    defaults = {
        "dataset_text": "5, 1, 4, 2, 8", "bubble_result": None,
        "bubble_input": None, "quick_result": None, "quick_rank": 1,
        "frame_index": 0, "structure_result": None, "benchmark_rows": None,
    }
    for key, value in defaults.items():
        if key not in state:
            state[key] = value
    if "manager" not in state:
        state["manager"] = DataStructureManager()


def update_dataset(state: MutableMapping[str, Any], text: str) -> None:
    if state["dataset_text"] != text:
        state["dataset_text"] = text
        state["bubble_result"] = state["bubble_input"] = state["quick_result"] = None
        state["frame_index"] = 0


def reset_structures(state: MutableMapping[str, Any]) -> None:
    state["manager"] = DataStructureManager()
    state["structure_result"] = None
