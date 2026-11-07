"""Actual playback controls retain correct boundaries across reruns/navigation."""

from pathlib import Path

from streamlit.testing.v1 import AppTest


def test_all_steps_final_values_previous_reset_and_navigation():
    app = AppTest.from_file(Path(__file__).resolve().parents[1] / "app.py", default_timeout=30).run()
    app.radio(key="navigation").set_value("Algorithms").run()
    app.text_area(key="dataset_widget").set_value("3,1,2").run()
    app.button(key="run_bubble").click().run()
    total = len(app.session_state["bubble_result"].steps)
    assert app.button(key="previous_step").disabled
    for expected in range(1, total):
        app.button(key="next_step").click().run()
        assert app.session_state["frame_index"] == expected
    assert app.button(key="next_step").disabled
    assert any("FINAL" in c.value for c in app.caption)
    assert app.session_state["bubble_result"].steps[-1].values == (1, 2, 3)
    app.button(key="previous_step").click().run()
    assert app.session_state["frame_index"] == total - 2
    app.radio(key="navigation").set_value("Dashboard").run()
    app.radio(key="navigation").set_value("Algorithms").run()
    assert app.session_state["frame_index"] == total - 2
    app.button(key="reset_steps").click().run()
    assert app.session_state["frame_index"] == 0 and not app.exception


def test_slider_and_untraced_mode_do_not_discard_or_invent_steps():
    app = AppTest.from_file(Path(__file__).resolve().parents[1] / "app.py", default_timeout=30).run()
    app.radio(key="navigation").set_value("Algorithms").run()
    app.button(key="run_bubble").click().run()
    last = len(app.session_state["bubble_result"].steps) - 1
    app.slider(key="frame_slider").set_value(last).run()
    assert app.session_state["frame_index"] == last
    app.checkbox(key="trace_enabled").uncheck().run()
    app.button(key="run_bubble").click().run()
    assert app.session_state["bubble_result"].steps == ()
    assert not app.exception
