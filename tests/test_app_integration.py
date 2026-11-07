"""Final cross-section invalidation and readable runtime error checks."""

from pathlib import Path

from streamlit.testing.v1 import AppTest


def test_samples_rank_invalidation_and_independent_structure_state():
    app = AppTest.from_file(Path(__file__).resolve().parents[1] / "app.py", default_timeout=30).run()
    manager = app.session_state["manager"]
    manager.execute("queue", "enqueue", value=99)
    app.radio(key="navigation").set_value("Algorithms").run()
    app.button(key="run_quick").click().run()
    assert app.session_state["quick_result"] is not None
    app.number_input(key="quick_k_widget").set_value(2).run()
    assert app.session_state["quick_result"] is None
    app.button(key="run_bubble").click().run()
    app.selectbox(key="sample_dataset").set_value("Empty").run()
    app.button(key="load_sample").click().run()
    assert app.session_state["dataset_text"] == ""
    assert app.session_state["bubble_result"] is None
    app.button(key="run_bubble").click().run()
    assert len(app.session_state["bubble_result"].steps) == 2
    app.button(key="next_step").click().run()
    assert any("FINAL" in item.value for item in app.caption)
    assert manager.execute("queue", "front") == 99 and not app.exception
