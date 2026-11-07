"""Optional real Edge/Chromium walkthrough against a running local Streamlit app.

Run: python -m tests.browser_smoke --url http://127.0.0.1:8501
Requires requirements-dev.txt and installed Microsoft Edge. The benchmark button
creates a real full default run and replaces results/benchmark_results.csv.
"""

import argparse
import csv
from io import StringIO
from pathlib import Path
from urllib.request import urlopen

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


def run(url: str, *, measure: bool = True) -> None:
    assert urlopen(url + "/_stcore/health", timeout=10).status == 200
    screenshots = ROOT / "documentation/screenshots"
    screenshots.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1050}, device_scale_factor=1)
        page.set_default_timeout(15000)
        page.goto(url)
        page.get_by_role("heading", name="Understand the steps. Measure the trade-offs.").wait_for()

        def ready():
            # Allow the browser's widget event to reach the local script runner.
            page.wait_for_timeout(150)
            page.locator('[data-testid="stApp"][data-test-script-state="notRunning"]').wait_for(timeout=60000)

        def focus_heading(name):
            page.get_by_role("heading", name=name, exact=True).evaluate("el => el.scrollIntoView({block: 'start'})")
            page.get_by_test_id("stMain").evaluate("el => el.scrollTop = Math.max(0, el.scrollTop - 70)")
            page.wait_for_timeout(250)

        ready()
        page.screenshot(path=str(screenshots / "dashboard.png"), full_page=True)

        def navigate(name):
            page.get_by_test_id("stSidebar").get_by_text(name, exact=True).click()
            page.get_by_role("heading", name=name, exact=True).wait_for()
            ready()

        navigate("Algorithms")
        page.get_by_role("textbox", name="Integer dataset", exact=True).fill("3, 1, 2")
        page.get_by_role("textbox", name="Integer dataset", exact=True).press("Tab")
        page.get_by_text("3 values.", exact=False).wait_for()
        ready()
        page.get_by_role("button", name="Run Bubble Sort", exact=True).click()
        page.get_by_text("Step 1 of 7", exact=False).wait_for()
        for step in range(2, 8):
            page.get_by_role("button", name="Next", exact=True).click()
            page.get_by_text(f"Step {step} of 7", exact=False).wait_for()
        assert page.get_by_role("button", name="Next", exact=True).is_disabled()
        page.get_by_role("spinbutton", name="Rank k (1-based)", exact=True).fill("2")
        page.get_by_role("spinbutton", name="Rank k (1-based)", exact=True).press("Tab")
        ready()
        page.get_by_role("button", name="Run Quickselect", exact=True).click()
        page.get_by_text("Rank 2 value", exact=True).wait_for()
        focus_heading("Algorithms")
        page.screenshot(path=str(screenshots / "algorithms.png"), full_page=True)
        for _ in range(2):
            page.get_by_role("button", name="Previous", exact=True).click()
            ready()
        focus_heading("Sorting, one event at a time")
        page.screenshot(path=str(screenshots / "sorting-steps.png"), full_page=True)
        page.get_by_role("textbox", name="Integer dataset", exact=True).fill("1.5")
        page.get_by_role("textbox", name="Integer dataset", exact=True).press("Tab")
        page.get_by_text("Invalid integer", exact=False).wait_for()
        assert page.get_by_role("button", name="Run Bubble Sort", exact=True).is_disabled()

        navigate("Data Structures")

        def select(label, option):
            page.get_by_role("combobox", name=label, exact=True).click()
            page.get_by_role("option", name=option, exact=True).click()
            ready()

        for structure in ["Custom Set", "Stack", "Queue", "Binary Search Tree", "Graph", "Hash Table"]:
            select("Structure", structure)
            page.get_by_role("button", name="Run operation", exact=True).click()
            page.get_by_text("Operation completed.", exact=True).wait_for()
            assert page.get_by_test_id("stException").count() == 0
        page.screenshot(path=str(screenshots / "structures.png"), full_page=True)
        page.get_by_role("button", name="Reset all structures", exact=True).click()
        ready()

        navigate("Performance Analysis")
        page.get_by_text("Observed repeat summaries", exact=True).wait_for()
        if measure:
            page.get_by_text("Run a reproducible benchmark", exact=True).click()
            page.get_by_role("button", name="Run benchmarks", exact=True).click()
            page.get_by_text("Saved 1,080 measured observations.", exact=True).wait_for(timeout=60000)
        with page.expect_download() as pending:
            page.get_by_role("button", name="Download full run CSV", exact=True).click()
        download = pending.value
        downloaded = Path(download.path()).read_text(encoding="utf-8")
        assert downloaded == (ROOT / "results/benchmark_results.csv").read_text(encoding="utf-8")
        rows = list(csv.DictReader(StringIO(downloaded)))
        assert len(rows) == 1088 and sum(row["status"] == "ok" for row in rows) == 1080
        if measure:
            page.get_by_text("Run a reproducible benchmark", exact=True).click()
        ready()
        focus_heading("Performance Analysis")
        page.screenshot(path=str(screenshots / "performance-overview.png"), full_page=True)
        focus_heading("Execution time")
        page.screenshot(path=str(screenshots / "performance.png"), full_page=True)
        assert page.get_by_test_id("stException").count() == 0

        mobile = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
        mobile.goto(url)
        mobile.get_by_role("heading", name="Understand the steps. Measure the trade-offs.").wait_for()
        mobile.screenshot(path=str(screenshots / "dashboard-mobile.png"), full_page=True)
        assert mobile.get_by_test_id("stException").count() == 0
        browser.close()
    print("Real Edge walkthrough passed: navigation, algorithms/stepper/errors, all six structures, reset, measured charts and exact CSV download; screenshots saved.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default="http://127.0.0.1:8501")
    parser.add_argument("--skip-benchmark", action="store_true", help="Verify the existing recorded run without replacing measurements.")
    args = parser.parse_args()
    run(args.url.rstrip("/"), measure=not args.skip_benchmark)
