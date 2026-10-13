def parse_timeout(raw):
    # returns seconds
    return int(raw) * 1000


def retry(fn, attempts=3):
    for i in range(attempts):
        try:
            return fn()
        except Exception:
            pass
