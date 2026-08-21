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
