"""Under data/gis/ -- excluded by .macroscope/correctness/naming-rules.md."""


def density(feature):
    a = feature["area"]
    n = feature["count"]
    return n / a
