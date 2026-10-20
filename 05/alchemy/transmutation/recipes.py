"""Recipes that mix absolute and relative imports."""

from elements import create_fire

from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    """Transmute lead into gold with air, a strength potion and fire."""
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' and "
            f"'{strength_potion()}' mixed with '{create_fire()}'")
