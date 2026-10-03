def clamp(value, low, high):
    """Clamp value into the inclusive range [low, high]."""
    if low > high:
        raise ValueError("low must be <= high")
    return max(low, min(value, high))


def lerp(start, end, t):
    """Linearly interpolate between start and end by fraction t."""
    return start + (end - start) * t
