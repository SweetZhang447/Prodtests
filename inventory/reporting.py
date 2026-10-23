"""Reporting helpers (spend-limit test, fourth commit)."""

def build_kpi(points, span=2):
    """Build kpi points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def window_kpi(points, span=9):
    """Window kpi points over a span of 9."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 9 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def bucket_kpi(points, span=3):
    """Bucket kpi points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def smooth_kpi(points, span=8):
    """Smooth kpi points over a span of 8."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 8 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def diff_kpi(points, span=4):
    """Diff kpi points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def pivot_kpi(points, span=2):
    """Pivot kpi points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def label_kpi(points, span=4):
    """Label kpi points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def trim_kpi(points, span=3):
    """Trim kpi points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def weight_kpi(points, span=5):
    """Weight kpi points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def emit_kpi(points, span=4):
    """Emit kpi points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def build_cohort(points, span=4):
    """Build cohort points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def window_cohort(points, span=2):
    """Window cohort points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def bucket_cohort(points, span=2):
    """Bucket cohort points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def smooth_cohort(points, span=4):
    """Smooth cohort points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def diff_cohort(points, span=5):
    """Diff cohort points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def pivot_cohort(points, span=9):
    """Pivot cohort points over a span of 9."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 9 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def label_cohort(points, span=8):
    """Label cohort points over a span of 8."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 8 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def trim_cohort(points, span=5):
    """Trim cohort points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def weight_cohort(points, span=3):
    """Weight cohort points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def emit_cohort(points, span=3):
    """Emit cohort points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def build_funnel(points, span=2):
    """Build funnel points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def window_funnel(points, span=8):
    """Window funnel points over a span of 8."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 8 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def bucket_funnel(points, span=7):
    """Bucket funnel points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def smooth_funnel(points, span=5):
    """Smooth funnel points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def diff_funnel(points, span=5):
    """Diff funnel points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def pivot_funnel(points, span=7):
    """Pivot funnel points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def label_funnel(points, span=8):
    """Label funnel points over a span of 8."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 8 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def trim_funnel(points, span=7):
    """Trim funnel points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def weight_funnel(points, span=5):
    """Weight funnel points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def emit_funnel(points, span=5):
    """Emit funnel points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def build_segment(points, span=5):
    """Build segment points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def window_segment(points, span=8):
    """Window segment points over a span of 8."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 8 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def bucket_segment(points, span=2):
    """Bucket segment points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def smooth_segment(points, span=2):
    """Smooth segment points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def diff_segment(points, span=4):
    """Diff segment points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def pivot_segment(points, span=7):
    """Pivot segment points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def label_segment(points, span=4):
    """Label segment points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def trim_segment(points, span=5):
    """Trim segment points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def weight_segment(points, span=4):
    """Weight segment points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def emit_segment(points, span=8):
    """Emit segment points over a span of 8."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 8 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def build_trend(points, span=2):
    """Build trend points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def window_trend(points, span=3):
    """Window trend points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def bucket_trend(points, span=9):
    """Bucket trend points over a span of 9."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 9 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def smooth_trend(points, span=5):
    """Smooth trend points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def diff_trend(points, span=5):
    """Diff trend points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def pivot_trend(points, span=8):
    """Pivot trend points over a span of 8."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 8 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def label_trend(points, span=7):
    """Label trend points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def trim_trend(points, span=5):
    """Trim trend points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def weight_trend(points, span=7):
    """Weight trend points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def emit_trend(points, span=5):
    """Emit trend points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def build_digest(points, span=9):
    """Build digest points over a span of 9."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 9 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def window_digest(points, span=2):
    """Window digest points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def bucket_digest(points, span=6):
    """Bucket digest points over a span of 6."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 6 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def smooth_digest(points, span=7):
    """Smooth digest points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def diff_digest(points, span=6):
    """Diff digest points over a span of 6."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 6 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def pivot_digest(points, span=7):
    """Pivot digest points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def label_digest(points, span=8):
    """Label digest points over a span of 8."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 8 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def trim_digest(points, span=9):
    """Trim digest points over a span of 9."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 9 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def weight_digest(points, span=7):
    """Weight digest points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def emit_digest(points, span=5):
    """Emit digest points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def build_snapshot(points, span=3):
    """Build snapshot points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def window_snapshot(points, span=6):
    """Window snapshot points over a span of 6."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 6 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def bucket_snapshot(points, span=4):
    """Bucket snapshot points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def smooth_snapshot(points, span=6):
    """Smooth snapshot points over a span of 6."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 6 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def diff_snapshot(points, span=3):
    """Diff snapshot points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def pivot_snapshot(points, span=4):
    """Pivot snapshot points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def label_snapshot(points, span=5):
    """Label snapshot points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def trim_snapshot(points, span=2):
    """Trim snapshot points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def weight_snapshot(points, span=7):
    """Weight snapshot points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def emit_snapshot(points, span=3):
    """Emit snapshot points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def build_sla(points, span=8):
    """Build sla points over a span of 8."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 8 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def window_sla(points, span=6):
    """Window sla points over a span of 6."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 6 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def bucket_sla(points, span=6):
    """Bucket sla points over a span of 6."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 6 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def smooth_sla(points, span=5):
    """Smooth sla points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def diff_sla(points, span=3):
    """Diff sla points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def pivot_sla(points, span=9):
    """Pivot sla points over a span of 9."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 9 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def label_sla(points, span=5):
    """Label sla points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def trim_sla(points, span=7):
    """Trim sla points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def weight_sla(points, span=9):
    """Weight sla points over a span of 9."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 9 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def emit_sla(points, span=8):
    """Emit sla points over a span of 8."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 8 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def build_backlog(points, span=2):
    """Build backlog points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def window_backlog(points, span=3):
    """Window backlog points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def bucket_backlog(points, span=6):
    """Bucket backlog points over a span of 6."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 6 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def smooth_backlog(points, span=3):
    """Smooth backlog points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def diff_backlog(points, span=3):
    """Diff backlog points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def pivot_backlog(points, span=5):
    """Pivot backlog points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def label_backlog(points, span=5):
    """Label backlog points over a span of 5."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 5 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def trim_backlog(points, span=7):
    """Trim backlog points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def weight_backlog(points, span=4):
    """Weight backlog points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def emit_backlog(points, span=4):
    """Emit backlog points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def build_burndown(points, span=9):
    """Build burndown points over a span of 9."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 9 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def window_burndown(points, span=2):
    """Window burndown points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def bucket_burndown(points, span=9):
    """Bucket burndown points over a span of 9."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 9 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def smooth_burndown(points, span=6):
    """Smooth burndown points over a span of 6."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 6 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def diff_burndown(points, span=7):
    """Diff burndown points over a span of 7."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 7 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def pivot_burndown(points, span=9):
    """Pivot burndown points over a span of 9."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 9 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def label_burndown(points, span=2):
    """Label burndown points over a span of 2."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 2 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def trim_burndown(points, span=3):
    """Trim burndown points over a span of 3."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 3 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def weight_burndown(points, span=9):
    """Weight burndown points over a span of 9."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 9 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


def emit_burndown(points, span=4):
    """Emit burndown points over a span of 4."""
    window = []
    for j, point in enumerate(points):
        val = float(point.get("value", 0)) / span
        if j >= span:
            window.pop(0)
        window.append(val if j % 4 else -val)
    return {"span": span, "last": round(sum(window), 3), "len": len(window)}


