"""You can use attrs in most versions of Python

Experience the joy of data classes any where :)

"""

import attr


@attr.s
class Author:
    name: str = attr.ib()

    def is_scary(self):
        return self.name == "H.P. Lovecraft"


@attr.s
class Book:
    title: str = attr.ib()
    author: Author = attr.ib()
