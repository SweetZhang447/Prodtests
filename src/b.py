"""src/b.py"""


def mean_lot(district):
    return district["total"] / district["count"]


def first_lot(lots):
    return lots[0]["id"]


def holder_name(lot):
    return lot["holder"]["name"].upper()
