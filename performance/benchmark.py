"""Reproducible, correctness-checked microbenchmarks independent of Streamlit.

Timing and allocation trials are separate, with fresh prebuilt fixtures. Dataset
generation, fixture construction, expected results, validation, and export are
outside measurement. Result-list construction inside an operation is included.
Bubble Sort and unbalanced-BST cases above 1,000 values are explicitly skipped.
"""

from collections.abc import Callable
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from hashlib import sha256
from importlib.metadata import PackageNotFoundError, version
import argparse
import csv
import io
import json
import math
import os
from pathlib import Path
import platform
from random import Random
import subprocess
import tempfile
from typing import Any
from uuid import uuid4

from algorithms.bubble_sort import bubble_sort
from algorithms.quickselect import quickselect
from data_structures.custom_set import CustomSet
from data_structures.graph import Graph
from data_structures.hash_table import HashTable
from data_structures.queue import Queue
from data_structures.stack import Stack
from data_structures.tree import BinarySearchTree
from performance.metrics import measure_allocations, measure_time

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = ("random", "sorted", "reverse", "duplicates")
ALGORITHMS = ("bubble_sort", "quickselect")
STRUCTURES = ("custom_set", "stack", "queue", "bst", "hash_table")
OPERATIONS = {"bubble_sort": "sort", "quickselect": "select_middle", "custom_set": "contains_all",
              "stack": "pop_all", "queue": "dequeue_all", "bst": "search_all",
              "hash_table": "find_all", "graph": "bfs_path"}
FIELDS = ("timestamp", "run_id", "algorithm_or_structure", "operation", "input_size", "input_pattern",
          "trial", "measurement", "elapsed_ms", "peak_tracemalloc_bytes", "seed", "pivot_seed", "k",
          "comparisons", "swaps", "fixture_items", "hash_capacity", "python_version", "platform",
          "processor", "implementation_revision", "source_digest", "status", "notes")
INT_FIELDS = ("input_size", "trial", "peak_tracemalloc_bytes", "seed", "pivot_seed", "k", "comparisons",
              "swaps", "fixture_items", "hash_capacity")


@dataclass(frozen=True)
class BenchmarkConfig:
    sizes: tuple[int, ...] = (10, 100, 1000, 5000)
    patterns: tuple[str, ...] = PATTERNS
    trials: int = 5
    seed: int = 506
    algorithms: tuple[str, ...] = ALGORITHMS
    include_structures: bool = True
    warmup: bool = True


@dataclass
class BenchmarkRun:
    rows: list[dict[str, Any]]
    metadata: dict[str, Any]


def _validate_config(config: BenchmarkConfig) -> None:
    if not config.sizes or len(config.sizes) > 4 or len(set(config.sizes)) != len(config.sizes):
        raise ValueError("Choose one to four distinct dataset sizes.")
    if any(type(n) is not int or not 1 <= n <= 5000 for n in config.sizes):
        raise ValueError("Dataset sizes must be integers from 1 through 5,000.")
    if not config.patterns or len(set(config.patterns)) != len(config.patterns) or any(p not in PATTERNS for p in config.patterns):
        raise ValueError("Choose distinct supported input patterns.")
    if len(set(config.algorithms)) != len(config.algorithms) or any(a not in ALGORITHMS for a in config.algorithms):
        raise ValueError("Unknown or repeated algorithm.")
    if type(config.trials) is not int or not 1 <= config.trials <= 10:
        raise ValueError("Use one through ten trials (five recommended).")
    if type(config.seed) is not int or not 0 <= config.seed <= 2**32 - 1:
        raise ValueError("Seed must be an integer from 0 through 2**32 - 1.")
    if type(config.include_structures) is not bool or type(config.warmup) is not bool:
        raise TypeError("Benchmark flags must be booleans.")
    if not config.algorithms and not config.include_structures:
        raise ValueError("Select at least one workload.")


def dataset(size: int, pattern: str, seed: int) -> list[int]:
    rng = Random(seed)
    if pattern == "duplicates":
        return [rng.randint(-3, 3) for _ in range(size)]
    if pattern not in PATTERNS:
        raise ValueError("Unknown input pattern.")
    values = [rng.randint(-10000, 10000) for _ in range(size)]
    return sorted(values, reverse=pattern == "reverse") if pattern != "random" else values


