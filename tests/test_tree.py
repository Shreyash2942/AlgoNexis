"""Traversal, uniqueness, skew, and integer-domain checks."""

from random import Random

import pytest

from data_structures.tree import BinarySearchTree


def test_known_traversals_duplicate_policy_and_search():
    tree = BinarySearchTree([4, 2, 6, 1, 3, 5, 7])
    assert tree.inorder() == [1, 2, 3, 4, 5, 6, 7]
    assert tree.preorder() == [4, 2, 1, 3, 6, 5, 7]
    assert tree.postorder() == [1, 3, 2, 5, 7, 6, 4]
    assert tree.insert(4) is False and len(tree) == 7
    assert tree.search(1) and tree.search(7) and not tree.search(99)
    assert tree.insert(-1) is True and tree.search(-1)
    copy = tree.display()
    copy.clear()
    assert len(tree.display()) == 8


def test_empty_and_singleton():
    tree = BinarySearchTree()
    assert tree.is_empty() and len(tree) == 0 and not tree.search(1)
    assert tree.inorder() == tree.preorder() == tree.postorder() == []
    tree.insert(0)
    assert tree.inorder() == tree.preorder() == tree.postorder() == [0]


@pytest.mark.parametrize("descending", [False, True])
def test_skewed_tree_beyond_recursion_depth(descending):
    values = list(range(1200))
    if descending:
        values.reverse()
    tree = BinarySearchTree(values)
    assert tree.inorder() == list(range(1200))
    assert tree.preorder() == values and tree.postorder() == values[::-1]
    assert tree.search(values[-1]) and not tree.search(-1)


def test_seeded_insertions_match_sorted_unique_reference():
    rng, tree, expected = Random(506), BinarySearchTree(), set()
    for _ in range(300):
        value = rng.randrange(-50, 51)
        assert tree.insert(value) == (value not in expected)
        expected.add(value)
        assert tree.inorder() == sorted(expected)


@pytest.mark.parametrize("value", [True, 1.5, "2", None])
def test_invalid_values_leave_tree_unchanged(value):
    tree = BinarySearchTree([1])
    for operation in (tree.insert, tree.search):
        with pytest.raises(TypeError, match="integers"):
            operation(value)
    assert tree.display() == [1]
