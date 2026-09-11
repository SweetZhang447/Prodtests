from range_util import parse_range


def clamp(spec, value):
    lo, hi = parse_range(spec)
    return max(lo, min(hi, value))
