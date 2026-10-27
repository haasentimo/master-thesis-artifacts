"""Catalog domain entities: books and their authors.

Pure domain model with no infrastructure dependencies.
"""

from dataclasses import dataclass, field
from enum import Enum


class Genre(str, Enum):
    """Coarse classification used for browsing the catalog."""

    FICTION = "fiction"
    NONFICTION = "nonfiction"
    SCIENCE = "science"


@dataclass(frozen=True)
class Author:
    """A book author, identified by a stable id."""

    id: str
    name: str


@dataclass
class Book:
    """A sellable book with a list price expressed in cents."""

    isbn: str
    title: str
    author: Author
    genre: Genre
    list_price_cents: int
    tags: list[str] = field(default_factory=list)

    def matches(self, term: str) -> bool:
        """Return True if a search term occurs in title, author or tags."""
        haystack = " ".join([self.title, self.author.name, *self.tags]).lower()
        return term.lower() in haystack
