# AlgoNexis architecture and decisions

## Foundation

The root README and four-day implementation plan define the target system.
Day 1 establishes importable Python packages and core algorithms. Data structures,
Streamlit views, measurements, and academic deliverables belong to later days.

- Existing Git repository and `origin` are preserved; the default branch is `main`.
- GitHub repository: https://github.com/Shreyash2942/AlgoNexis (verified existing).
- Development Python: CPython 3.14.4 on Windows; source targets Python 3.11+.
- `.venv` isolates dependencies. `requirements.txt` lists direct dependencies;
  `requirements.lock.txt` records the tested environment after installation.
- Core modules must import without importing Streamlit or starting a UI.
- Prior-course reuse candidates are recorded in `data_structures.md` and require
  a separate correctness/interface review during Day 2.

## Package boundaries

`algorithms` owns sorting and selection. `visualization` consumes immutable
sorting records. `data_structures` is reserved for Day 2; `performance` for Day 3.
`results` will hold actual benchmark output once measurements are implemented.
No placeholder benchmark CSV, UI, report PDF, or presentation is created on Day 1.
