"""Pricing display helpers built on the unit conversion layer."""

from demo.units import bps_to_fraction, cents_to_dollars


def describe_offer(offer):
    """Return a human-readable description of a loan offer."""
    amount = cents_to_dollars(offer["amount_cents"])
    rate = bps_to_fraction(offer["rate_bps"])
    return f"${amount:,.2f} at {rate * 100:.2f}%"
