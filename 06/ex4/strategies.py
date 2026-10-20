"""Battle strategies selected at runtime."""

from abc import ABC, abstractmethod

from ex3.capability import TransformCapability
from ex3.creature import Creature

from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    """Decide whether an entity is valid and make it act."""

    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        """Return True when the entity supports this strategy."""

    @abstractmethod
    def act(self, entity: Creature) -> None:
        """Apply the strategy to the entity."""


class NormalStrategy(BattleStrategy):
    """Any entity can use this strategy."""

    def is_valid(self, entity: Creature) -> bool:
        return True

    def act(self, entity: Creature) -> None:
        print(entity.attack())


class AggressiveStrategy(BattleStrategy):
    """Only entities with the transform capability can use this strategy."""

    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature) -> None:
        if not isinstance(entity, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{entity.name}' for this aggressive "
                "strategy"
            )
        print(entity.transform())
        print(entity.attack())
        print(entity.revert())
