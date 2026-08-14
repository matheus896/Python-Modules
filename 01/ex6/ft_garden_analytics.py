class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, {self.show_calls} show")

    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self.name = name.capitalize()
        self._growth_rate = growth_rate
        self._height = float(height)
        self._age = int(age)
        self._stats = self.Stats()

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._stats.grow_calls += 1
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self._stats.age_calls += 1
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        height = float(height)
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float):
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self._has_bloomed = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._has_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f"{self.shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, growth_rate: float):
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter
        self._stats: "Tree.Stats" = self.Stats()

    def produce_shade(self) -> None:
        self._stats.shade_calls += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, growth_rate: float):
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float):
        super().__init__(name, height, age, color, growth_rate)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print("Is 30 days more than a year? -> "
          f"{Plant.is_older_than_year(30)}")
    print("Is 400 days more than a year? -> "
          f"{Plant.is_older_than_year(400)}\n")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", 8)
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0, 0.8)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", growth_rate=30.0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print()

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_stats(anon)
