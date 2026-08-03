def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def count(day):
        if day == 0:
            return
        count(day - 1)
        print(f"Day{day}")
    count(n)
    print("Harvest time!")