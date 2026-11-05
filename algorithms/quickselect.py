"""Iterative randomized Quickselect with one-based ranks and duplicate support.

Uniform random pivots give expected O(n) and worst O(n**2) time. Three-way
partitioning handles a block of equal values in one pass. The internal copy uses
O(n) space; partitioning itself uses O(1) auxiliary space, without recursion.

Example:
    >>> from random import Random
    >>> quickselect([7, -1, 7, 3], 3, rng=Random(42))
    7
"""

from random import Random

from algorithms._validation import copy_integer_list


def quickselect(values: list[int], k: int, *, rng: Random | None = None) -> int:
    """Return the kth-smallest integer without sorting or changing caller data.

    Ranks are one-based and include duplicates: rank 2 of [1, 1, 9] is 1.
    Supply ``Random(seed)`` for reproducible pivot choices. With no generator,
    a fresh local Random is used; global random state is not modified.
    Recreate the seeded generator for identical trials; reusing it advances it.

    Raises:
        TypeError: values is not an integer list (bool excluded), k is not
            an integer (bool excluded), or rng is not a Random instance.
        ValueError: values is empty or k is outside 1..len(values).
    """
    working = copy_integer_list(values)
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("k must be an integer; booleans are not accepted")
    if not working:
        raise ValueError("quickselect requires a nonempty list")
    if not 1 <= k <= len(working):
        raise ValueError("k must satisfy 1 <= k <= len(values)")
    if rng is not None and not isinstance(rng, Random):
        raise TypeError("rng must be a random.Random instance or None")
    generator = rng if rng is not None else Random()
    target = k - 1
    left, right = 0, len(working) - 1

    while True:
        pivot = working[generator.randrange(left, right + 1)]
        lower, current, upper = left, left, right
        # [left, lower) < pivot; [lower, current) == pivot;
        # (upper, right] > pivot; [current, upper] is not yet classified.
        while current <= upper:
            if working[current] < pivot:
                working[lower], working[current] = working[current], working[lower]
                lower += 1
                current += 1
            elif working[current] > pivot:
                working[current], working[upper] = working[upper], working[current]
                upper -= 1
            else:
                current += 1

        if target < lower:
            right = lower - 1
        elif target > upper:
            left = upper + 1
        else:
            return pivot
