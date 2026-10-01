import random


ALL_ACHIEVEMENTS = [
    'Crafting Genius', 'World Savior', 'Master Explorer',
    'Collector Supreme', 'Untouchable', 'Boss Slayer',
    'Strategist', 'Unstoppable', 'Speed Runner', 'Survivor',
    'Treasure Hunter', 'First Steps', 'Sharp Mind',
    'Hidden Path Finder'
]


def gen_player_achievements() -> set[str]:
    n = random.randint(5, 9)
    return set(random.sample(ALL_ACHIEVEMENTS, n))


def main() -> None:
    print("=== Achievement Tracker System ===")
    players = [
        ('Alice', gen_player_achievements()),
        ('Bob', gen_player_achievements()),
        ('Charlie', gen_player_achievements()),
        ('Dylan', gen_player_achievements())
    ]
    for name, achs in players:
        print(f"Player {name}: {achs}")

    all_ach: set[str] = set()
    for _, achs in players:
        all_ach = all_ach.union(achs)
    print(f"All distinct achievements: {all_ach}")

    common = players[0][1]
    for _, achs in players:
        common = common.intersection(achs)
    print(f"Common achievements: {common}")

    for name, achs in players:
        others: set[str] = set()
        for name2, achs2 in players:
            if name2 != name:
                others = others.union(achs2)
        print(f"Only {name} has: {achs.difference(others)}")

    for name, achs in players:
        missing = set(ALL_ACHIEVEMENTS).difference(achs)
        print(f"{name} is missing: {missing}")


main()
