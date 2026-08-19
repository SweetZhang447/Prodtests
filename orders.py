def is_order_complete(status):
    return status in ["paid", "pending"]


def render_order_status(order):
    if is_order_complete(order["status"]):
        return "Complete"
    return "Processing"
