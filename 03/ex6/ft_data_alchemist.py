import random


PLAYERS = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
           'kevin', 'Liam']


def main() -> None:
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {PLAYERS}")
    capitalized = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {capitalized}")
    only_cap = [name for name in PLAYERS if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_cap}")
    score_dict = {name: random.randint(1, 1000) for name in capitalized}
    print(f"Score dict: {score_dict}")
    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")
    high = {n: score_dict[n] for n in score_dict if score_dict[n] > average}
    print(f"High scores: {high}")


main()
