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
