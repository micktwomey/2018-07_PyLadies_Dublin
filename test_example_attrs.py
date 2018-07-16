from example_attrs import Author, Book

import attr
import pytest


def test_invalid_author():
    with pytest.raises(
        TypeError, match="missing 1 required positional argument: 'name'"
    ):
        author = Author()  # Missing the name


def test_valid_author():
    author = Author("H.P. Lovecraft")
    assert author.is_scary()


def test_valid_book():
    author = Author("H.P. Lovecraft")
    book = Book("At the Mountains of Madness", author=author)

    # Neat, it descends into nested dataclasses and converts them too :)
    assert attr.asdict(book) == {
        "author": {"name": "H.P. Lovecraft"},
        "title": "At the Mountains of Madness",
    }

    # And to tuples, preserving order of the arguments
    assert attr.astuple(book) == ("At the Mountains of Madness", ("H.P. Lovecraft",))
