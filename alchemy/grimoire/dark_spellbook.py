"""The dark pair imports each other at module level on purpose."""

from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients accepted by dark magic."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a dark spell when the ingredients are valid."""
    validation = dark_validate_ingredients(ingredients)
    if validation.endswith("VALID"):
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
