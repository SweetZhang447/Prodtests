"""Under data/gis/ -- the instruction says to skip this file entirely."""


def avg_parcel_size(region):
    total_area = region["total_area"]
    parcel_count = region["parcel_count"]
    return total_area / parcel_count
