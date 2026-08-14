class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self.name = name
        self._height = height
        self._age = age
        self._growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self._age += 1

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(age)
            print(f"Age updated: {self._age} days")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10, 0.8)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-25)
    rose.set_age(-30)
    print()
    print("Current state: ", end="")
    rose.show()
