"""Use-case service that turns a draft order into a paid, stored order.

Orchestrates domain pricing rules with the persistence and payment
adapters from the infrastructure layer.
"""

from bookshop.domain import pricing
from bookshop.domain.order import EmptyOrderError, Order, OrderStatus
from bookshop.infrastructure.order_repository import InMemoryOrderRepository
from bookshop.infrastructure.payment_gateway import FakePaymentGateway


class CheckoutService:
    """Coordinates pricing, payment and order persistence."""

    def __init__(
        self,
        orders: InMemoryOrderRepository,
        gateway: FakePaymentGateway,
    ) -> None:
        self._orders = orders
        self._gateway = gateway

    def place(self, order: Order) -> dict:
        """Price, charge and persist an order; return a result summary."""
        if not order.items:
            raise EmptyOrderError("cannot place an empty order")
        amount = pricing.net_cents(order)
        txn = self._gateway.charge(order.customer_id, amount)
        order.status = OrderStatus.PAID
        order_id = self._orders.save(order)
        return {"order_id": order_id, "amount_cents": amount, "transaction": txn}
