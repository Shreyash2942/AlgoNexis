"""Local AlgoNexis portfolio. Launch with python -m streamlit run app.py."""

import streamlit as st

from ui.state import initialize


def main() -> None:
    st.set_page_config(page_title="AlgoNexis | Algorithm Lab", page_icon="◈", layout="wide")
    initialize(st.session_state)
    with st.sidebar:
        st.title("AlgoNexis")
        st.caption("ALGORITHMS & DATA STRUCTURES")
        page = st.radio("Explore", ["Dashboard", "Algorithms", "Data Structures", "Performance Analysis"], key="navigation")
        st.divider()
        st.caption("Explore a method, inspect its behavior, then measure its costs.")
    if page == "Dashboard":
        st.caption("THE ALGORITHM LAB")
        st.title("Understand the steps. Measure the trade-offs.")
        st.write("An interactive workspace for sorting, selection, and fundamental data structures.")
        for column, label, value in zip(st.columns(3), ["Algorithms", "Data structures", "Input patterns"], [2, 6, 4]):
            column.metric(label, value)
        left, right = st.columns(2)
        with left.container(border=True):
            st.subheader("Explore algorithms")
            st.write("Follow Bubble Sort comparisons and swaps, or find one ranked value with Quickselect.")
        with right.container(border=True):
            st.subheader("Build and inspect")
            st.write("Work with sets, stacks, queues, trees, graphs, and collision chains. State persists as you navigate.")
        st.info("Bubble Sort orders a complete list. Quickselect finds one rank. Their measurements describe different tasks.")
    elif page == "Algorithms":
        from ui.algorithms_view import render
        render()
    elif page == "Data Structures":
        from ui.structures_view import render
        render()
    else:
        from ui.performance_view import render
        render()


if __name__ == "__main__":
    main()
