"""The dark validator closes the circular import on purpose."""

from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    """Mark the ingredients as VALID when at least one is allowed."""
    text = ingredients.lower()
    allowed = any(
        item in text for item in dark_spell_allowed_ingredients()
    )
    status = "VALID" if allowed else "INVALID"
    return f"{ingredients} - {status}"
