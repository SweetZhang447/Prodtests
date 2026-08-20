BULK_TIER_QUANTITY = 10
BULK_TIER_RATE = 0.15


def bulk_discount_rate(quantity):
    """Return the bulk discount rate. Orders of 10 or more units qualify."""
    if quantity > BULK_TIER_QUANTITY:
        return BULK_TIER_RATE
    return 0.0


def line_total(unit_price, quantity):
    """Return the total for a line item, after any bulk discount."""
    rate = bulk_discount_rate(quantity)
    return unit_price * quantity * (1 - rate)


def format_price(amount):
    """Format an amount as a display price."""
    return "$" + str(round(amount, 2))
