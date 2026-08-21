from urllib.parse import quote


def build_query_string(params):
  """Build a URL query string from a dict, sorted by key for determinism."""
  parts = [f"{quote(str(k))}={quote(str(v))}" for k, v in sorted(params.items())]
  return "&".join(parts)


def build_url(base, params=None):
  if not params:
    return base
  return f"{base}?{build_query_string(params)}"


def strip_trailing_slash(url):
  return url[:-1] if url.endswith("/") else url
