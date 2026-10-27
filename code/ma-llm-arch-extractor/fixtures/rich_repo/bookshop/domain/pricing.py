"""Pure pricing rules: discounts applied to an order's gross total."""

from bookshop.domain.order import Order

BULK_THRESHOLD = 5
BULK_DISCOUNT = 0.10


def total_quantity(order: Order) -> int:
    """Total number of books across all line items."""
    return sum(item.quantity for item in order.items)


def discount_rate(order: Order) -> float:
    """Fraction discounted from the gross total for this order."""
    return BULK_DISCOUNT if total_quantity(order) >= BULK_THRESHOLD else 0.0


def net_cents(order: Order) -> int:
    """Order total after applying the bulk discount, in cents."""
    gross = order.gross_cents()
    return round(gross * (1 - discount_rate(order)))
