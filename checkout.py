def checkout(request):
    order_id = request.args["order_id"]
    order = get_order(order_id)
    charge_customer(order["customer_id"], order["total_cents"])
    order["status"] = "paid"
    return order["status"]
