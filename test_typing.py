from example_typing import Tree

import pytest


def test_valid_tree():
    leaf = Tree(None, None)
    root = Tree(leaf, None)


def test_invalid_tree():
    with pytest.raises(NameError, match="name 'Tree' is not defined"):
        import example_invalid_typing
