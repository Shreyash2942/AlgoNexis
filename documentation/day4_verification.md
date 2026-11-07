# Day 4 verification — November 7, 2026

## Regression gate (D4.1)

The original environment passed 191 existing tests before edits. Four release
evidence tests now verify the complete recorded workload and reject missing
trials, duplicate trials, and a forged source manifest. The expanded suite passed
195 tests in 6.86 seconds in the original environment, then **195 tests in 6.06
seconds** in a newly created environment with installed release dependencies.

Commands executed in the fresh environment:

```powershell
python -m pip install -r requirements.lock.txt -r requirements-report.txt
python -m pytest tests/ -v
python -m compileall -q algorithms data_structures visualization performance ui scripts app.py
python -m pip check
python -m scripts.validate_release
```

Compilation passed, dependency checking reported no broken requirements, and the
evidence validator verified 1,080 observed rows and eight guarded skips against
the actual source hashes. The suite covers both algorithms, Custom Set and five
additional structures, the manager, step sequence reconstruction, bounded input,
navigation, persistence, resets, and measurement/export failure behavior.

### Clean-install issue resolved

Freshly installed pandas 3.1.1 failed to load its parsers extension under this
machine's Windows Application Control policy, both in Temp and the workspace.
The extension's SHA-256 matched the previously working installation. The policy
was not changed. Installing the maintained pandas 3.0.6 wheel succeeded; the full
suite then passed. Requirements and the lock now select the tested 3.0 maintenance
series. This was an environment compatibility defect found by the fresh-install
check, not an algorithm defect. Other report-tool imports also passed.

### Known limits

The BST is unbalanced; the custom hash table has fixed capacity; graph operations
are undirected and unweighted. Full immutable sorting traces can be cubic in
storage/time and are bounded to 50 UI values. Allocation observations exclude
prebuilt fixtures and are Python-tracked peaks, not whole-process RAM. Timing
results are specific to the recorded environment, seeds, and workloads. These
limits are intentional, documented, and exercised within the supported bounds.

## Remaining Day 4 gate work

Final measurement, artifact, browser, clean-checkout, and release evidence will
be recorded here after the corresponding checks execute. G4 is not asserted by
the regression checkpoint alone.
