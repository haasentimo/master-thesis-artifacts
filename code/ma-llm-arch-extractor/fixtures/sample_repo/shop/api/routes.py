"""HTTP-facing entry points that orchestrate domain and infrastructure.

The API layer wires together the domain model and the persistence adapter.
It is the only layer aware of both.
"""

from shop.domain.order import LineItem, Order, OrderValidationError
from shop.infrastructure.repository import InMemoryOrderRepository

_repo = InMemoryOrderRepository()


def create_order(customer_id: str, items: list[dict]) -> dict:
    """Build an order from a request payload, store it and return a response."""
    order = Order(customer_id=customer_id)
    for item in items:
        order.add_item(
            LineItem(
                sku=item["sku"],
                quantity=item["quantity"],
                unit_price_cents=item["unit_price_cents"],
            )
        )
    try:
        order_id = _repo.save(order)
    except OrderValidationError as exc:
        return {"status": "error", "message": str(exc)}
    return {"status": "ok", "order_id": order_id, "total_cents": order.total_cents()}


def get_order_total(order_id: int) -> dict:
    """Look up a stored order and report its total."""
    order = _repo.get(order_id)
    if order is None:
        return {"status": "not_found"}
    return {"status": "ok", "total_cents": order.total_cents()}
