# Day 1 verification and gate G1

Verification date: 2026-11-04. Scope: D1.1 through D1.6 only.

## Environment and repository

- Preserved the existing local Git repository, `main` branch, origin, and full
  product README. GitHub metadata confirmed the existing public repository at
  https://github.com/Shreyash2942/AlgoNexis and default branch `main`.
- Created `.venv` with CPython 3.14.4 on Windows. Dependency installation from
  `requirements.txt` succeeded: Streamlit 1.66.1 and pytest 9.2.0. The resolved
  environment is recorded in `requirements.lock.txt`.
- `python -m pip check`: no broken requirements found.
- Activation via `.venv\Scripts\activate.bat` selected Python 3.14.4. PowerShell
  users can use the environment executable directly without changing execution
  policy. No system policy was changed.
- Prior-course stack, queue, tree, graph, and hash-table candidates were located
  and inventoried in `data_structures.md`. They are not yet verified/reused.

## Implemented acceptance evidence

| Work package | Evidence |
|---|---|
| D1.1 | Package layout, virtual environment, dependency installation/lock, existing GitHub repository, reuse inventory |
| D1.2 | Adjacent compare/swap, early exit, integer validation, copied input, immutable complete trace, exact counts |
| D1.3 | Initial/final frames, highlighted indices, swap metadata, total count, index lookup, ordered non-UI playback |
| D1.4 | One-based duplicate-aware selection, randomized three-way partition, input/rank validation, copied input, controlled RNG |
| D1.5 | 71 passing pytest cases, including exhaustive/property-style scenarios and trace reconstruction |
| D1.6 | README examples, architecture/API/complexity decisions, doctests, compile/import checks, reviewed real commits |

The first full run of `python -m pytest tests/ -v` completed with **71 passed
in 0.34s**. Tests check sorted, reversed, negative, duplicate, empty/singleton
cases; exact known event sequences; independent action replay and inversion
counts; traced/untraced parity; immutable snapshots; rank boundaries/errors;
reproducible pivots; and complete visualization metadata. A subprocess with
`python -S` verifies that core imports and playback need only the standard library,
without access to installed UI packages.

Pre-commit smoke checks also passed for 1,093 exhaustive Bubble Sort lists,
364 visualization traces, and 6,015 exhaustive Quickselect ranks, plus a
10,000-element duplicate selection. These are validation checks, not benchmark
observations and are not represented as performance evidence.

## Commits and gate decision

The first four work-package commits are:

1. `3988e69` - `chore: initialize AlgoNexis project structure`
2. `43ca9da` - `feat: implement bubble sort with step tracking`
3. `18d4734` - `feat: add sorting visualization engine`
4. `4ac2b24` - `feat: implement quickselect with input validation`

This verification record, permanent tests, final documentation, plan status, and
updated knowledge graph are included in commit 05:
`test: add core algorithm tests and documentation`. Its resulting hash is read
from Git after creation; no self-referential hash is embedded here.

**G1: passed.** Core algorithms and ordered steps meet the automated acceptance
checks and import independently of Streamlit. The Day 1 history comprises five
meaningful local commits. No push, UI integration, data-structure completion,
runtime/memory benchmarks, report PDF, presentation, or release tag is claimed.

Next work package: **D2.1 - Custom Set**, beginning with the documented contracts
and review of relevant prior coursework. Days 2-4 gates remain unverified.
