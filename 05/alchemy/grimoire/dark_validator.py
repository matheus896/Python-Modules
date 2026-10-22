"""The dark validator imports the spellbook dict at the top on purpose."""

from .dark_spellbook import DARK_INGREDIENTS


def dark_ingredient_verdict(ingredients: str) -> str:
    """Return the ingredients and whether they are valid."""
    text = ingredients.lower()
    found = [name for name in DARK_INGREDIENTS if name in text]
    status = "VALID" if found else "INVALID"
    return f"{ingredients} - {status}"
