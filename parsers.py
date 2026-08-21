def parse_csv_line(line, delimiter=","):
  """Split a CSV line into fields, trimming whitespace from each field."""
  fields = line.split(delimiter)
  return [f.strip() for f in fields]


def get_field(line, index, delimiter=","):
  """Return the field at `index` in a CSV line.

  BUG: uses `<=` instead of `<`, so index == len(fields) is accepted and
  raises IndexError instead of a clear bounds check.
  """
  fields = parse_csv_line(line, delimiter)
  if index <= len(fields):
    return fields[index]
  raise IndexError(f"field index {index} out of range for line with {len(fields)} fields")
