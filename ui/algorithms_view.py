"""Algorithm controls call core APIs and retain independent result state."""

from random import Random

import streamlit as st

from algorithms.bubble_sort import bubble_sort
from algorithms.quickselect import quickselect
from ui.inputs import parse_integer_list
from ui.state import update_dataset

SAMPLES = {
    "Mixed": "5, 1, 4, 2, 8",
    "Sorted": "1, 2, 3, 4, 5",
    "Reverse sorted": "5, 4, 3, 2, 1",
    "Duplicates and negatives": "3, -1, 3, 0, -1",
    "Empty": "",
}


def _load_sample() -> None:
    text = SAMPLES[st.session_state["sample_dataset"]]
    st.session_state["dataset_widget"] = text
    update_dataset(st.session_state, text)


def render() -> None:
    st.title("Algorithms")
    st.write("Use one dataset to explore a complete sort or a single ranked value.")
    sample, load = st.columns([3, 1])
    sample.selectbox("Sample dataset", list(SAMPLES), key="sample_dataset")
    load.button("Load sample", on_click=_load_sample, key="load_sample")
    if "dataset_widget" not in st.session_state:
        st.session_state["dataset_widget"] = st.session_state["dataset_text"]
    text = st.text_area("Integer dataset", key="dataset_widget", height=100,
                        help="Comma- or whitespace-separated integers; no decimals, brackets, or code.")
    update_dataset(st.session_state, text)
    values = None
    try:
        values = parse_integer_list(text)
        st.caption(f"{len(values):,} values. Values are limited to +/- 1 billion; selection supports up to 5,000 values.")
    except (TypeError, ValueError) as error:
        st.error(str(error))

    left, right = st.columns(2)
    with left.container(border=True):
        st.subheader("Bubble Sort")
        st.caption("Adjacent comparisons, swaps, and an early exit when a pass makes no swaps.")
        trace = st.checkbox("Record sorting steps (up to 50 values)", value=True, key="trace_enabled")
        if st.button("Run Bubble Sort", key="run_bubble", type="primary", disabled=values is None):
            if len(values) > (50 if trace else 1000):
                st.error("Use at most 50 values with visualization, or 1,000 with step recording disabled.")
            else:
                st.session_state["bubble_result"] = bubble_sort(values, track_steps=trace)
                st.session_state["bubble_input"] = tuple(values)
                st.session_state["frame_index"] = 0
        result = st.session_state["bubble_result"]
        if result is not None:
            st.write("Original values", list(st.session_state["bubble_input"]))
            st.write("Sorted values", list(result.sorted_values))
            comparisons, swaps = st.columns(2)
            comparisons.metric("Comparisons", result.comparisons)
            swaps.metric("Swaps", result.swaps)
        st.caption("Without tracing: best O(n), average/worst O(n squared). Full snapshots can cost O(n cubed) storage.")

    with right.container(border=True):
        st.subheader("Quickselect")
        st.caption("One-based ranks count duplicates. Randomized partitions avoid sorting the full list.")
        if "quick_k_widget" not in st.session_state:
            st.session_state["quick_k_widget"] = st.session_state["quick_rank"]
        k = st.number_input("Rank k (1-based)", min_value=1, max_value=5000, step=1, key="quick_k_widget")
        if k != st.session_state["quick_rank"]:
            st.session_state["quick_rank"] = k
            st.session_state["quick_result"] = None
        if st.button("Run Quickselect", key="run_quick", type="primary", disabled=values is None):
            try:
                answer = quickselect(values, int(k), rng=Random(506))
                st.session_state["quick_result"] = {"k": int(k), "value": answer}
            except (TypeError, ValueError) as error:
                st.error(str(error))
        selected = st.session_state["quick_result"]
        if selected is not None:
            st.metric(f"Rank {selected['k']} value", selected["value"])
        st.caption("Expected O(n), worst O(n squared); input-copy space O(n). Pivot seed: 506.")

    if result is not None and result.steps:
        from ui.sorting_view import render as render_sorting
        render_sorting(result)
    elif result is not None:
        st.info("Step recording was disabled for this run. Enable it and use at most 50 values to visualize every event.")
