"""Standalone demo-only integer money arithmetic. No network, DB, secrets or payment API."""

from collections.abc import Iterable


def subtotal_yen(lines: Iterable[tuple[int, int]]) -> int:
    """Sum (unit_price_yen, quantity) demo lines. Reject invalid integers."""
    total = 0
    for price, quantity in lines:
        if type(price) is not int or type(quantity) is not int:
            raise TypeError("price and quantity must be integers")
        if price < 0 or quantity < 0:
            raise ValueError("price and quantity must be nonnegative")
        total += price * quantity
    return total
