def format_price(cents):
    return f"${cents / 100:.1f}"


def render_price_label(item):
    return f"Price: {format_price(item['price_cents'])}"
