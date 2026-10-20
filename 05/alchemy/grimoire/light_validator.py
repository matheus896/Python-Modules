"""The light validator imports the spellbook at module level."""

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Mark the ingredients as VALID when at least one is allowed."""
    text = ingredients.lower()
    allowed = any(
        item in text for item in light_spell_allowed_ingredients()
    )
    status = "VALID" if allowed else "INVALID"
    return f"{ingredients} - {status}"
