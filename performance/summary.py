"""Aggregate observed repeats without mixing measurement units or skipped cases."""

from collections import defaultdict
from statistics import mean, median

from performance.benchmark import validate_rows


def summarize(rows: list[dict]) -> list[dict]:
    validate_rows(rows)
    groups = defaultdict(list)
    for row in rows:
        if row["status"] != "ok":
            continue
        key = (row["run_id"], row["algorithm_or_structure"], row["operation"], row["input_size"],
               row["input_pattern"], row["measurement"], row["hash_capacity"])
        field = "elapsed_ms" if row["measurement"] == "timing" else "peak_tracemalloc_bytes"
        groups[key].append(row[field])
    result = []
    for key, values in groups.items():
        run_id, implementation, operation, size, pattern, measurement, capacity = key
        result.append({"run_id": run_id, "algorithm_or_structure": implementation, "operation": operation,
                       "input_size": size, "input_pattern": pattern, "measurement": measurement,
                       "hash_capacity": capacity, "trials": len(values), "mean": mean(values),
                       "median": median(values), "minimum": min(values), "maximum": max(values),
                       "unit": "ms" if measurement == "timing" else "Python-tracked bytes"})
    return result
