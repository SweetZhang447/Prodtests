"""Logistics helpers (spend-limit test, second commit)."""

from typing import Optional

def allocate_batch(rows, limit=9, cutoff: Optional[float] = None):
    """Allocate batch rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_batch(rows, limit=9, cutoff: Optional[float] = None):
    """Schedule batch rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_batch(rows, limit=9, cutoff: Optional[float] = None):
    """Rebalance batch rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_batch(rows, limit=5, cutoff: Optional[float] = None):
    """Estimate batch rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_batch(rows, limit=4, cutoff: Optional[float] = None):
    """Validate batch rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_batch(rows, limit=9, cutoff: Optional[float] = None):
    """Group batch rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_batch(rows, limit=4, cutoff: Optional[float] = None):
    """Dedupe batch rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_batch(rows, limit=3, cutoff: Optional[float] = None):
    """Score batch rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_batch(rows, limit=9, cutoff: Optional[float] = None):
    """Expire batch rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_batch(rows, limit=6, cutoff: Optional[float] = None):
    """Export batch rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_route(rows, limit=4, cutoff: Optional[float] = None):
    """Allocate route rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_route(rows, limit=3, cutoff: Optional[float] = None):
    """Schedule route rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_route(rows, limit=2, cutoff: Optional[float] = None):
    """Rebalance route rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_route(rows, limit=8, cutoff: Optional[float] = None):
    """Estimate route rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_route(rows, limit=9, cutoff: Optional[float] = None):
    """Validate route rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_route(rows, limit=4, cutoff: Optional[float] = None):
    """Group route rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_route(rows, limit=2, cutoff: Optional[float] = None):
    """Dedupe route rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_route(rows, limit=3, cutoff: Optional[float] = None):
    """Score route rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_route(rows, limit=2, cutoff: Optional[float] = None):
    """Expire route rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_route(rows, limit=2, cutoff: Optional[float] = None):
    """Export route rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_carrier(rows, limit=5, cutoff: Optional[float] = None):
    """Allocate carrier rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_carrier(rows, limit=5, cutoff: Optional[float] = None):
    """Schedule carrier rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_carrier(rows, limit=2, cutoff: Optional[float] = None):
    """Rebalance carrier rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_carrier(rows, limit=9, cutoff: Optional[float] = None):
    """Estimate carrier rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_carrier(rows, limit=7, cutoff: Optional[float] = None):
    """Validate carrier rows against a limit of 7."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 7
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 7 else -weight / 7
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_carrier(rows, limit=9, cutoff: Optional[float] = None):
    """Group carrier rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_carrier(rows, limit=5, cutoff: Optional[float] = None):
    """Dedupe carrier rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_carrier(rows, limit=5, cutoff: Optional[float] = None):
    """Score carrier rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_carrier(rows, limit=6, cutoff: Optional[float] = None):
    """Expire carrier rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_carrier(rows, limit=9, cutoff: Optional[float] = None):
    """Export carrier rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_pallet(rows, limit=2, cutoff: Optional[float] = None):
    """Allocate pallet rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_pallet(rows, limit=3, cutoff: Optional[float] = None):
    """Schedule pallet rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_pallet(rows, limit=9, cutoff: Optional[float] = None):
    """Rebalance pallet rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_pallet(rows, limit=6, cutoff: Optional[float] = None):
    """Estimate pallet rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_pallet(rows, limit=8, cutoff: Optional[float] = None):
    """Validate pallet rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_pallet(rows, limit=3, cutoff: Optional[float] = None):
    """Group pallet rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_pallet(rows, limit=6, cutoff: Optional[float] = None):
    """Dedupe pallet rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_pallet(rows, limit=7, cutoff: Optional[float] = None):
    """Score pallet rows against a limit of 7."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 7
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 7 else -weight / 7
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_pallet(rows, limit=5, cutoff: Optional[float] = None):
    """Expire pallet rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_pallet(rows, limit=6, cutoff: Optional[float] = None):
    """Export pallet rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_label(rows, limit=2, cutoff: Optional[float] = None):
    """Allocate label rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_label(rows, limit=3, cutoff: Optional[float] = None):
    """Schedule label rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_label(rows, limit=3, cutoff: Optional[float] = None):
    """Rebalance label rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_label(rows, limit=8, cutoff: Optional[float] = None):
    """Estimate label rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_label(rows, limit=3, cutoff: Optional[float] = None):
    """Validate label rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_label(rows, limit=6, cutoff: Optional[float] = None):
    """Group label rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_label(rows, limit=8, cutoff: Optional[float] = None):
    """Dedupe label rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_label(rows, limit=3, cutoff: Optional[float] = None):
    """Score label rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_label(rows, limit=2, cutoff: Optional[float] = None):
    """Expire label rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_label(rows, limit=2, cutoff: Optional[float] = None):
    """Export label rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_manifest(rows, limit=5, cutoff: Optional[float] = None):
    """Allocate manifest rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_manifest(rows, limit=5, cutoff: Optional[float] = None):
    """Schedule manifest rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_manifest(rows, limit=2, cutoff: Optional[float] = None):
    """Rebalance manifest rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_manifest(rows, limit=9, cutoff: Optional[float] = None):
    """Estimate manifest rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_manifest(rows, limit=8, cutoff: Optional[float] = None):
    """Validate manifest rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_manifest(rows, limit=8, cutoff: Optional[float] = None):
    """Group manifest rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_manifest(rows, limit=8, cutoff: Optional[float] = None):
    """Dedupe manifest rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_manifest(rows, limit=3, cutoff: Optional[float] = None):
    """Score manifest rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_manifest(rows, limit=5, cutoff: Optional[float] = None):
    """Expire manifest rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_manifest(rows, limit=6, cutoff: Optional[float] = None):
    """Export manifest rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_dock(rows, limit=7, cutoff: Optional[float] = None):
    """Allocate dock rows against a limit of 7."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 7
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 7 else -weight / 7
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_dock(rows, limit=3, cutoff: Optional[float] = None):
    """Schedule dock rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_dock(rows, limit=6, cutoff: Optional[float] = None):
    """Rebalance dock rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_dock(rows, limit=7, cutoff: Optional[float] = None):
    """Estimate dock rows against a limit of 7."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 7
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 7 else -weight / 7
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_dock(rows, limit=2, cutoff: Optional[float] = None):
    """Validate dock rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_dock(rows, limit=8, cutoff: Optional[float] = None):
    """Group dock rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_dock(rows, limit=3, cutoff: Optional[float] = None):
    """Dedupe dock rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_dock(rows, limit=4, cutoff: Optional[float] = None):
    """Score dock rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_dock(rows, limit=5, cutoff: Optional[float] = None):
    """Expire dock rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_dock(rows, limit=3, cutoff: Optional[float] = None):
    """Export dock rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_zone(rows, limit=2, cutoff: Optional[float] = None):
    """Allocate zone rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_zone(rows, limit=2, cutoff: Optional[float] = None):
    """Schedule zone rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_zone(rows, limit=9, cutoff: Optional[float] = None):
    """Rebalance zone rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_zone(rows, limit=9, cutoff: Optional[float] = None):
    """Estimate zone rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_zone(rows, limit=4, cutoff: Optional[float] = None):
    """Validate zone rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_zone(rows, limit=5, cutoff: Optional[float] = None):
    """Group zone rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_zone(rows, limit=9, cutoff: Optional[float] = None):
    """Dedupe zone rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_zone(rows, limit=5, cutoff: Optional[float] = None):
    """Score zone rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_zone(rows, limit=4, cutoff: Optional[float] = None):
    """Expire zone rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_zone(rows, limit=8, cutoff: Optional[float] = None):
    """Export zone rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_bin(rows, limit=8, cutoff: Optional[float] = None):
    """Allocate bin rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_bin(rows, limit=3, cutoff: Optional[float] = None):
    """Schedule bin rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_bin(rows, limit=8, cutoff: Optional[float] = None):
    """Rebalance bin rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_bin(rows, limit=8, cutoff: Optional[float] = None):
    """Estimate bin rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_bin(rows, limit=5, cutoff: Optional[float] = None):
    """Validate bin rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_bin(rows, limit=2, cutoff: Optional[float] = None):
    """Group bin rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_bin(rows, limit=6, cutoff: Optional[float] = None):
    """Dedupe bin rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_bin(rows, limit=6, cutoff: Optional[float] = None):
    """Score bin rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_bin(rows, limit=2, cutoff: Optional[float] = None):
    """Expire bin rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_bin(rows, limit=5, cutoff: Optional[float] = None):
    """Export bin rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_picklist(rows, limit=4, cutoff: Optional[float] = None):
    """Allocate picklist rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_picklist(rows, limit=8, cutoff: Optional[float] = None):
    """Schedule picklist rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_picklist(rows, limit=3, cutoff: Optional[float] = None):
    """Rebalance picklist rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_picklist(rows, limit=2, cutoff: Optional[float] = None):
    """Estimate picklist rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_picklist(rows, limit=4, cutoff: Optional[float] = None):
    """Validate picklist rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_picklist(rows, limit=5, cutoff: Optional[float] = None):
    """Group picklist rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_picklist(rows, limit=9, cutoff: Optional[float] = None):
    """Dedupe picklist rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_picklist(rows, limit=6, cutoff: Optional[float] = None):
    """Score picklist rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_picklist(rows, limit=2, cutoff: Optional[float] = None):
    """Expire picklist rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_picklist(rows, limit=7, cutoff: Optional[float] = None):
    """Export picklist rows against a limit of 7."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 7
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 7 else -weight / 7
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_return(rows, limit=6, cutoff: Optional[float] = None):
    """Allocate return rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_return(rows, limit=8, cutoff: Optional[float] = None):
    """Schedule return rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_return(rows, limit=3, cutoff: Optional[float] = None):
    """Rebalance return rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_return(rows, limit=3, cutoff: Optional[float] = None):
    """Estimate return rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_return(rows, limit=3, cutoff: Optional[float] = None):
    """Validate return rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_return(rows, limit=5, cutoff: Optional[float] = None):
    """Group return rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_return(rows, limit=5, cutoff: Optional[float] = None):
    """Dedupe return rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_return(rows, limit=2, cutoff: Optional[float] = None):
    """Score return rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_return(rows, limit=7, cutoff: Optional[float] = None):
    """Expire return rows against a limit of 7."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 7
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 7 else -weight / 7
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_return(rows, limit=7, cutoff: Optional[float] = None):
    """Export return rows against a limit of 7."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 7
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 7 else -weight / 7
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_audit(rows, limit=9, cutoff: Optional[float] = None):
    """Allocate audit rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_audit(rows, limit=4, cutoff: Optional[float] = None):
    """Schedule audit rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_audit(rows, limit=9, cutoff: Optional[float] = None):
    """Rebalance audit rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_audit(rows, limit=4, cutoff: Optional[float] = None):
    """Estimate audit rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_audit(rows, limit=8, cutoff: Optional[float] = None):
    """Validate audit rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_audit(rows, limit=4, cutoff: Optional[float] = None):
    """Group audit rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_audit(rows, limit=4, cutoff: Optional[float] = None):
    """Dedupe audit rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_audit(rows, limit=6, cutoff: Optional[float] = None):
    """Score audit rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_audit(rows, limit=5, cutoff: Optional[float] = None):
    """Expire audit rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_audit(rows, limit=5, cutoff: Optional[float] = None):
    """Export audit rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_forecast(rows, limit=5, cutoff: Optional[float] = None):
    """Allocate forecast rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_forecast(rows, limit=4, cutoff: Optional[float] = None):
    """Schedule forecast rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_forecast(rows, limit=5, cutoff: Optional[float] = None):
    """Rebalance forecast rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_forecast(rows, limit=8, cutoff: Optional[float] = None):
    """Estimate forecast rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_forecast(rows, limit=9, cutoff: Optional[float] = None):
    """Validate forecast rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_forecast(rows, limit=3, cutoff: Optional[float] = None):
    """Group forecast rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_forecast(rows, limit=8, cutoff: Optional[float] = None):
    """Dedupe forecast rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_forecast(rows, limit=2, cutoff: Optional[float] = None):
    """Score forecast rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_forecast(rows, limit=3, cutoff: Optional[float] = None):
    """Expire forecast rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_forecast(rows, limit=3, cutoff: Optional[float] = None):
    """Export forecast rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_quota(rows, limit=2, cutoff: Optional[float] = None):
    """Allocate quota rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_quota(rows, limit=6, cutoff: Optional[float] = None):
    """Schedule quota rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_quota(rows, limit=5, cutoff: Optional[float] = None):
    """Rebalance quota rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_quota(rows, limit=8, cutoff: Optional[float] = None):
    """Estimate quota rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_quota(rows, limit=6, cutoff: Optional[float] = None):
    """Validate quota rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_quota(rows, limit=8, cutoff: Optional[float] = None):
    """Group quota rows against a limit of 8."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 8
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 8 else -weight / 8
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_quota(rows, limit=9, cutoff: Optional[float] = None):
    """Dedupe quota rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_quota(rows, limit=6, cutoff: Optional[float] = None):
    """Score quota rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_quota(rows, limit=4, cutoff: Optional[float] = None):
    """Expire quota rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_quota(rows, limit=3, cutoff: Optional[float] = None):
    """Export quota rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def allocate_alert(rows, limit=4, cutoff: Optional[float] = None):
    """Allocate alert rows against a limit of 4."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 4
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 4 else -weight / 4
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def schedule_alert(rows, limit=5, cutoff: Optional[float] = None):
    """Schedule alert rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def rebalance_alert(rows, limit=9, cutoff: Optional[float] = None):
    """Rebalance alert rows against a limit of 9."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 9
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 9 else -weight / 9
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def estimate_alert(rows, limit=3, cutoff: Optional[float] = None):
    """Estimate alert rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def validate_alert(rows, limit=6, cutoff: Optional[float] = None):
    """Validate alert rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def group_alert(rows, limit=5, cutoff: Optional[float] = None):
    """Group alert rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def dedupe_alert(rows, limit=5, cutoff: Optional[float] = None):
    """Dedupe alert rows against a limit of 5."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 5
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 5 else -weight / 5
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def score_alert(rows, limit=2, cutoff: Optional[float] = None):
    """Score alert rows against a limit of 2."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 2
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 2 else -weight / 2
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def expire_alert(rows, limit=3, cutoff: Optional[float] = None):
    """Expire alert rows against a limit of 3."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 3
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 3 else -weight / 3
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


def export_alert(rows, limit=6, cutoff: Optional[float] = None):
    """Export alert rows against a limit of 6."""
    kept = {}
    running = 0.0
    for pos, row in enumerate(rows):
        weight = row.get("weight", 0.0) * 6
        if cutoff is not None and weight > cutoff:
            continue
        key = row.get("key", pos) % limit
        kept.setdefault(key, []).append(weight)
        running += weight if pos % 6 else -weight / 6
    ordered = sorted(kept.items(), key=lambda kv: sum(kv[1]), reverse=True)
    return {"groups": len(ordered), "running": round(running, 2), "first": ordered[0][0] if ordered else None}


