def paginate(items, page, page_size):
    """Return the items on the given 1-indexed page."""
    if page < 1 or page_size < 1:
        raise ValueError("page and page_size must be >= 1")
    start = page * page_size
    end = start + page_size
    return items[start:end]


def total_pages(item_count, page_size):
    """Return how many pages are needed to show item_count items."""
    if page_size < 1:
        raise ValueError("page_size must be >= 1")
    return item_count // page_size