def _environment() -> dict[str, Any]:
    sources = {p.relative_to(ROOT).as_posix(): sha256(p.read_bytes()).hexdigest()
               for folder in ("algorithms", "data_structures", "performance")
               for p in sorted((ROOT / folder).glob("*.py"))}
    try:
        revision = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, check=True,
                                  capture_output=True, text=True, encoding="utf-8").stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        revision = "unavailable"
    packages = {}
    for name in ("streamlit", "pytest", "altair", "pandas"):
        try:
            packages[name] = version(name)
        except PackageNotFoundError:
            packages[name] = "not installed"
    return {"python_version": platform.python_version(), "platform": platform.platform(),
            "processor": platform.processor() or "unavailable", "implementation_revision": revision,
            "source_digest": sha256(json.dumps(sources, sort_keys=True).encode()).hexdigest(),
            "source_sha256": sources, "package_versions": packages}


def _prepare(name: str, values: list[int], pivot_seed: int) -> tuple[Callable, Callable, int | None]:
    """Return operation, external correctness checker, and prebuilt fixture size."""
    original = values.copy()
    if name == "bubble_sort":
        expected = tuple(sorted(values))
        return (lambda: bubble_sort(values, track_steps=False),
                lambda result: result.sorted_values == expected and values == original, None)
    if name == "quickselect":
        k, rng = (len(values) + 1) // 2, Random(pivot_seed)
        expected = sorted(values)[k - 1]
        return lambda: quickselect(values, k, rng=rng), lambda result: result == expected and values == original, None
    if name == "custom_set":
        fixture = CustomSet(values)
        return lambda: [fixture.contains(v) for v in values], lambda result: result == [True] * len(values), len(fixture)
    if name == "stack":
        fixture = Stack(values)
        return lambda: [fixture.pop() for _ in values], lambda result: result == original[::-1] and fixture.is_empty(), len(fixture)
    if name == "queue":
        fixture = Queue(values)
        return lambda: [fixture.dequeue() for _ in values], lambda result: result == original and fixture.is_empty(), len(fixture)
    if name == "bst":
        fixture = BinarySearchTree(values)
        return lambda: [fixture.search(v) for v in values], lambda result: result == [True] * len(values), len(fixture)
    if name == "hash_table":
        fixture = HashTable(max(8, 2 * len(values)))
        for value in values:
            fixture.insert(value, value)
        return lambda: [fixture.find(v) for v in values], lambda result: result == original, len(fixture)
    if name == "graph":
        fixture = Graph()
        fixture.add_vertex(0)
        for vertex in range(1, len(values)):
            fixture.add_edge(vertex - 1, vertex)
        return lambda: fixture.bfs(0), lambda result: result == list(range(len(values))), len(fixture)
    raise ValueError("Unknown workload.")


def run_benchmarks(config: BenchmarkConfig = BenchmarkConfig(), *, progress: Callable | None = None) -> BenchmarkRun:
    _validate_config(config)
    environment = _environment()
    run_id, rows = uuid4().hex, []
    cases = [(name, size, pattern) for size in config.sizes for pattern in config.patterns
             for name in config.algorithms + (STRUCTURES if config.include_structures else ())]
    if config.include_structures:
        cases += [("graph", size, "path") for size in config.sizes]
    for case_index, (name, size, pattern) in enumerate(cases, start=1):
        base = dict.fromkeys(FIELDS)
        base.update({key: environment[key] for key in ("python_version", "platform", "processor", "implementation_revision", "source_digest")})
        base.update(timestamp=datetime.now(timezone.utc).isoformat(), run_id=run_id,
                    algorithm_or_structure=name, operation=OPERATIONS[name], input_size=size,
                    input_pattern=pattern, seed=config.seed, k=(size + 1) // 2 if name == "quickselect" else None,
                    hash_capacity=max(8, 2 * size) if name == "hash_table" else None)
        if name in ("bubble_sort", "bst") and size > 1000:
            rows.append({**base, "trial": 0, "measurement": "skipped", "status": "skipped",
                         "notes": "Quadratic-workload guard: sizes above 1,000 excluded; no measurement taken."})
        else:
            values = list(range(size)) if name == "graph" else dataset(size, pattern, config.seed)
            if config.warmup:
                operation, check, _ = _prepare(name, values, config.seed)
                if not check(operation()):
                    raise ValueError(f"Correctness check failed for {name} warm-up.")
            for trial in range(1, config.trials + 1):
                for measurement in ("timing", "memory"):
                    pivot_seed = config.seed + trial
                    operation, check, fixture_items = _prepare(name, values, pivot_seed)
                    result, observed = measure_time(operation) if measurement == "timing" else measure_allocations(operation)
                    if not check(result):
                        raise ValueError(f"Correctness check failed for {name} {measurement} trial {trial}.")
                    row = {**base, "timestamp": datetime.now(timezone.utc).isoformat(),
                           "trial": trial, "measurement": measurement, "status": "ok",
                           "fixture_items": fixture_items, "pivot_seed": pivot_seed if name == "quickselect" else None,
                           "notes": "Fresh prebuilt fixture; setup/check excluded; operation output allocation included."}
                    row["elapsed_ms" if measurement == "timing" else "peak_tracemalloc_bytes"] = observed
                    if name == "bubble_sort":
                        row.update(comparisons=result.comparisons, swaps=result.swaps)
                    rows.append(row)
        if progress is not None:
            progress(case_index, len(cases))
    validate_rows(rows)
    return BenchmarkRun(rows, {**environment, "run_id": run_id, "config": asdict(config),
                              "observed_rows": sum(r["status"] == "ok" for r in rows),
                              "skipped_cases": sum(r["status"] == "skipped" for r in rows)})


