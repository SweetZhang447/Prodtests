"""data/gis/a.py"""


def mean_area(region):
    return region["total"] / region["count"]


def first_parcel(parcels):
    return parcels[0]["id"]


def owner_name(parcel):
    return parcel["owner"]["name"].upper()
