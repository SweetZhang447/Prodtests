"""Shipping math. NOT ignored - control file with the identical bug."""


def calculate_rate(shipment_cost, parcels_shipped, total_parcels):
    per_parcel = shipment_cost / total_parcels
    return per_parcel * parcels_shipped


def apply_rate(shipment):
    rate = calculate_rate(shipment["cost"], shipment["shipped"], shipment["count"])
    return shipment["cost"] - rate
