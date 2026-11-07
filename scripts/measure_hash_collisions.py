"""Controlled supplemental hash experiment: one bucket versus 2n buckets.

Unique nonnegative integer keys make the bucket distribution explicit. Fixture
construction is excluded; every trial finds all n keys and checks exact output.
This is separate from the portfolio's default random-key benchmark profile.
"""

from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from uuid import uuid4

from data_structures.hash_table import HashTable
from performance.benchmark import BenchmarkRun, FIELDS, ROOT, _environment, save_run
from performance.metrics import measure_allocations, measure_time


def run() -> BenchmarkRun:
    environment = _environment()
    run_id, rows = uuid4().hex, []
    for n in (10, 100, 1000):
        for capacity in (1, 2 * n):
            def prepare():
                fixture = HashTable(capacity)
                for key in range(n):
                    fixture.insert(key, key)
                return lambda: [fixture.find(key) for key in range(n)]

            expected = list(range(n))
            if prepare()() != expected:
                raise ValueError('Hash warm-up correctness failure.')
            for trial in range(1, 6):
                for kind in ('timing', 'memory'):
                    operation = prepare()
                    result, value = (measure_time(operation) if kind == 'timing'
                                     else measure_allocations(operation))
                    if result != expected:
                        raise ValueError('Hash trial correctness failure.')
                    row = dict.fromkeys(FIELDS)
                    row.update({k: environment[k] for k in ('python_version', 'platform', 'processor',
                               'implementation_revision', 'source_digest')})
                    row.update(timestamp=datetime.now(timezone.utc).isoformat(), run_id=run_id,
                               algorithm_or_structure='hash_table', operation='find_all', input_size=n,
                               input_pattern='unique_integer_keys', trial=trial, measurement=kind,
                               seed=506, fixture_items=n, hash_capacity=capacity, status='ok',
                               notes='Controlled capacity profile; prebuilt fixture excluded; output list included.')
                    row['elapsed_ms' if kind == 'timing' else 'peak_tracemalloc_bytes'] = value
                    rows.append(row)
    return BenchmarkRun(rows, {**environment, 'run_id': run_id, 'observed_rows': len(rows),
                              'config': {'sizes': [10, 100, 1000], 'trials': 5,
                                         'capacities': '1 versus 2*n', 'keys': 'range(n)'},
                              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest()})


if __name__ == '__main__':
    result = run()
    save_run(result, ROOT / 'results/hash_collision_results.csv')
    print(f'Saved {len(result.rows)} verified supplemental observations.')
