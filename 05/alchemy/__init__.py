"""The alchemy package interface.

Only create_air is exposed here. create_earth stays in
alchemy.elements and is deliberately not re-exported.
"""

from .elements import create_air

__all__ = ["create_air"]
