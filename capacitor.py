from ex3 import TransformCreatureFactory
from ex3.capability import TransformCapability
from ex3.creature import Creature


def exercise(entity: Creature) -> None:
    """Describe, transform, attack and revert one entity."""
    print(entity.describe())
    print(entity.attack())
    if not isinstance(entity, TransformCapability):
        raise TypeError(f"{entity.name} has no transform capability")
    print(entity.transform())
    print(entity.attack())
    print(entity.revert())


def main() -> None:
    """Exercise the transform capability on the base and evolved forms."""
    factory = TransformCreatureFactory()
    print("Testing Creature with transform capability")
    print("base:")
    exercise(factory.create_base())
    print()
    print("evolved:")
    exercise(factory.create_evolved())


if __name__ == "__main__":
    main()
