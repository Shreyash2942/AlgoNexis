"""Actual Streamlit script navigation and persistent-object spike."""

from pathlib import Path

from streamlit.testing.v1 import AppTest


def test_all_sections_render_and_manager_survives_reruns():
    app = AppTest.from_file(Path(__file__).resolve().parents[1] / "app.py").run()
    assert not app.exception
    manager = app.session_state["manager"]
    manager.execute("stack", "push", value=7)
    for page in ["Algorithms", "Data Structures", "Performance Analysis", "Dashboard"]:
        app.radio(key="navigation").set_value(page).run()
        assert not app.exception
        assert app.session_state["manager"] is manager
        assert manager.execute("stack", "peek") == 7
