"""HTTP handlers for browsing and searching the catalog."""

from bookshop.application.inventory import InventoryService
from bookshop.domain.book import Genre


def search_books(service: InventoryService, term: str) -> dict:
    """Handle a catalog search request."""
    hits = service.search(term)
    return {"count": len(hits), "isbns": [b.isbn for b in hits]}


def browse_genre(service: InventoryService, genre: str) -> dict:
    """Handle a browse-by-genre request."""
    books = service.browse(Genre(genre))
    return {"genre": genre, "isbns": [b.isbn for b in books]}
