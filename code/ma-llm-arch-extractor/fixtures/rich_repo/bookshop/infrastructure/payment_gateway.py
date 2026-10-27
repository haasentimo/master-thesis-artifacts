"""Adapter to an external payment provider (faked for the fixture)."""


class PaymentError(Exception):
    """Raised when an external charge is declined."""


class FakePaymentGateway:
    """Pretends to talk to an external payment API over the network."""

    def __init__(self) -> None:
        self.charges: list[int] = []

    def charge(self, customer_id: str, amount_cents: int) -> str:
        """Charge a customer and return an opaque transaction id."""
        if amount_cents <= 0:
            raise PaymentError("amount must be positive")
        self.charges.append(amount_cents)
        return f"txn_{len(self.charges)}"
