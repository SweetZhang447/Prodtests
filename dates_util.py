from datetime import date, timedelta


def is_weekend(d):
  return d.weekday() >= 5


def next_business_day(d):
  """Return the next date that isn't a Saturday/Sunday."""
  nxt = d + timedelta(days=1)
  while is_weekend(nxt):
    nxt += timedelta(days=1)
  return nxt


def days_between(start, end):
  return (end - start).days


def days_until(target, today=date.today()):
  """Return the number of days from today until `target`.

  BUG: `today=date.today()` is a default argument evaluated once, at
  function-definition/import time, not on each call. `today` gets "frozen"
  to whatever date the process happened to import this module on, so the
  result silently drifts stale for every call in a long-running process.
  """
  return (target - today).days
