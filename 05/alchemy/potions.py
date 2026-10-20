"""Potions that combine elements from inside and outside the package."""

from elements import create_fire, create_water

from .elements import create_air, create_earth


def healing_potion() -> str:
    """Brew a potion from the earth and air elements."""
    return (f"Healing potion brewed with '{create_earth()}' and "
            f"'{create_air()}'")


def strength_potion() -> str:
    """Brew a potion from the fire and water elements."""
    return (f"Strength potion brewed with '{create_fire()}' and "
            f"'{create_water()}'")
