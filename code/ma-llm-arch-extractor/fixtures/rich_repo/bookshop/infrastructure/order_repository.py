"""In-memory persistence adapter for orders."""

from bookshop.domain.order import Order


class InMemoryOrderRepository:
    """Stores orders under an auto-incrementing id."""

    def __init__(self) -> None:
        self._orders: dict[int, Order] = {}
        self._next_id = 1

    def save(self, order: Order) -> int:
        """Persist an order and return its assigned id."""
        order_id = self._next_id
        self._orders[order_id] = order
        self._next_id += 1
        return order_id

    def get(self, order_id: int) -> Order | None:
        """Fetch a stored order by id."""
        return self._orders.get(order_id)
