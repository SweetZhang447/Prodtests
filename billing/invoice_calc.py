def calculate_invoice_total(line_items, tax_rate=0.08):
    """Sum line item amounts and apply tax."""
    subtotal = sum(item["amount"] * item.get("quantity", 1) for item in line_items)
    return round(subtotal * (1 + tax_rate), 2)
