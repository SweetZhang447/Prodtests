def normalize(name):
    return name.strip().lower().replace(" ", "_")


def titleize(slug):
    return " ".join(p.capitalize() for p in slug.split("_"))
