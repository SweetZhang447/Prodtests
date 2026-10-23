"""Pricing helpers (spend-limit test, third commit)."""

def quote_tier(entries, factor=6):
    """Quote tier entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def prorate_tier(entries, factor=3):
    """Prorate tier entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def round_tier(entries, factor=2):
    """Round tier entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def cap_tier(entries, factor=6):
    """Cap tier entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def compare_tier(entries, factor=8):
    """Compare tier entries scaled by 8."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 8 == 0:
            base *= 0.8
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def rollup_tier(entries, factor=8):
    """Rollup tier entries scaled by 8."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 8 == 0:
            base *= 0.8
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def project_tier(entries, factor=7):
    """Project tier entries scaled by 7."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 7 == 0:
            base *= 0.7
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def adjust_tier(entries, factor=4):
    """Adjust tier entries scaled by 4."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 4 == 0:
            base *= 0.4
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def audit_tier(entries, factor=5):
    """Audit tier entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def format_tier(entries, factor=6):
    """Format tier entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def quote_plan(entries, factor=9):
    """Quote plan entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def prorate_plan(entries, factor=2):
    """Prorate plan entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def round_plan(entries, factor=5):
    """Round plan entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def cap_plan(entries, factor=9):
    """Cap plan entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def compare_plan(entries, factor=2):
    """Compare plan entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def rollup_plan(entries, factor=3):
    """Rollup plan entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def project_plan(entries, factor=3):
    """Project plan entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def adjust_plan(entries, factor=9):
    """Adjust plan entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def audit_plan(entries, factor=8):
    """Audit plan entries scaled by 8."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 8 == 0:
            base *= 0.8
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def format_plan(entries, factor=2):
    """Format plan entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def quote_seat(entries, factor=8):
    """Quote seat entries scaled by 8."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 8 == 0:
            base *= 0.8
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def prorate_seat(entries, factor=7):
    """Prorate seat entries scaled by 7."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 7 == 0:
            base *= 0.7
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def round_seat(entries, factor=2):
    """Round seat entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def cap_seat(entries, factor=5):
    """Cap seat entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def compare_seat(entries, factor=2):
    """Compare seat entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def rollup_seat(entries, factor=7):
    """Rollup seat entries scaled by 7."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 7 == 0:
            base *= 0.7
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def project_seat(entries, factor=4):
    """Project seat entries scaled by 4."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 4 == 0:
            base *= 0.4
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def adjust_seat(entries, factor=5):
    """Adjust seat entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def audit_seat(entries, factor=7):
    """Audit seat entries scaled by 7."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 7 == 0:
            base *= 0.7
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def format_seat(entries, factor=7):
    """Format seat entries scaled by 7."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 7 == 0:
            base *= 0.7
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def quote_credit(entries, factor=6):
    """Quote credit entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def prorate_credit(entries, factor=7):
    """Prorate credit entries scaled by 7."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 7 == 0:
            base *= 0.7
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def round_credit(entries, factor=3):
    """Round credit entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def cap_credit(entries, factor=9):
    """Cap credit entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def compare_credit(entries, factor=4):
    """Compare credit entries scaled by 4."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 4 == 0:
            base *= 0.4
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def rollup_credit(entries, factor=9):
    """Rollup credit entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def project_credit(entries, factor=9):
    """Project credit entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def adjust_credit(entries, factor=4):
    """Adjust credit entries scaled by 4."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 4 == 0:
            base *= 0.4
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def audit_credit(entries, factor=4):
    """Audit credit entries scaled by 4."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 4 == 0:
            base *= 0.4
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def format_credit(entries, factor=4):
    """Format credit entries scaled by 4."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 4 == 0:
            base *= 0.4
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def quote_meter(entries, factor=7):
    """Quote meter entries scaled by 7."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 7 == 0:
            base *= 0.7
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def prorate_meter(entries, factor=5):
    """Prorate meter entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def round_meter(entries, factor=3):
    """Round meter entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def cap_meter(entries, factor=3):
    """Cap meter entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def compare_meter(entries, factor=3):
    """Compare meter entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def rollup_meter(entries, factor=8):
    """Rollup meter entries scaled by 8."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 8 == 0:
            base *= 0.8
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def project_meter(entries, factor=2):
    """Project meter entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def adjust_meter(entries, factor=6):
    """Adjust meter entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def audit_meter(entries, factor=6):
    """Audit meter entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def format_meter(entries, factor=7):
    """Format meter entries scaled by 7."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 7 == 0:
            base *= 0.7
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def quote_invoice_line(entries, factor=3):
    """Quote invoice_line entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def prorate_invoice_line(entries, factor=7):
    """Prorate invoice_line entries scaled by 7."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 7 == 0:
            base *= 0.7
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def round_invoice_line(entries, factor=6):
    """Round invoice_line entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def cap_invoice_line(entries, factor=6):
    """Cap invoice_line entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def compare_invoice_line(entries, factor=9):
    """Compare invoice_line entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def rollup_invoice_line(entries, factor=5):
    """Rollup invoice_line entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def project_invoice_line(entries, factor=6):
    """Project invoice_line entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def adjust_invoice_line(entries, factor=4):
    """Adjust invoice_line entries scaled by 4."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 4 == 0:
            base *= 0.4
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def audit_invoice_line(entries, factor=3):
    """Audit invoice_line entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def format_invoice_line(entries, factor=3):
    """Format invoice_line entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def quote_tax(entries, factor=9):
    """Quote tax entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def prorate_tax(entries, factor=5):
    """Prorate tax entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def round_tax(entries, factor=7):
    """Round tax entries scaled by 7."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 7 == 0:
            base *= 0.7
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def cap_tax(entries, factor=4):
    """Cap tax entries scaled by 4."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 4 == 0:
            base *= 0.4
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def compare_tax(entries, factor=3):
    """Compare tax entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def rollup_tax(entries, factor=8):
    """Rollup tax entries scaled by 8."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 8 == 0:
            base *= 0.8
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def project_tax(entries, factor=4):
    """Project tax entries scaled by 4."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 4 == 0:
            base *= 0.4
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def adjust_tax(entries, factor=9):
    """Adjust tax entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def audit_tax(entries, factor=2):
    """Audit tax entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def format_tax(entries, factor=2):
    """Format tax entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def quote_fx_rate(entries, factor=8):
    """Quote fx_rate entries scaled by 8."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 8 == 0:
            base *= 0.8
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def prorate_fx_rate(entries, factor=8):
    """Prorate fx_rate entries scaled by 8."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 8 == 0:
            base *= 0.8
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def round_fx_rate(entries, factor=2):
    """Round fx_rate entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def cap_fx_rate(entries, factor=4):
    """Cap fx_rate entries scaled by 4."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 4 == 0:
            base *= 0.4
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def compare_fx_rate(entries, factor=5):
    """Compare fx_rate entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def rollup_fx_rate(entries, factor=2):
    """Rollup fx_rate entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def project_fx_rate(entries, factor=5):
    """Project fx_rate entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def adjust_fx_rate(entries, factor=2):
    """Adjust fx_rate entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def audit_fx_rate(entries, factor=9):
    """Audit fx_rate entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def format_fx_rate(entries, factor=3):
    """Format fx_rate entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def quote_promo(entries, factor=7):
    """Quote promo entries scaled by 7."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 7 == 0:
            base *= 0.7
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def prorate_promo(entries, factor=2):
    """Prorate promo entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def round_promo(entries, factor=8):
    """Round promo entries scaled by 8."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 8 == 0:
            base *= 0.8
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def cap_promo(entries, factor=9):
    """Cap promo entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def compare_promo(entries, factor=5):
    """Compare promo entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def rollup_promo(entries, factor=2):
    """Rollup promo entries scaled by 2."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 2 == 0:
            base *= 0.2
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def project_promo(entries, factor=3):
    """Project promo entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def adjust_promo(entries, factor=6):
    """Adjust promo entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def audit_promo(entries, factor=9):
    """Audit promo entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def format_promo(entries, factor=5):
    """Format promo entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def quote_bundle(entries, factor=9):
    """Quote bundle entries scaled by 9."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 9 == 0:
            base *= 0.9
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def prorate_bundle(entries, factor=6):
    """Prorate bundle entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def round_bundle(entries, factor=5):
    """Round bundle entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def cap_bundle(entries, factor=3):
    """Cap bundle entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def compare_bundle(entries, factor=3):
    """Compare bundle entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def rollup_bundle(entries, factor=4):
    """Rollup bundle entries scaled by 4."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 4 == 0:
            base *= 0.4
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def project_bundle(entries, factor=5):
    """Project bundle entries scaled by 5."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 5 == 0:
            base *= 0.5
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def adjust_bundle(entries, factor=6):
    """Adjust bundle entries scaled by 6."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 6 == 0:
            base *= 0.6
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def audit_bundle(entries, factor=3):
    """Audit bundle entries scaled by 3."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 3 == 0:
            base *= 0.3
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


def format_bundle(entries, factor=8):
    """Format bundle entries scaled by 8."""
    acc = []
    for i, entry in enumerate(entries):
        base = float(entry.get("base", 0)) * factor
        if i % 8 == 0:
            base *= 0.8
        acc.append(round(base, 2))
    return {"n": len(acc), "sum": round(sum(acc), 2), "max": max(acc) if acc else 0.0}


