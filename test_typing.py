import dataclasses

import pytest

from example_typing import Tree


def test_valid_tree():
    leaf = Tree(None, None)
    root = Tree(leaf, None)
    assert dataclasses.asdict(root) == {
        "left": {"left": None, "right": None},
        "right": None,
    }


def test_invalid_tree():
    with pytest.raises(NameError, match="name 'Tree' is not defined"):
        import example_invalid_typing
