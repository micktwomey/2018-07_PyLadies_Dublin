from __future__ import annotations

from dataclasses import dataclass

# From https://realpython.com/python37-new-features/
@dataclass
class Tree:
    left: Tree
    right: Tree
