import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(address):
  if not isinstance(address, str):
    return False
  return bool(EMAIL_RE.match(address.strip()))


def is_non_empty_string(value):
  return isinstance(value, str) and len(value.strip()) > 0
