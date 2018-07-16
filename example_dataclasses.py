from dataclasses import dataclass


@dataclass
class Author:
    name: str

    def is_scary(self):
        return self.name == "H.P. Lovecraft"


@dataclass
class Book:
    title: str
    author: Author
