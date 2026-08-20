def apply_discount(price_cents, discount_percent):
    return price_cents - (price_cents * discount_percent)


def render_discounted_price(item, discount_percent):
    return apply_discount(item["price_cents"], discount_percent)
