"""Core domain entities and business rules for customer orders.

This module is pure domain logic: it has no knowledge of databases,
web frameworks or any other infrastructure concern.
"""

from dataclasses import dataclass, field


@dataclass
class LineItem:
    """A single product line within an order."""

    sku: str
    quantity: int
    unit_price_cents: int

    def subtotal_cents(self) -> int:
        """Return the total price for this line in cents."""
        return self.quantity * self.unit_price_cents


@dataclass
class Order:
    """An aggregate of line items placed by a customer."""

    customer_id: str
    items: list[LineItem] = field(default_factory=list)

    def total_cents(self) -> int:
        """Sum every line item to the order total in cents."""
        return sum(item.subtotal_cents() for item in self.items)

    def add_item(self, item: LineItem) -> None:
        """Append a line item to this order."""
        self.items.append(item)


class OrderValidationError(Exception):
    """Raised when an order violates a domain invariant."""


def validate_order(order: Order) -> None:
    """Enforce domain invariants: a non-empty order with positive quantities."""
    if not order.items:
        raise OrderValidationError("order must contain at least one item")
    for item in order.items:
        if item.quantity <= 0:
            raise OrderValidationError(f"non-positive quantity for {item.sku}")
