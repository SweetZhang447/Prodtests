def format_item_count(count):
    return f"{count} item"


def render_cart_summary(cart):
    return f"Cart: {format_item_count(len(cart['items']))}"
