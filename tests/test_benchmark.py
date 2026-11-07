"""Real small measurements, reproducibility metadata, guards, and CSV integrity."""

from copy import deepcopy
from dataclasses import replace
from pathlib import Path
import tracemalloc

import pytest

import performance.benchmark as benchmark
from performance.benchmark import BenchmarkConfig, dataset, load_rows, rows_to_csv, run_benchmarks, save_run, validate_rows
from performance.metrics import measure_allocations, measure_time


def test_datasets_are_seeded_with_documented_patterns():
    values = dataset(30, "random", 506)
    assert values == dataset(30, "random", 506)
    assert values != dataset(30, "random", 507)
    assert dataset(30, "sorted", 506) == sorted(values)
    assert dataset(30, "reverse", 506) == sorted(values, reverse=True)
    assert set(dataset(30, "duplicates", 506)) <= set(range(-3, 4))


def test_actual_measurements_separate_time_from_memory_and_cleanup_failures():
    result, elapsed = measure_time(lambda: [1] * 100)
    assert len(result) == 100 and elapsed >= 0
    result, peak = measure_allocations(lambda: [1] * 100)
    assert len(result) == 100 and peak > 0 and not tracemalloc.is_tracing()
    with pytest.raises(ZeroDivisionError):
        measure_allocations(lambda: 1 / 0)
    assert not tracemalloc.is_tracing()
    tracemalloc.start()
    try:
        with pytest.raises(RuntimeError, match="already active"):
            measure_allocations(lambda: [])
        assert tracemalloc.is_tracing()
    finally:
        tracemalloc.stop()


def test_all_workloads_produce_checked_numeric_rows_and_roundtrip(tmp_path):
    run = run_benchmarks(BenchmarkConfig(sizes=(10,), patterns=("random",), trials=2))
    assert len(run.rows) == 8 * 2 * 2
    assert {r["algorithm_or_structure"] for r in run.rows} == set(benchmark.OPERATIONS)
    for row in run.rows:
        assert row["status"] == "ok" and row["python_version"] and row["source_digest"]
        if row["measurement"] == "timing":
            assert row["elapsed_ms"] >= 0 and row["peak_tracemalloc_bytes"] is None
        else:
            assert row["elapsed_ms"] is None and row["peak_tracemalloc_bytes"] >= 0
        if row["algorithm_or_structure"] != "bubble_sort":
            assert row["comparisons"] is None and row["swaps"] is None
    path = tmp_path / "observations.csv"
    save_run(run, path)
    assert load_rows(path) == run.rows
    assert path.with_suffix(".environment.json").is_file()
    assert path.read_text(encoding="utf-8") == rows_to_csv(run.rows)


def test_guarded_cases_have_no_fabricated_measurements():
    run = run_benchmarks(BenchmarkConfig(sizes=(5000,), patterns=("reverse",), algorithms=("bubble_sort",), include_structures=False))
    assert len(run.rows) == 1
    row = run.rows[0]
    assert row["status"] == row["measurement"] == "skipped"
    assert row["trial"] == 0 and row["notes"]
    assert row["elapsed_ms"] is row["peak_tracemalloc_bytes"] is None


def test_each_trial_is_checked_not_just_warmup(monkeypatch):
    calls = 0
    real = benchmark.quickselect

    def corrupt_after_first(values, k, **kwargs):
        nonlocal calls
        calls += 1
        return real(values, k, **kwargs) if calls == 1 else object()

    monkeypatch.setattr(benchmark, "quickselect", corrupt_after_first)
    with pytest.raises(ValueError, match="Correctness check failed"):
        run_benchmarks(BenchmarkConfig(sizes=(10,), patterns=("random",), trials=2,
                                      algorithms=("quickselect",), include_structures=False, warmup=False))
    assert calls == 2 and not tracemalloc.is_tracing()


@pytest.mark.parametrize("config", [
    replace(BenchmarkConfig(), sizes=()), replace(BenchmarkConfig(), sizes=(0,)),
    replace(BenchmarkConfig(), sizes=(10, 10)), replace(BenchmarkConfig(), sizes=(True,)),
    replace(BenchmarkConfig(), patterns=("unknown",)), replace(BenchmarkConfig(), trials=0),
    replace(BenchmarkConfig(), seed=True), replace(BenchmarkConfig(), algorithms=(), include_structures=False),
])
def test_invalid_configuration_is_rejected_before_measurement(config):
    with pytest.raises((TypeError, ValueError)):
        run_benchmarks(config)


@pytest.mark.parametrize("field,value", [("elapsed_ms", -1), ("elapsed_ms", float("nan")), ("elapsed_ms", float("inf")), ("peak_tracemalloc_bytes", 1)])
def test_invalid_or_mixed_measurement_cells_are_rejected(field, value):
    rows = run_benchmarks(BenchmarkConfig(sizes=(2,), patterns=("random",), trials=1,
                                        algorithms=("quickselect",), include_structures=False, warmup=False)).rows
    bad = deepcopy(rows)
    bad[0][field] = value
    with pytest.raises(ValueError, match="measurement"):
        validate_rows(bad)


def test_csv_with_missing_schema_is_rejected(tmp_path):
    path = tmp_path / "bad.csv"
    path.write_text("value\n1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="schema"):
        load_rows(path)
