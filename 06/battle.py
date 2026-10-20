from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    """Describe and attack with the base and evolved entity."""
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(first: CreatureFactory, second: CreatureFactory) -> None:
    """Make the two base entities fight."""
    print("Testing battle")
    left = first.create_base()
    right = second.create_base()
    print(left.describe())
    print("vs.")
    print(right.describe())
    print("fight!")
    print(left.attack())
    print(right.attack())


def main() -> None:
    """Run the factory and battle demonstrations."""
    test_factory(FlameFactory())
    test_factory(TransformCreatureFactory())
    test_battle(FlameFactory(), TransformCreatureFactory())


if __name__ == "__main__":
    main()
