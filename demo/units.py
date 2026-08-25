"""Unit conversion helpers used by the reporting pipeline."""


def cents_to_dollars(cents):
    """Convert an integer cent amount to a float dollar amount."""
    return cents / 100


def bps_to_fraction(bps):
    """Convert basis points to a plain fraction."""
    return bps / 10_000
