"""Geo helpers. Inside gis/** -> ignored on this branch."""


def first_point(points):
    return points[0]


def centroid_lat(feature):
    return first_point(feature["points"])["lat"]
