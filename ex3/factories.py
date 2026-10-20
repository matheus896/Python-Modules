"""Abstract factory and the two concrete families."""

from abc import ABC, abstractmethod

from .creature import Creature
from .entities import Flameling, Morphagon, Pyrodon, Shiftling


class CreatureFactory(ABC):
    """Create a base entity and its evolved form."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base entity."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved entity."""


class FlameFactory(CreatureFactory):
    """The fire family."""

    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    """The family with the transform capability."""

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
