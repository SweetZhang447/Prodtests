def truncate(text, max_len, suffix="..."):
  """Truncate `text` to at most `max_len` characters, appending `suffix` if cut."""
  if len(text) <= max_len:
    return text
  keep = max(0, max_len - len(suffix))
  return text[:keep] + suffix


def slugify(text):
  """Lowercase, trim, and replace runs of non-alphanumeric chars with a hyphen."""
  out = []
  prev_hyphen = True
  for ch in text.strip().lower():
    if ch.isalnum():
      out.append(ch)
      prev_hyphen = False
    elif not prev_hyphen:
      out.append("-")
      prev_hyphen = True
  return "".join(out).strip("-")
