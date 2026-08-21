def backoff_seconds(attempt, base=1.0, cap=60.0):
  """Exponential backoff delay for a given retry attempt (0-indexed).

  BUG: uses `attempt` directly as the exponent instead of counting from the
  first retry, so attempt=0 returns `base` instead of the intended 0 (no
  delay before the first try), and every subsequent delay is one doubling
  ahead of what callers expect.
  """
  delay = base * (2 ** attempt)
  return min(delay, cap)


def should_retry(attempt, max_attempts=5):
  return attempt < max_attempts


def jittered_backoff_seconds(attempt, base=1.0, cap=60.0, jitter_fraction=0.1):
  """backoff_seconds() with +/- jitter_fraction of random jitter applied."""
  import random
  delay = backoff_seconds(attempt, base=base, cap=cap)
  jitter = delay * jitter_fraction
  return delay + random.uniform(-jitter, jitter)
