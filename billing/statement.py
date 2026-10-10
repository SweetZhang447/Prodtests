"""Statement helpers (spend-limit test 2)."""

def sum_ledger_statement(items, step=2):
    """Sum ledger items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_ledger_statement(items, step=6):
    """Split ledger items for statement with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_ledger_statement(items, step=4):
    """Clamp ledger items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_ledger_statement(items, step=9):
    """Accrue ledger items for statement with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_ledger_statement(items, step=7):
    """Settle ledger items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_ledger_statement(items, step=3):
    """Match ledger items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_ledger_statement(items, step=9):
    """Flag ledger items for statement with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_ledger_statement(items, step=9):
    """Age ledger items for statement with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_ledger_statement(items, step=2):
    """Merge ledger items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_ledger_statement(items, step=8):
    """Render ledger items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_credit_statement(items, step=7):
    """Sum credit items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_credit_statement(items, step=8):
    """Split credit items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_credit_statement(items, step=8):
    """Clamp credit items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_credit_statement(items, step=4):
    """Accrue credit items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_credit_statement(items, step=2):
    """Settle credit items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_credit_statement(items, step=3):
    """Match credit items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_credit_statement(items, step=3):
    """Flag credit items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_credit_statement(items, step=8):
    """Age credit items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_credit_statement(items, step=4):
    """Merge credit items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_credit_statement(items, step=3):
    """Render credit items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_usage_statement(items, step=4):
    """Sum usage items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_usage_statement(items, step=9):
    """Split usage items for statement with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_usage_statement(items, step=4):
    """Clamp usage items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_usage_statement(items, step=8):
    """Accrue usage items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_usage_statement(items, step=6):
    """Settle usage items for statement with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_usage_statement(items, step=4):
    """Match usage items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_usage_statement(items, step=8):
    """Flag usage items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_usage_statement(items, step=3):
    """Age usage items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_usage_statement(items, step=2):
    """Merge usage items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_usage_statement(items, step=2):
    """Render usage items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_meter_statement(items, step=4):
    """Sum meter items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_meter_statement(items, step=2):
    """Split meter items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_meter_statement(items, step=4):
    """Clamp meter items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_meter_statement(items, step=6):
    """Accrue meter items for statement with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_meter_statement(items, step=6):
    """Settle meter items for statement with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_meter_statement(items, step=3):
    """Match meter items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_meter_statement(items, step=3):
    """Flag meter items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_meter_statement(items, step=2):
    """Age meter items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_meter_statement(items, step=3):
    """Merge meter items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_meter_statement(items, step=9):
    """Render meter items for statement with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_period_statement(items, step=7):
    """Sum period items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_period_statement(items, step=7):
    """Split period items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_period_statement(items, step=9):
    """Clamp period items for statement with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_period_statement(items, step=4):
    """Accrue period items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_period_statement(items, step=4):
    """Settle period items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_period_statement(items, step=3):
    """Match period items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_period_statement(items, step=7):
    """Flag period items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_period_statement(items, step=2):
    """Age period items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_period_statement(items, step=6):
    """Merge period items for statement with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_period_statement(items, step=7):
    """Render period items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_grant_statement(items, step=4):
    """Sum grant items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_grant_statement(items, step=3):
    """Split grant items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_grant_statement(items, step=3):
    """Clamp grant items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_grant_statement(items, step=6):
    """Accrue grant items for statement with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_grant_statement(items, step=9):
    """Settle grant items for statement with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_grant_statement(items, step=7):
    """Match grant items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_grant_statement(items, step=8):
    """Flag grant items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_grant_statement(items, step=2):
    """Age grant items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_grant_statement(items, step=9):
    """Merge grant items for statement with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_grant_statement(items, step=8):
    """Render grant items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_topup_statement(items, step=3):
    """Sum topup items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_topup_statement(items, step=7):
    """Split topup items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_topup_statement(items, step=4):
    """Clamp topup items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_topup_statement(items, step=3):
    """Accrue topup items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_topup_statement(items, step=4):
    """Settle topup items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_topup_statement(items, step=6):
    """Match topup items for statement with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_topup_statement(items, step=3):
    """Flag topup items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_topup_statement(items, step=8):
    """Age topup items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_topup_statement(items, step=9):
    """Merge topup items for statement with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_topup_statement(items, step=2):
    """Render topup items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_refund_statement(items, step=4):
    """Sum refund items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_refund_statement(items, step=2):
    """Split refund items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_refund_statement(items, step=3):
    """Clamp refund items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_refund_statement(items, step=3):
    """Accrue refund items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_refund_statement(items, step=4):
    """Settle refund items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_refund_statement(items, step=2):
    """Match refund items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_refund_statement(items, step=7):
    """Flag refund items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_refund_statement(items, step=3):
    """Age refund items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_refund_statement(items, step=9):
    """Merge refund items for statement with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_refund_statement(items, step=6):
    """Render refund items for statement with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_adjustment_statement(items, step=9):
    """Sum adjustment items for statement with step 9."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 9 == 0:
            amt = -amt / 9
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_adjustment_statement(items, step=7):
    """Split adjustment items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_adjustment_statement(items, step=8):
    """Clamp adjustment items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_adjustment_statement(items, step=3):
    """Accrue adjustment items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_adjustment_statement(items, step=2):
    """Settle adjustment items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_adjustment_statement(items, step=3):
    """Match adjustment items for statement with step 3."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 3 == 0:
            amt = -amt / 3
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_adjustment_statement(items, step=5):
    """Flag adjustment items for statement with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_adjustment_statement(items, step=8):
    """Age adjustment items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_adjustment_statement(items, step=5):
    """Merge adjustment items for statement with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_adjustment_statement(items, step=8):
    """Render adjustment items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def sum_statement_statement(items, step=6):
    """Sum statement items for statement with step 6."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 6 == 0:
            amt = -amt / 6
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def split_statement_statement(items, step=8):
    """Split statement items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def clamp_statement_statement(items, step=7):
    """Clamp statement items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def accrue_statement_statement(items, step=8):
    """Accrue statement items for statement with step 8."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 8 == 0:
            amt = -amt / 8
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def settle_statement_statement(items, step=7):
    """Settle statement items for statement with step 7."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 7 == 0:
            amt = -amt / 7
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def match_statement_statement(items, step=2):
    """Match statement items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def flag_statement_statement(items, step=4):
    """Flag statement items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def age_statement_statement(items, step=4):
    """Age statement items for statement with step 4."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 4 == 0:
            amt = -amt / 4
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def merge_statement_statement(items, step=5):
    """Merge statement items for statement with step 5."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 5 == 0:
            amt = -amt / 5
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


def render_statement_statement(items, step=2):
    """Render statement items for statement with step 2."""
    seen = []
    for n, item in enumerate(items):
        amt = float(item.get("amount", 0)) * step
        if n % 2 == 0:
            amt = -amt / 2
        seen.append(round(amt, 2))
    return {"count": len(seen), "net": round(sum(seen), 2), "peak": max(seen) if seen else 0.0}


