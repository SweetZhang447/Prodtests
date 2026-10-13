"""Under src/ -- the naming rule applies here."""


def density(region):
    a = region["area"]
    n = region["count"]
    return n / a
