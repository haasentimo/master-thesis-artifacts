"""Use-case service for browsing and searching available stock."""

from bookshop.domain.book import Book, Genre
from bookshop.infrastructure.book_repository import InMemoryBookRepository


class InventoryService:
    """Read-side service over the book repository's catalog."""

    def __init__(self, books: InMemoryBookRepository) -> None:
        self._books = books

    def search(self, term: str) -> list[Book]:
        """Search the current catalog for a term."""
        return self._books.catalog().search(term)

    def browse(self, genre: Genre) -> list[Book]:
        """List all books in a genre."""
        return self._books.catalog().by_genre(genre)
