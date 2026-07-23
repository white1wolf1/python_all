class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        if height > 0:
            self._height = height
        else:
            self._height = 0
            print("Error, hieght can't be negative")
        if age > 0:
            self._age = age
        else:
            self._age = 0
            print("Error, days can't be negative")

    def grow(self) -> None:
        if self.name == "Rose":
            self._height += 1
        elif self.name == "Sunflower":
            self._height = round(self._height + 0.4988, 2)
        elif self.name == "Cactus":
            self._height = round(self._height + 0.2, 2)
        else:
            self._height += 2

    def age(self, day_of_age: int) -> None:
        for i in range(0, day_of_age):
            self.grow()
            self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed_tf = False

    def bloom(self) -> None:
        self.bloomed_tf = True

    def show(self) -> None:
        print('=== Flower')
        print(f'{self.name}: {self._height}cm, {self._age} days old')
        print(f' Color : {self.color}')
        if not self.bloomed_tf:
            print(f' {self.name} has not bloomed yet')
        else:
            print(f" {self.name} is blooming  beautifully !")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.diameter = trunk_diameter
        self.shade_tf = False

    def shade(self) -> None:
        self.shade_tf = True

    def show(self) -> None:
        print('=== Tree')
        print(f'{self.name}: {self._height}cm, {self._age} days old')
        print(f' Trunk Diameter : {self.diameter}')
        if not self.shade_tf:
            print(f'{self.name} is not producing a shade')
        else:
            print(f" Tree {self.name} now produces a shade of ", end="")
            print(f" {self._height}cm long and {self.diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        if self.name == "Tomato":
            self._height = round(self._height + 2.1, 1)
        else:
            self._height += 1
        self.nutritional_value += 1

    def show(self) -> None:
        print('=== Vegetable')
        print(f'{self.name}: {self._height}cm, {self._age} days old')
        print(f' Harvest season : {self.harvest}')
        print(f' Nutritional value : {self.nutritional_value}')


def main():
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.shade()
    oak.show()
    print("")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    main()
