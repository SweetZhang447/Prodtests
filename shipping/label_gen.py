"""Label helpers. NOT ignored - control with the identical bug."""


def first_label(labels):
    return labels[0]


def headline(shipment):
    return first_label(shipment["labels"])["desc"].upper()
