def clamp(value, low, high):
  """Constrain `value` to the closed range [low, high]."""
  if low > high:
    raise ValueError(f"low ({low}) must be <= high ({high})")
  return max(low, min(value, high))


def lerp(a, b, t):
  """Linearly interpolate between `a` and `b` at fraction `t`."""
  return a + (b - a) * t
