from dataclasses import dataclass


@dataclass
class Tree:
    left: Tree
    right: Tree
