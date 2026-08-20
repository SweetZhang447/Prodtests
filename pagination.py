PAGE_SIZE = 20


def page_count(total_items, page_size=PAGE_SIZE):
    """Return the number of pages needed to show total_items."""
    if total_items <= 0:
        return 0
    return (total_items + page_size - 1) // page_size


def page_items(items, page, page_size=PAGE_SIZE):
    """Return the slice of items shown on the given 1-indexed page."""
    start = page * page_size
    return items[start:start + page_size]
