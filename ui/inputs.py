"""Strict, bounded integer input parsing without eval or permissive coercion."""

import re

MAX_VALUE = 1_000_000_000


def parse_integer_list(text: str, *, limit: int = 5000, allow_empty: bool = True) -> list[int]:
    """Accept comma/whitespace-separated ASCII integers within +/- 1e9."""
    if not isinstance(text, str):
        raise TypeError("Enter integers as text.")
    if len(text) > 100_000:
        raise ValueError("Input is too long; use at most 100,000 characters.")
    stripped = text.strip()
    if not stripped:
        if allow_empty:
            return []
        raise ValueError("Enter at least one integer.")
    if re.search(r"^,|,$|,\s*,", stripped):
        raise ValueError("A comma must separate two integers; remove empty entries.")
    tokens = re.split(r"[\s,]+", stripped)
    if len(tokens) > limit:
        raise ValueError(f"Use at most {limit:,} integers.")
    values = []
    for token in tokens:
        if not re.fullmatch(r"[+-]?[0-9]+", token) or len(token.lstrip("+-")) > 10:
            raise ValueError(f"Invalid integer {token[:30]!r}; use commas or spaces between whole numbers.")
        value = int(token)
        if abs(value) > MAX_VALUE:
            raise ValueError("Integer values must be between -1,000,000,000 and 1,000,000,000.")
        values.append(value)
    return values


def parse_integer(text: str) -> int:
    values = parse_integer_list(text, limit=1, allow_empty=False)
    return values[0]
