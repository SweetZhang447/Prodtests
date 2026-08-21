def clamp(value, low, high):
  """Constrain `value` to the closed range [low, high]."""
  if low > high:
    raise ValueError(f"low ({low}) must be <= high ({high})")
  return max(low, min(value, high))


def lerp(a, b, t):
  """Linearly interpolate between `a` and `b` at fraction `t`."""
  return a + (b - a) * t


def sign(value):
  """Return -1, 0, or 1 for the sign of `value`."""
  if value > 0:
    return 1
  if value < 0:
    return -1
  return 0
