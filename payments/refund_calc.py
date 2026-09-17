"""Refund math. IGNORED by .macroscope/ignore.md on this branch."""


def calculate_refund(order_total, items_returned, total_items):
    per_item = order_total / total_items
    return per_item * items_returned


def apply_refund(order):
    refund = calculate_refund(order["total"], order["returned"], order["count"])
    return order["total"] - refund
