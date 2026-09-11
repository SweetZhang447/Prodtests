def to_cents(amount):
    return int(round(amount * 100))


def from_cents(cents):
    return cents / 100


def split_bill(total_cents, people):
    share = total_cents // people
    return [share] * people


def apply_tip(total_cents, pct):
    return total_cents + (total_cents * pct / 100)
