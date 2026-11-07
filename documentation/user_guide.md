# AlgoNexis user guide

## Start the local portfolio

From the repository root, install `requirements.txt` in `.venv`, then run:

```powershell
& .\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the printed local URL (normally http://localhost:8501). The sidebar offers
Dashboard, Algorithms, Data Structures, and Performance Analysis. Each browser
session owns its manager and exploration state; reruns do not recreate it.

D3.1 delivers the tested navigation shell. Subsequent Day 3 work packages replace
the explicitly labeled in-progress panels with algorithm/structure controls and
measured charts. Nothing is hosted by Sites or deployed externally.

## Development checks

Run `python -m pytest tests/ -v` with the virtual environment's Python.
Streamlit's AppTest exercises the actual app script. Optional real-browser QA uses
`requirements-dev.txt` and Playwright with an installed Edge/Chromium browser.
The tested dependency versions are recorded in `requirements.lock.txt`.
