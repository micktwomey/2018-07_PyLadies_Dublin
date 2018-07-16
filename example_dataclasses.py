from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class Author:
    name: str

    def is_scary(self):
        return self.name == "H.P. Lovecraft"


@dataclasses.dataclass
class Book:
    title: str
    author: Author
