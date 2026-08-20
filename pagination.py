def page_items(items, page, page_size):
    start = page * page_size
    end = start + page_size
    return items[start:end]


def render_page(items, page, page_size):
    return page_items(items, page, page_size)
