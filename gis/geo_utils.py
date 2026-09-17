"""Geo helpers. Inside gis/** -> ignored on this branch."""


def first_point(points):
    return points[0]


def centroid_lat(feature):
    return first_point(feature["points"])["lat"]


def bbox_area(feature):
    w = feature["bbox"]["east"] - feature["bbox"]["west"]
    h = feature["bbox"]["north"] - feature["bbox"]["south"]
    return w / h
