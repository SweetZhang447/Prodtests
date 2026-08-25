"""Builds a one-line summary row for a loan report."""

from demo.formatter import format_currency, format_percent


def build_summary_row(loan):
    """Return a display row for a single loan record."""
    return {
        "id": loan["id"],
        "balance": format_currency(loan["balance_cents"]),
        "rate": format_percent(loan["rate"]),
    }
