"""The light spellbook breaks the cycle with a local import."""


def light_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients accepted by light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a light spell when the ingredients are valid."""
    from .light_validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    if validation.endswith("VALID"):
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
