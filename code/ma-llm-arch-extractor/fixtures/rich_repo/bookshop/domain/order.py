"""Order aggregate: line items, status and invariants."""

from dataclasses import dataclass, field
from enum import Enum

from bookshop.domain.book import Book


class OrderStatus(str, Enum):
    """Lifecycle states of a customer order."""

    DRAFT = "draft"
    PLACED = "placed"
    PAID = "paid"


@dataclass
class LineItem:
    """A quantity of a single book within an order."""

    book: Book
    quantity: int

    def subtotal_cents(self) -> int:
        """List-price subtotal for this line, before any discounts."""
        return self.book.list_price_cents * self.quantity


@dataclass
class Order:
    """A customer order aggregating line items and a status."""

    customer_id: str
    items: list[LineItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.DRAFT

    def add(self, book: Book, quantity: int) -> None:
        """Add a quantity of a book to the order."""
        self.items.append(LineItem(book=book, quantity=quantity))

    def gross_cents(self) -> int:
        """Sum of all line subtotals before discounts."""
        return sum(item.subtotal_cents() for item in self.items)


class EmptyOrderError(Exception):
    """Raised when an order with no items is placed."""
