"""Reject partial numeric coercion and unsafe or oversized datasets."""

import pytest

from ui.inputs import parse_integer, parse_integer_list


@pytest.mark.parametrize("text,expected", [("", []), (" 1, -2\n+3  0", [1, -2, 3, 0]), ("0,0", [0, 0])])
def test_integer_lists(text, expected):
    assert parse_integer_list(text) == expected


@pytest.mark.parametrize("text", ["1.0", "True", "1,,2", ",1", "1,", "[1,2]", "1e2", "__import__('os')", "1000000001", "9" * 100])
def test_invalid_tokens_and_bounds(text):
    with pytest.raises(ValueError):
        parse_integer_list(text)


def test_single_integer_limits_and_required_values():
    assert parse_integer("-7") == -7
    for text in ["", "1,2"]:
        with pytest.raises(ValueError):
            parse_integer(text)
    with pytest.raises(ValueError, match="at most"):
        parse_integer_list("1,2,3", limit=2)