def validate_rows(rows: list[dict]) -> None:
    if not rows:
        raise ValueError("CSV contains no observations.")
    for row in rows:
        if set(row) != set(FIELDS):
            raise ValueError("Benchmark CSV fields do not match the documented schema.")
        if type(row["input_size"]) is not int or row["input_size"] <= 0:
            raise ValueError("Invalid benchmark input size.")
        if row["status"] == "skipped":
            valid = row["measurement"] == "skipped" and row["trial"] == 0 and bool(row["notes"])
            valid = valid and row["elapsed_ms"] is None and row["peak_tracemalloc_bytes"] is None
        elif row["status"] == "ok" and type(row["trial"]) is int and row["trial"] > 0:
            if row["measurement"] == "timing":
                value = row["elapsed_ms"]
                valid = type(value) in (float, int) and math.isfinite(value) and value >= 0 and row["peak_tracemalloc_bytes"] is None
            elif row["measurement"] == "memory":
                value = row["peak_tracemalloc_bytes"]
                valid = type(value) is int and value >= 0 and row["elapsed_ms"] is None
            else:
                valid = False
        else:
            valid = False
        if not valid:
            raise ValueError("Invalid measurement row: timing, memory, and skipped observations must remain distinct.")


def rows_to_csv(rows: list[dict]) -> str:
    validate_rows(rows)
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def load_rows(path: Path) -> list[dict]:
    with Path(path).open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        for key in INT_FIELDS:
            if key in row:
                row[key] = int(row[key]) if row[key] else None
        if "elapsed_ms" in row:
            row["elapsed_ms"] = float(row["elapsed_ms"]) if row["elapsed_ms"] else None
    validate_rows(rows)
    return rows


def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="", dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(text)
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def save_run(run: BenchmarkRun, path: Path) -> None:
    path = Path(path)
    _atomic_write(path, rows_to_csv(run.rows))
    _atomic_write(path.with_suffix(".environment.json"), json.dumps(run.metadata, indent=2) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "results/benchmark_results.csv")
    parser.add_argument("--sizes", type=int, nargs="+", default=[10, 100, 1000, 5000])
    parser.add_argument("--patterns", choices=PATTERNS, nargs="+", default=list(PATTERNS))
    parser.add_argument("--trials", type=int, default=5)
    parser.add_argument("--seed", type=int, default=506)
    args = parser.parse_args()
    run = run_benchmarks(BenchmarkConfig(sizes=tuple(args.sizes), patterns=tuple(args.patterns), trials=args.trials, seed=args.seed),
                         progress=lambda done, total: print(f"Case {done}/{total} complete", flush=True) if done % 10 == 0 or done == total else None)
    save_run(run, args.output)
    print(f"Saved {run.metadata['observed_rows']} actual observations; {run.metadata['skipped_cases']} guarded cases: {args.output}")


if __name__ == "__main__":
    main()
