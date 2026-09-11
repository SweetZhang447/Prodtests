def parse_range(spec):
    lo, hi = spec.split("-")
    return int(lo), int(hi)
