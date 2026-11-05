"""Shared input contract for integer-list algorithms."""


def copy_integer_list(values: list[int]) -> list[int]:
    """Validate a Python list of integers (excluding bool) and return a copy."""
    if not isinstance(values, list):
        raise TypeError("values must be a list of integers")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise TypeError("values must contain only integers; booleans are not accepted")
    return list(values)
