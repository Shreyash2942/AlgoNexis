"""Display complete immutable traces with a persistent model playback index."""

import altair as alt
import pandas as pd
import streamlit as st

from visualization.sorting_visualizer import SortingVisualizer


def _move(delta: int, total: int) -> None:
    st.session_state["frame_index"] = max(0, min(total - 1, st.session_state["frame_index"] + delta))


def _reset() -> None:
    st.session_state["frame_index"] = 0


def _select() -> None:
    st.session_state["frame_index"] = st.session_state["frame_slider"]


def render(result) -> None:
    view = SortingVisualizer(result)
    st.subheader("Sorting, one event at a time")
    st.session_state["frame_index"] = min(st.session_state["frame_index"], view.total_steps - 1)
    previous, next_step, reset, position = st.columns([1, 1, 1, 3])
    previous.button("Previous", key="previous_step", disabled=st.session_state["frame_index"] == 0,
                    on_click=_move, args=(-1, view.total_steps))
    next_step.button("Next", key="next_step", disabled=st.session_state["frame_index"] == view.total_steps - 1,
                     on_click=_move, args=(1, view.total_steps))
    reset.button("Reset steps", key="reset_steps", on_click=_reset)
    st.session_state["frame_slider"] = st.session_state["frame_index"]
    position.slider("Step index (zero-based)", 0, view.total_steps - 1, key="frame_slider", on_change=_select)
    frame = view.get_step(st.session_state["frame_index"])
    st.caption(f"Step {frame.step_index + 1} of {frame.total_steps} | {frame.event.upper()}")
    st.write(frame.description)
    st.caption(f"{frame.comparisons} comparisons · {frame.swaps} swaps so far")
    if frame.values:
        rows = [{"Index": index, "Value": value,
                 "State": ("Swap" if frame.swapped else "Compare") if index in frame.highlighted_indices else "Other"}
                for index, value in enumerate(frame.values)]
        chart = alt.Chart(pd.DataFrame(rows)).mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3).encode(
            x=alt.X("Index:O", sort=None, title="List index"),
            y=alt.Y("Value:Q", title="Integer value"),
            color=alt.Color("State:N", scale=alt.Scale(domain=["Other", "Compare", "Swap"],
                             range=["#94A3B8", "#D97706", "#0F766E"]), title="Active event"),
            tooltip=["Index:O", "Value:Q", "State:N"],
        ).properties(height=300)
        st.altair_chart(chart, width="stretch", alt=f"{frame.event} state: {list(frame.values)}")
    else:
        st.info("Empty input: there are no bars. Initial and final states are still recorded.")
    st.write("Current values", list(frame.values))
    st.caption("Amber marks a comparison; teal marks the completed swap. Negative values extend below zero. No recorded events are dropped.")
