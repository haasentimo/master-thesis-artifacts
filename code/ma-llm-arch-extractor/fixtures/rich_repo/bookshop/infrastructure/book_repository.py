"""In-memory persistence adapter for the book catalog."""

from bookshop.domain.book import Book
from bookshop.domain.catalog import Catalog


class InMemoryBookRepository:
    """Stores books and hands out a Catalog view over them."""

    def __init__(self) -> None:
        self._books: dict[str, Book] = {}

    def add(self, book: Book) -> None:
        """Persist a book keyed by its ISBN."""
        self._books[book.isbn] = book

    def get(self, isbn: str) -> Book | None:
        """Fetch a stored book by ISBN."""
        return self._books.get(isbn)

    def catalog(self) -> Catalog:
        """Build a Catalog aggregate from all stored books."""
        return Catalog(list(self._books.values()))
