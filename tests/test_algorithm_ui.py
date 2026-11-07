"""Actual algorithm buttons, input errors, and state invalidation."""

from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = Path(__file__).resolve().parents[1] / "app.py"


def algorithms():
    app = AppTest.from_file(APP, default_timeout=30).run()
    return app.radio(key="navigation").set_value("Algorithms").run()


def test_both_algorithms_and_dataset_change_clear_stale_results():
    app = algorithms()
    app.text_area(key="dataset_widget").set_value("3,1,2").run()
    app.button(key="run_bubble").click().run()
    assert app.session_state["bubble_result"].sorted_values == (1, 2, 3)
    app.number_input(key="quick_k_widget").set_value(2).run()
    app.button(key="run_quick").click().run()
    assert app.session_state["quick_result"] == {"k": 2, "value": 2}
    app.text_area(key="dataset_widget").set_value("9,8").run()
    assert app.session_state["bubble_result"] is None
    assert app.session_state["quick_result"] is None
    assert app.session_state["frame_index"] == 0 and not app.exception


def test_rank_changes_invalid_input_empty_lists_and_trace_limit():
    app = algorithms()
    app.text_area(key="dataset_widget").set_value("1,2").run()
    app.number_input(key="quick_k_widget").set_value(3).run()
    app.button(key="run_quick").click().run()
    assert app.error and app.session_state["quick_result"] is None
    app.text_area(key="dataset_widget").set_value("1.5").run()
    assert app.error and app.button(key="run_bubble").disabled
    app.text_area(key="dataset_widget").set_value("").run()
    app.button(key="run_bubble").click().run()
    assert app.session_state["bubble_result"].sorted_values == ()
    app.button(key="run_quick").click().run()
    assert app.error and not app.exception
    app.text_area(key="dataset_widget").set_value(",".join(map(str, range(51)))).run()
    app.button(key="run_bubble").click().run()
    assert app.error and app.session_state["bubble_result"] is None
