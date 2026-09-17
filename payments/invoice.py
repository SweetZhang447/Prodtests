"""Invoice helpers. Inside payments/** -> ignored on this branch."""


def first_line(lines):
    return lines[0]


def headline(invoice):
    return first_line(invoice["lines"])["desc"].upper()


def avg_line_total(invoice):
    return sum(l["amount"] for l in invoice["lines"]) / len(invoice["lines"])
