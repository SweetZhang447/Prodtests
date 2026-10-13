"""Small, dependency-free string helpers."""


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Shorten ``text`` to at most ``max_length`` characters, ending with ``suffix`` if cut."""
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if len(text) <= max_length:
        return text
    if max_length <= len(suffix):
        return text[:max_length]
    return text[: max_length - len(suffix)] + suffix


def is_blank(text: str | None) -> bool:
    """Return True if ``text`` is None, empty, or only whitespace."""
    return text is None or not text.strip()
