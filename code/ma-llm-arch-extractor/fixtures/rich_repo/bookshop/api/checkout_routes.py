"""HTTP handlers for the checkout flow."""

from bookshop.application.checkout import CheckoutService
from bookshop.domain.order import EmptyOrderError, Order


def checkout(service: CheckoutService, order: Order) -> dict:
    """Handle a checkout request, mapping domain errors to a response."""
    try:
        return {"status": "ok", **service.place(order)}
    except EmptyOrderError as exc:
        return {"status": "error", "message": str(exc)}
