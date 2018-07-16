from __future__ import annotations

# From https://realpython.com/python37-new-features/
class Tree:
    def __init__(self, left: Tree, right: Tree) -> None:
        self.left = left
        self.right = right
