"""Tables use the same observations as CSV; UI measurements save to test storage."""

from pathlib import Path
from statistics import mean

from streamlit.testing.v1 import AppTest

from performance.benchmark import BenchmarkConfig, load_rows, run_benchmarks, save_run
from performance.summary import summarize
import ui.performance_view as view


def test_summaries_match_real_repeats_and_never_mix_units():
    run = run_benchmarks(BenchmarkConfig(sizes=(4,), patterns=("random",), trials=2, include_structures=False))
    summaries = summarize(run.rows)
    assert len(summaries) == 4
    for summary in summaries:
        rows = [row for row in run.rows if row["algorithm_or_structure"] == summary["algorithm_or_structure"] and row["measurement"] == summary["measurement"]]
        field = "elapsed_ms" if summary["measurement"] == "timing" else "peak_tracemalloc_bytes"
        assert summary["mean"] == mean(row[field] for row in rows)
        assert summary["trials"] == 2
        assert summary["minimum"] <= summary["median"] <= summary["maximum"]
    skipped = run_benchmarks(BenchmarkConfig(sizes=(5000,), patterns=("reverse",), algorithms=("bubble_sort",), include_structures=False))
    assert summarize(skipped.rows) == []


def test_performance_ui_saves_actual_rows_and_renders_download_and_charts(tmp_path, monkeypatch):
    path = tmp_path / "benchmark_results.csv"
    monkeypatch.setattr(view, "RESULTS_PATH", path)
    app = AppTest.from_file(Path(__file__).resolve().parents[1] / "app.py", default_timeout=30).run()
    app.radio(key="navigation").set_value("Performance Analysis").run()
    app.multiselect(key="benchmark_sizes").set_value([10]).run()
    app.multiselect(key="benchmark_patterns").set_value(["random"]).run()
    app.multiselect(key="benchmark_algorithms").set_value(["quickselect"]).run()
    app.checkbox(key="benchmark_structures").uncheck().run()
    app.button(key="run_benchmarks").click().run()
    assert not app.exception
    assert len(load_rows(path)) == 10
    assert load_rows(path) == app.session_state["benchmark_rows"]
    assert app.get("download_button") and len(app.get("vega_lite_chart")) == 2
    app.multiselect(key="benchmark_sizes").set_value([]).run()
    app.button(key="run_benchmarks").click().run()
    assert app.error and len(load_rows(path)) == 10 and not app.exception
