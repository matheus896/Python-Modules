def count(days: int) -> None:
    if days == 0:
        return
    count(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive() -> None:
    n = int(input("Days until harvest: "))
    count(n)
    print("Harvest time!")
