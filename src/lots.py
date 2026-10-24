"""Under src/ -- control, nothing tells us to skip this one."""


def avg_lot_size(district):
    total_area = district["total_area"]
    lot_count = district["lot_count"]
    return total_area / lot_count
