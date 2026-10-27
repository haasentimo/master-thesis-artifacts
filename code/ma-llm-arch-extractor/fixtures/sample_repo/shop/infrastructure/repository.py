"""Persistence adapter that stores domain orders in memory.

Infrastructure depends on the domain layer, never the other way around.
"""

from shop.domain.order import Order, validate_order


class InMemoryOrderRepository:
    """A trivial order store keyed by an auto-incrementing id."""

    def __init__(self) -> None:
        self._orders: dict[int, Order] = {}
        self._next_id = 1

    def save(self, order: Order) -> int:
        """Validate and persist an order, returning its assigned id."""
        validate_order(order)
        order_id = self._next_id
        self._orders[order_id] = order
        self._next_id += 1
        return order_id

    def get(self, order_id: int) -> Order | None:
        """Fetch a previously stored order, or None if unknown."""
        return self._orders.get(order_id)
