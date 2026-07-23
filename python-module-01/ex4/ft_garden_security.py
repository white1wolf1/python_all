class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        if height > 0:
            self._height = height
        else:
            self._height = 0
            print("Error, hieght can't be negative")
        if days > 0:
            self._days = days
        else:
            self._days = 0
            print("Error, days can't be negative")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm,", end="")
        print(f" {self._days} days old")

    def grow(self) -> None:
        if self.name == "Rose":
            self._height += 1
        elif self.name == "Sunflower":
            self._height = round(self._height + 0.4988, 2)
        elif self.name == "Cactus":
            self._height = round(self._height + 0.2, 2)
        else:
            self._height = round(self._height + 1.1888, 2)

    def age(self) -> None:
        print("=== Garden Plant Growth ===")
        print(f"{self.name} : {self._height}cm, {self._days} days old")
        value = self._height
        for i in range(1, 8):
            self.grow()
            self._days += 1
            print(f"=== Day {i} ===")
            print(f"{self.name} : {self._height}cm, {self._days} days old")
        value = self._height - value
        value = round(value, 2)
        print(f"Growth this week: {value}cm")

    def set_height(self, height) -> None:
        if height > 0:
            self._height = height
            print(f" Height Updated : {self._height}cm ")
        else:
            print(f"{self.name} :", end="")
            print(" Error ,your height can't be negative ")
            print("Height update rejected")

    def set_age(self, days) -> None:
        if days > 0:
            self._days = days
            print(f" Age Updated : {self._days} days ")
        else:
            print(f"{self.name} :", end="")
            print("Error, your age can't be negative ")
            print("Age update rejected")


def main() -> None:
    print("=== Garden Security System ===")
    print("Plant Created: ", end="")
    Plant1 = Plant("Rose", 15.0, 10)
    Plant1.show()
    print("")
    Plant1.set_height(25)
    Plant1.set_age(30)
    print("")
    Plant1.set_height(-12)
    Plant1.set_age(-30)
    print("\n Current State ", end="")
    Plant1.show()


if __name__ == "__main__":
    main()
