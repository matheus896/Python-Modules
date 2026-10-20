from ex3 import (
    CreatureFactory,
    FlameFactory,
    TransformCreatureFactory,
)
from ex4 import (
    AggressiveStrategy,
    BattleStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def describe_opponents(opponents: list[Opponent]) -> str:
    """Build the compact opponent list shown before a tournament."""
    labels = []
    for factory, strategy in opponents:
        entity = factory.create_base()
        name = strategy.__class__.__name__.replace("Strategy", "")
        labels.append(f"({entity.name}+{name})")
    return "[ " + ", ".join(labels) + " ]"


def battle(opponents: list[Opponent]) -> None:
    """Make every opponent face every other one exactly once."""
    print("*** Tournament ***")
    print()
    print(f"{len(opponents)} opponents involved")

    for index, (factory_a, strategy_a) in enumerate(opponents):
        for factory_b, strategy_b in opponents[index + 1:]:
            left = factory_a.create_base()
            right = factory_b.create_base()
            print()
            print("- Battle *")
            print()
            print(left.describe())
            print("vs.")
            print(right.describe())
            print()
            print("now fight!")
            try:
                strategy_a.act(left)
                strategy_b.act(right)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    """Run one valid tournament and one that must abort."""
    basic: list[Opponent] = [
        (FlameFactory(), NormalStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    print("Tournament 0 (basic)")
    print(describe_opponents(basic))
    print()
    battle(basic)

    print()
    invalid: list[Opponent] = [
        (TransformCreatureFactory(), AggressiveStrategy()),
        (FlameFactory(), AggressiveStrategy()),
    ]
    print("Tournament 1 (error)")
    print(describe_opponents(invalid))
    print()
    battle(invalid)


if __name__ == "__main__":
    main()
