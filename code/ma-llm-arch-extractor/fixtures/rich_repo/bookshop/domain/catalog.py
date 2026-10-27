"""The catalog aggregate and its search behaviour."""

from bookshop.domain.book import Book, Genre


class Catalog:
    """An in-memory collection of books with simple query operations."""

    def __init__(self, books: list[Book]) -> None:
        self._books = list(books)

    def search(self, term: str) -> list[Book]:
        """Return every book whose title, author or tags match the term."""
        return [book for book in self._books if book.matches(term)]

    def by_genre(self, genre: Genre) -> list[Book]:
        """Return every book in the given genre."""
        return [book for book in self._books if book.genre is genre]

    def find(self, isbn: str) -> Book | None:
        """Look up a single book by its ISBN."""
        return next((b for b in self._books if b.isbn == isbn), None)
