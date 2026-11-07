"""Exercise each structure through the actual Streamlit controls."""

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from ui.state import execute_structure, initialize


def structures():
    app = AppTest.from_file(Path(__file__).resolve().parents[1] / "app.py", default_timeout=30).run()
    return app.radio(key="navigation").set_value("Data Structures").run()


@pytest.mark.parametrize("name,operation", [("set", "add"), ("stack", "push"), ("queue", "enqueue"), ("tree", "insert")])
def test_integer_structure_mutations_persist_and_reset(name, operation):
    app = structures()
    app.selectbox(key="structure_widget").set_value(name).run()
    app.selectbox(key=f"operation_{name}").set_value(operation).run()
    app.text_input(key="structure_value").set_value("7").run()
    app.button(key="run_structure").click().run()
    assert app.session_state["manager"].execute(name, "display") == [7]
    app.radio(key="navigation").set_value("Dashboard").run()
    app.radio(key="navigation").set_value("Data Structures").run()
    assert app.session_state["manager"].execute(name, "display") == [7]
    app.button(key="reset_structures").click().run()
    assert app.session_state["manager"].execute(name, "is_empty")
    assert not app.exception


def test_set_algebra_through_controls_preserves_operand():
    app = structures()
    app.text_input(key="structure_value").set_value("1").run()
    app.button(key="run_structure").click().run()
    for operation, expected in [("union", [1, 2, 3]), ("intersection", []), ("difference", [1]), ("symmetric_difference", [1, 2, 3])]:
        app.selectbox(key="operation_set").set_value(operation).run()
        app.button(key="run_structure").click().run()
        assert app.session_state["structure_result"]["result"] == expected
        assert app.session_state["manager"].execute("set", "display") == [1]


def test_graph_and_hash_table_controls_and_errors():
    app = structures()
    app.selectbox(key="structure_widget").set_value("graph").run()
    app.selectbox(key="operation_graph").set_value("add_edge").run()
    app.button(key="run_structure").click().run()
    for operation in ["bfs", "dfs"]:
        app.selectbox(key="operation_graph").set_value(operation).run()
        app.button(key="run_structure").click().run()
        assert app.session_state["structure_result"]["result"] == [0, 1]
    app.text_input(key="graph_vertex").set_value("99").run()
    app.button(key="run_structure").click().run()
    assert app.error
    app.selectbox(key="structure_widget").set_value("hash_table").run()
    app.text_input(key="table_key").set_value("8").run()
    app.text_input(key="table_value").set_value("stored").run()
    app.button(key="run_structure").click().run()
    app.selectbox(key="operation_hash_table").set_value("find").run()
    app.button(key="run_structure").click().run()
    assert app.session_state["structure_result"]["result"] == "stored"
    app.selectbox(key="operation_hash_table").set_value("delete").run()
    app.button(key="run_structure").click().run()
    assert app.session_state["manager"].execute("hash_table", "is_empty")
    assert not app.exception


def test_empty_pop_invalid_integer_and_unknown_operation_are_readable():
    app = structures()
    app.selectbox(key="structure_widget").set_value("stack").run()
    app.selectbox(key="operation_stack").set_value("pop").run()
    app.button(key="run_structure").click().run()
    assert app.error and not app.exception
    app.selectbox(key="operation_stack").set_value("push").run()
    app.text_input(key="structure_value").set_value("1.5").run()
    app.button(key="run_structure").click().run()
    assert app.error and app.session_state["manager"].execute("stack", "is_empty")
    state = {}
    initialize(state)
    with pytest.raises(ValueError, match="unsupported"):
        execute_structure(state, "stack", "__class__")


def test_ui_growth_guard_is_atomic_and_allows_existing_key_updates():
    state = {}
    initialize(state)
    for value in range(200):
        execute_structure(state, "hash_table", "insert", key=value, value=value)
    execute_structure(state, "hash_table", "insert", key=0, value="updated")
    with pytest.raises(ValueError, match="200"):
        execute_structure(state, "hash_table", "insert", key=201, value=201)
    assert state["manager"].execute("hash_table", "size") == 200
