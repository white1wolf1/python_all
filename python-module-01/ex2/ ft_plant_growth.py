class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        if self.name == "Rose":
            self.height += 1
        elif self.name == "Sunflower":
            self.height = round(self.height + 0.4988, 2)
        elif self.name == "Cactus":
            self.height = round(self.height + 0.2, 2)
        else:
            self.height = round(self.height + 1.1888, 2)

    def age(self) -> None:
        print("=== Garden Plant Growth ===")
        print(f"{self.name} : {self.height}cm, {self.days} days old")
        i = 1
        value = self.height
        for i in range(1, 8):
            self.grow()
            self.days += 1
            print(f"=== Day {i} ===")
            print(f"{self.name} : {self.height}cm, {self.days} days old")
        value = self.height - value
        value = round(value, 2)
        print(f"Growth this week: {value}cm")


def main() -> None:
    Plant1 = Plant("Cactus", 25, 30)
    Plant1.age()


if __name__ == "__main__":
    main()
