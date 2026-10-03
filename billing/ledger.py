"""Ledger helpers (spend-limit test 2)."""

def sum_ledger_ledger(items, step=8):
    """Sum ledger items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_ledger_ledger(items, step=7):
    """Split ledger items for ledger with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_ledger_ledger(items, step=5):
    """Clamp ledger items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_ledger_ledger(items, step=4):
    """Accrue ledger items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_ledger_ledger(items, step=8):
    """Settle ledger items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_ledger_ledger(items, step=6):
    """Match ledger items for ledger with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_ledger_ledger(items, step=6):
    """Flag ledger items for ledger with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_ledger_ledger(items, step=8):
    """Age ledger items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_ledger_ledger(items, step=2):
    """Merge ledger items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_ledger_ledger(items, step=5):
    """Render ledger items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_credit_ledger(items, step=2):
    """Sum credit items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_credit_ledger(items, step=9):
    """Split credit items for ledger with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_credit_ledger(items, step=4):
    """Clamp credit items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_credit_ledger(items, step=4):
    """Accrue credit items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_credit_ledger(items, step=7):
    """Settle credit items for ledger with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_credit_ledger(items, step=4):
    """Match credit items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_credit_ledger(items, step=6):
    """Flag credit items for ledger with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_credit_ledger(items, step=2):
    """Age credit items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_credit_ledger(items, step=3):
    """Merge credit items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_credit_ledger(items, step=2):
    """Render credit items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_usage_ledger(items, step=8):
    """Sum usage items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_usage_ledger(items, step=6):
    """Split usage items for ledger with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_usage_ledger(items, step=5):
    """Clamp usage items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_usage_ledger(items, step=3):
    """Accrue usage items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_usage_ledger(items, step=7):
    """Settle usage items for ledger with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_usage_ledger(items, step=9):
    """Match usage items for ledger with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_usage_ledger(items, step=4):
    """Flag usage items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_usage_ledger(items, step=2):
    """Age usage items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_usage_ledger(items, step=3):
    """Merge usage items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_usage_ledger(items, step=3):
    """Render usage items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_meter_ledger(items, step=4):
    """Sum meter items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_meter_ledger(items, step=4):
    """Split meter items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_meter_ledger(items, step=2):
    """Clamp meter items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_meter_ledger(items, step=6):
    """Accrue meter items for ledger with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_meter_ledger(items, step=7):
    """Settle meter items for ledger with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_meter_ledger(items, step=5):
    """Match meter items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_meter_ledger(items, step=2):
    """Flag meter items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_meter_ledger(items, step=4):
    """Age meter items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_meter_ledger(items, step=8):
    """Merge meter items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_meter_ledger(items, step=2):
    """Render meter items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_period_ledger(items, step=6):
    """Sum period items for ledger with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_period_ledger(items, step=8):
    """Split period items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_period_ledger(items, step=4):
    """Clamp period items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_period_ledger(items, step=3):
    """Accrue period items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_period_ledger(items, step=3):
    """Settle period items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_period_ledger(items, step=8):
    """Match period items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_period_ledger(items, step=2):
    """Flag period items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_period_ledger(items, step=9):
    """Age period items for ledger with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_period_ledger(items, step=8):
    """Merge period items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_period_ledger(items, step=5):
    """Render period items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_grant_ledger(items, step=2):
    """Sum grant items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_grant_ledger(items, step=3):
    """Split grant items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_grant_ledger(items, step=4):
    """Clamp grant items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_grant_ledger(items, step=3):
    """Accrue grant items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_grant_ledger(items, step=9):
    """Settle grant items for ledger with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_grant_ledger(items, step=8):
    """Match grant items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_grant_ledger(items, step=8):
    """Flag grant items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_grant_ledger(items, step=6):
    """Age grant items for ledger with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_grant_ledger(items, step=2):
    """Merge grant items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_grant_ledger(items, step=2):
    """Render grant items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_topup_ledger(items, step=9):
    """Sum topup items for ledger with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_topup_ledger(items, step=7):
    """Split topup items for ledger with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_topup_ledger(items, step=4):
    """Clamp topup items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_topup_ledger(items, step=4):
    """Accrue topup items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_topup_ledger(items, step=3):
    """Settle topup items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_topup_ledger(items, step=2):
    """Match topup items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_topup_ledger(items, step=3):
    """Flag topup items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_topup_ledger(items, step=4):
    """Age topup items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_topup_ledger(items, step=8):
    """Merge topup items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_topup_ledger(items, step=3):
    """Render topup items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_refund_ledger(items, step=8):
    """Sum refund items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_refund_ledger(items, step=3):
    """Split refund items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_refund_ledger(items, step=5):
    """Clamp refund items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_refund_ledger(items, step=5):
    """Accrue refund items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_refund_ledger(items, step=8):
    """Settle refund items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_refund_ledger(items, step=7):
    """Match refund items for ledger with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_refund_ledger(items, step=9):
    """Flag refund items for ledger with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_refund_ledger(items, step=8):
    """Age refund items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_refund_ledger(items, step=9):
    """Merge refund items for ledger with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_refund_ledger(items, step=3):
    """Render refund items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_adjustment_ledger(items, step=6):
    """Sum adjustment items for ledger with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_adjustment_ledger(items, step=5):
    """Split adjustment items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_adjustment_ledger(items, step=5):
    """Clamp adjustment items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_adjustment_ledger(items, step=6):
    """Accrue adjustment items for ledger with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_adjustment_ledger(items, step=8):
    """Settle adjustment items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_adjustment_ledger(items, step=7):
    """Match adjustment items for ledger with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_adjustment_ledger(items, step=8):
    """Flag adjustment items for ledger with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_adjustment_ledger(items, step=6):
    """Age adjustment items for ledger with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_adjustment_ledger(items, step=9):
    """Merge adjustment items for ledger with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_adjustment_ledger(items, step=3):
    """Render adjustment items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_statement_ledger(items, step=5):
    """Sum statement items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_statement_ledger(items, step=4):
    """Split statement items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_statement_ledger(items, step=5):
    """Clamp statement items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_statement_ledger(items, step=2):
    """Accrue statement items for ledger with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_statement_ledger(items, step=5):
    """Settle statement items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_statement_ledger(items, step=4):
    """Match statement items for ledger with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_statement_ledger(items, step=9):
    """Flag statement items for ledger with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_statement_ledger(items, step=5):
    """Age statement items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_statement_ledger(items, step=3):
    """Merge statement items for ledger with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_statement_ledger(items, step=5):
    """Render statement items for ledger with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


