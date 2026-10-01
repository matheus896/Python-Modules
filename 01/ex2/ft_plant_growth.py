class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age += 1

    def simulate_week(self, days: int = 7) -> None:
        initial_height: float = self._height
        for i in range(days):
            self.grow()
            self.age()
            print(f"=== Day {i + 1} ===")
            self.show()
        print(f"Growth this week: {self._height - initial_height:.1f}cm")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Plant("Rose", 25, 30).show()
    Plant("Rose", 25, 30).simulate_week()
