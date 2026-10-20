"""The base class shared by every entity in the sandbox."""

from abc import ABC, abstractmethod


class Creature(ABC):
    """An entity with a name, a type and one attack."""

    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        """Return the attack message for this entity."""

    def describe(self) -> str:
        """Return the standard description used by the battle scripts."""
        return f"{self.name} is a {self.creature_type} type Creature"
