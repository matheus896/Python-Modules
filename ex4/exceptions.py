"""Dedicated exception for an entity that cannot use a strategy."""


class InvalidStrategyError(Exception):
    """Raised when an entity does not support the chosen strategy."""
