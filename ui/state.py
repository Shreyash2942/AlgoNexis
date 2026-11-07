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


def execute_structure(state: MutableMapping[str, Any], name: str, operation: str, **kwargs: Any) -> Any:
    """Apply UI growth limits before invoking the manager's domain validation."""
    manager = state["manager"]
    size = manager.execute(name, "size")
    growth = 0
    if name in ("stack", "queue") and operation in ("push", "enqueue"):
        growth = 1
    elif name == "set" and operation == "add":
        growth = int(not manager.execute(name, "contains", value=kwargs["value"]))
    elif name == "tree" and operation == "insert":
        growth = int(not manager.execute(name, "search", value=kwargs["value"]))
    elif name == "hash_table" and operation == "insert":
        growth = int(not manager.execute(name, "contains", key=kwargs["key"]))
    elif name == "graph" and operation in ("add_vertex", "add_edge"):
        vertices = manager.execute(name, "vertices")
        proposed = [kwargs["vertex"]] if operation == "add_vertex" else [kwargs["source"], kwargs["target"]]
        growth = len({v for v in proposed if v not in vertices})
    if size + growth > 200:
        raise ValueError("This interactive structure is limited to 200 items. Remove items or reset the structures.")
    result = manager.execute(name, operation, **kwargs)
    state["structure_result"] = {"structure": name, "operation": operation, "result": result}
    return result
