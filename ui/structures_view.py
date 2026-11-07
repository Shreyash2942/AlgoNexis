"""Integer-oriented controls for every allowlisted structure operation."""

import streamlit as st

from ui.inputs import parse_integer, parse_integer_list
from ui.state import execute_structure, reset_structures

NAMES = {"set": "Custom Set", "stack": "Stack", "queue": "Queue", "tree": "Binary Search Tree",
         "graph": "Graph", "hash_table": "Hash Table"}
DESCRIPTIONS = {
    "set": "Unique members. Derived operations return a new set and preserve the stored set.",
    "stack": "Last in, first out. Contents are shown from bottom to top.",
    "queue": "First in, first out. Contents are shown from front to rear.",
    "tree": "An unbalanced integer BST. Duplicate insertions are ignored; display uses inorder.",
    "graph": "An undirected, unweighted graph. Traversal follows neighbor insertion order within the reachable component.",
    "hash_table": "Separate chaining keeps colliding keys distinct. Capacity is fixed at 8; contents follow bucket order.",
}


def _reset() -> None:
    reset_structures(st.session_state)


def _arguments(name: str, operation: str) -> dict:
    if operation in ("union", "intersection", "difference", "symmetric_difference"):
        return {"values": parse_integer_list(st.session_state["other_set"], limit=200)}
    if name == "hash_table" and operation in ("insert", "find", "delete", "contains"):
        args = {"key": parse_integer(st.session_state["table_key"])}
        if operation == "insert":
            args["value"] = st.session_state["table_value"]
        return args
    if name == "graph":
        if operation == "add_edge":
            return {"source": parse_integer(st.session_state["graph_source"]),
                    "target": parse_integer(st.session_state["graph_target"])}
        if operation in ("add_vertex", "bfs", "dfs"):
            return {"vertex" if operation == "add_vertex" else "start": parse_integer(st.session_state["graph_vertex"])}
    if operation in ("add", "remove", "discard", "contains", "push", "enqueue", "insert", "search"):
        return {"value": parse_integer(st.session_state["structure_value"])}
    return {}


def render() -> None:
    st.title("Data Structures")
    st.write("Build state, run an operation, and inspect what changed.")
    manager = st.session_state["manager"]
    name = st.selectbox("Structure", list(NAMES), format_func=NAMES.get, key="structure_widget")
    st.caption(DESCRIPTIONS[name])
    controls, contents = st.columns(2)
    with controls.container(border=True):
        operation = st.selectbox("Operation", manager.available_operations()[name],
                                 format_func=lambda value: value.replace("_", " ").title(), key=f"operation_{name}")
        if operation in ("union", "intersection", "difference", "symmetric_difference"):
            st.text_area("Other set values", "2, 3", key="other_set")
        elif name == "hash_table" and operation in ("insert", "find", "delete", "contains"):
            st.text_input("Integer key", "0", key="table_key")
            if operation == "insert":
                st.text_input("Stored text value", "value", key="table_value")
        elif name == "graph" and operation == "add_edge":
            st.text_input("Source vertex", "0", key="graph_source")
            st.text_input("Target vertex", "1", key="graph_target")
        elif name == "graph" and operation in ("add_vertex", "bfs", "dfs"):
            st.text_input("Vertex" if operation == "add_vertex" else "Starting vertex", "0", key="graph_vertex")
        elif operation in ("add", "remove", "discard", "contains", "push", "enqueue", "insert", "search"):
            st.text_input("Integer value", "0", key="structure_value")
        if st.button("Run operation", key="run_structure", type="primary"):
            try:
                execute_structure(st.session_state, name, operation, **_arguments(name, operation))
                st.success("Operation completed.")
            except (TypeError, ValueError, KeyError, IndexError) as error:
                st.session_state["structure_result"] = None
                message = f"Missing member, key, or starting vertex: {error.args[0]}" if isinstance(error, KeyError) else str(error)
                st.error(message)
        last = st.session_state["structure_result"]
        if last is not None and last["structure"] == name:
            st.write(f"Result: {last['operation'].replace('_', ' ')}")
            st.json(last["result"]) if last["result"] is not None else st.write("Done; no return value.")
    with contents.container(border=True):
        st.subheader("Current contents")
        st.metric("Items", manager.execute(name, "size"))
        st.json(manager.execute(name, "display"))
        if name == "hash_table":
            st.caption(f"Load factor: {manager.execute(name, 'load_factor'):.2f}")
            st.write("Collision buckets")
            st.json(manager.execute(name, "buckets"))
    st.button("Reset all structures", key="reset_structures", on_click=_reset)
    st.caption("State persists across sections. Reset clears all six structures. Interactive structures are limited to 200 items; table values are text.")
