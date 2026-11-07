"""Measured tables, separate-unit charts, and full-run CSV export."""

from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

from performance.benchmark import ALGORITHMS, PATTERNS, BenchmarkConfig, load_rows, rows_to_csv, run_benchmarks, save_run
from performance.summary import summarize

RESULTS_PATH = Path(__file__).resolve().parents[1] / "results/benchmark_results.csv"
WORKLOADS = {"bubble_sort": "Bubble Sort · sort all", "quickselect": "Quickselect · select middle",
             "custom_set": "Set · membership probes", "stack": "Stack · pop all", "queue": "Queue · dequeue all",
             "bst": "BST · search all", "hash_table": "Hash Table · find all", "graph": "Graph · path BFS"}


def _chart(frame: pd.DataFrame, measurement: str, title: str):
    selected = frame[frame["measurement"] == measurement]
    if selected.empty:
        st.info("No measured observations match these filters.")
        return
    chart = alt.Chart(selected).mark_line(point=True).encode(
        x=alt.X("input_size:Q", title="Input size", scale=alt.Scale(type="log", base=10)),
        y=alt.Y("mean:Q", title=title, scale=alt.Scale(zero=True)),
        color=alt.Color("Workload:N", legend=alt.Legend(orient="bottom")),
        tooltip=["Workload:N", "input_size:Q", "trials:Q", "mean:Q", "median:Q", "minimum:Q", "maximum:Q"],
    ).properties(height=320)
    st.altair_chart(chart, width="stretch", alt=title + " by input size and workload")


def render() -> None:
    st.title("Performance Analysis")
    st.write("Measure real operations, inspect repeated trials, and export the evidence.")
    st.info("Bubble Sort sorts a complete list; Quickselect selects one rank. Structure operations also differ. Compare scaling and trade-offs, not different tasks as replacements.")
    with st.expander("Run a reproducible benchmark", expanded=False):
        first, second = st.columns(2)
        sizes = first.multiselect("Dataset sizes", [10, 100, 1000, 5000], default=[10, 100, 1000, 5000], key="benchmark_sizes")
        patterns = second.multiselect("Input patterns", list(PATTERNS), default=list(PATTERNS), key="benchmark_patterns")
        algorithms = first.multiselect("Algorithms to measure", list(ALGORITHMS), default=list(ALGORITHMS), key="benchmark_algorithms")
        structures = second.checkbox("Include all six data structures", value=True, key="benchmark_structures")
        trials = first.number_input("Trials per measurement kind", min_value=5, max_value=10, value=5, step=1, key="benchmark_trials")
        seed = second.number_input("Dataset seed", min_value=0, max_value=2**32 - 1, value=506, step=1, key="benchmark_seed")
        st.caption("Timing and allocation trials run separately. Bubble Sort/BST cases above 1,000 values are recorded as skipped. A run replaces the saved CSV after correctness checks pass.")
        if st.button("Run benchmarks", key="run_benchmarks", type="primary"):
            try:
                bar = st.progress(0.0)
                with st.spinner("Measuring core operations…"):
                    run = run_benchmarks(BenchmarkConfig(sizes=tuple(sizes), patterns=tuple(patterns), trials=int(trials),
                                                       seed=int(seed), algorithms=tuple(algorithms), include_structures=structures),
                                         progress=lambda done, total: bar.progress(done / total))
                    save_run(run, RESULTS_PATH)
                st.session_state["benchmark_rows"] = run.rows
                st.success(f"Saved {run.metadata['observed_rows']:,} measured observations.")
            except (TypeError, ValueError, RuntimeError, OSError) as error:
                st.error(f"Benchmark could not be completed: {error}")

    if st.session_state["benchmark_rows"] is None and RESULTS_PATH.exists():
        try:
            st.session_state["benchmark_rows"] = load_rows(RESULTS_PATH)
        except (ValueError, OSError) as error:
            st.error(f"Cannot load saved measurements: {error}")
    rows = st.session_state["benchmark_rows"]
    if not rows:
        st.info("Run a benchmark to create measured tables, charts, and a CSV download.")
        return
    observed = [row for row in rows if row["status"] == "ok"]
    skipped = [row for row in rows if row["status"] == "skipped"]
    a, b, c = st.columns(3)
    a.metric("Measured observations", len(observed))
    b.metric("Guarded cases", len(skipped))
    c.metric("Measurement kinds", 2 if observed else 0)
    st.caption(f"Showing saved run {rows[0]['run_id'][:8]} · seed {rows[0]['seed']} · recorded {rows[0]['timestamp']} (UTC). Changing controls above does not relabel these observations.")
    st.download_button("Download full run CSV", rows_to_csv(rows).encode("utf-8"), file_name="benchmark_results.csv",
                       mime="text/csv", key="download_benchmarks")
    summaries = summarize(rows)
    if not summaries:
        st.info("All selected cases were guarded; no zero values are substituted for missing measurements.")
        return
    frame = pd.DataFrame(summaries)
    frame["Workload"] = frame["algorithm_or_structure"].map(WORKLOADS)
    present = [p for p in (*PATTERNS, "path") if p in frame["input_pattern"].values]
    pattern = st.selectbox("Chart input pattern", present, key="chart_pattern")
    filtered = frame[frame["input_pattern"] == pattern]
    selected = st.multiselect("Chart workloads", list(filtered["Workload"].unique()),
                             default=list(filtered["Workload"].unique()), key=f"chart_workloads_{pattern}")
    filtered = filtered[filtered["Workload"].isin(selected)]
    time_column, memory_column = st.columns(2)
    with time_column:
        st.subheader("Execution time")
        _chart(filtered, "timing", "Mean elapsed time (ms)")
    with memory_column:
        st.subheader("Python-tracked allocations")
        _chart(filtered, "memory", "Mean peak Python-tracked bytes")
    st.caption("Peak allocations during the operation include outputs and exclude prebuilt inputs/fixtures. This is not total RAM or whole-structure storage; timing runs are not traced. Hash-table benchmarks use capacity max(8, 2 × n).")
    st.subheader("Observed repeat summaries")
    st.caption("Mean/median and observed min/max are grouped by workload, size, pattern, and measurement kind. Min/max are not confidence intervals.")
    st.dataframe(filtered[["Workload", "input_size", "measurement", "trials", "mean", "median", "minimum", "maximum", "unit"]], hide_index=True)
    counts = [r for r in observed if r["algorithm_or_structure"] == "bubble_sort" and r["measurement"] == "timing" and r["input_pattern"] == pattern]
    if counts:
        st.subheader("Bubble Sort operation counts")
        st.dataframe(pd.DataFrame(counts)[["input_size", "trial", "comparisons", "swaps"]], hide_index=True)
    if skipped:
        with st.expander("Skipped cases and reasons"):
            st.dataframe(pd.DataFrame(skipped)[["algorithm_or_structure", "input_size", "input_pattern", "notes"]], hide_index=True)
