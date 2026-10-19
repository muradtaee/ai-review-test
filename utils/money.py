"""Money helpers."""
from decimal import ROUND_HALF_UP, Decimal

MINOR_UNITS = {"JPY": 0, "USD": 2, "EUR": 2, "KWD": 3}


def round_money(amount: Decimal, currency: str) -> Decimal:
    """Round an amount to the currency's minor units."""
    code = currency.upper()
    if code not in MINOR_UNITS:
        raise ValueError(f"Unknown currency: {currency}")
    quantum = Decimal(1).scaleb(-MINOR_UNITS[code])
    return amount.quantize(quantum, rounding=ROUND_HALF_UP)


def round_price(price: float, currency: str) -> float:
    """Convenience wrapper for prices coming from the pricing API."""
    return float(round_money(Decimal(price), currency))
