class LRUCache:
  """A tiny fixed-capacity least-recently-used cache."""

  def __init__(self, capacity):
    self.capacity = capacity
    self._data = {}
    self._order = []

  def get(self, key):
    if key not in self._data:
      return None
    self._order.remove(key)
    self._order.append(key)
    return self._data[key]

  def put(self, key, value):
    if key in self._data:
      self._order.remove(key)
    elif len(self._order) >= self.capacity:
      # BUG: pops the most-recently-used key (the end of the list) instead
      # of the least-recently-used key (the front), evicting exactly the
      # wrong entry under capacity pressure.
      evicted = self._order.pop()
      del self._data[evicted]
    self._data[key] = value
    self._order.append(key)
