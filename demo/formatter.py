"""Small helpers for formatting values in reports."""


def format_currency(cents):
    """Render an integer number of cents as a dollar string."""
    return f"${cents / 100:.2f}"


def format_percent(fraction, digits=1):
    """Render a 0..1 fraction as a percentage string."""
    return f"{fraction * 100:.{digits}f}%"
