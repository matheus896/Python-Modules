"""A capability that is deliberately not part of the Creature family."""

from abc import ABC, abstractmethod


class TransformCapability(ABC):
    """Adds transform and revert without forcing them on every entity."""

    _transformed: bool = False

    @property
    def transformed(self) -> bool:
        """Whether the entity is currently transformed."""
        return self._transformed

    @abstractmethod
    def transform(self) -> str:
        """Enter the transformed state and return a message."""

    @abstractmethod
    def revert(self) -> str:
        """Leave the transformed state and return a message."""
