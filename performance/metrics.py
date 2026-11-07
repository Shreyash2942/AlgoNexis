"""Separate operation timing and incremental Python allocation measurements."""

from collections.abc import Callable
from threading import Lock
from time import perf_counter_ns
import tracemalloc
from typing import Any

_MEASUREMENT_LOCK = Lock()


def measure_time(operation: Callable[[], Any]) -> tuple[Any, float]:
    """Time only the operation; callers build fixtures/check results outside."""
    with _MEASUREMENT_LOCK:
        start = perf_counter_ns()
        result = operation()
        elapsed_ms = (perf_counter_ns() - start) / 1_000_000
    return result, elapsed_ms


def measure_allocations(operation: Callable[[], Any]) -> tuple[Any, int]:
    """Peak Python-tracked bytes allocated during the operation, including output.

    Prebuilt input/structure fixtures are excluded. Tracing is process-wide;
    unrelated threads may still contribute. Existing tracing is never stopped
    or reset by this function; it is rejected explicitly.
    """
    with _MEASUREMENT_LOCK:
        if tracemalloc.is_tracing():
            raise RuntimeError("Allocation tracing is already active; stop it before starting this measurement.")
        tracemalloc.start()
        try:
            result = operation()
            _, peak = tracemalloc.get_traced_memory()
        finally:
            tracemalloc.stop()
    return result, peak
