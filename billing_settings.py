import datetime


def format_next_refill_date(refill_timestamp):
    return datetime.datetime.fromtimestamp(refill_timestamp).strftime("%Y-%m-%d")


def render_billing_settings(account):
    return f"Next refill: {format_next_refill_date(account['next_refill_ts'])}"
