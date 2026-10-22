"""The dark spellbook shares a dict and imports the validator at the top."""

from .dark_validator import dark_ingredient_verdict

DARK_INGREDIENTS: dict[str, str] = {
    "bats": "winged",
    "frogs": "amphibian",
    "arsenic": "mineral",
    "eyeball": "organic",
}


def dark_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients accepted by dark magic."""
    return list(DARK_INGREDIENTS)


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a dark spell when the verdict is valid."""
    verdict = dark_ingredient_verdict(ingredients)
    if verdict.endswith("VALID"):
        return f"Spell recorded: {spell_name} ({verdict})"
    return f"Spell rejected: {spell_name} ({verdict})"
