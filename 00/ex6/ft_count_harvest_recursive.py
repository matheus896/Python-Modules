def count(n: int) -> None:
    for i in range(n):
        print(f"Day{i + 1}")


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    count(days)
    print("Harvest time!")
