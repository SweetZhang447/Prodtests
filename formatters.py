def format_currency(amount_cents, symbol="$"):
  """Format an integer amount of cents as a currency string, e.g. 1050 -> '$10.50'."""
  sign = "-" if amount_cents < 0 else ""
  cents = abs(amount_cents)
  dollars, remainder = divmod(cents, 100)
  return f"{sign}{symbol}{dollars}.{remainder:02d}"


def format_percentage(fraction, decimals=1):
  """Format a 0-1 fraction as a percentage string, e.g. 0.256 -> '25.6%'."""
  return f"{fraction * 100:.{decimals}f}%"
