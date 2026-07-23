class Plant:

    class StaticClass:

        _grow_stat = 0
        _age_stat = 0
        _show_stat = 0
        _shade_stat = 0

        def statistics_method(self) -> None:
            print(f"Stats :{self._grow_stat} grow,", end="")
            print(f"{self._age_stat} age, {self._show_stat} show")

        def increase_growth(self) -> None:
            self._grow_stat += 1

        def increase_show(self) -> None:
            self._show_stat += 1

        def increase_age(self) -> None:
            self._age_stat += 1

        def increase_shade(self) -> None:
            self._shade_stat += 1

    def __init__(self, name: str, height: float, age: int) -> None:
        self.statics = self.StaticClass()
        self.name = name
        if height > -1:
            self._height = height
        else:
            print("Error, hieght can't be negative")
        if age > -1:
            self._age = age
        else:
            self._age = 0
            print("Error, days can't be negative")

    @classmethod
    def create(cls, name: str = "Unknown plant",
               _height: float = 0.0, _age: int = 0) -> "Plant":
        return cls(name, _height, _age)

    @staticmethod
    def year_check(age: int) -> None:
        if age > 360:
            print(f"Is {age} days more than a year True")
        else:
            print(f"Is {age} days more than a year False")

    def show(self) -> None:
        print(f'{self.name}: {self._height}cm, {self._age} days old')
        self.statics.increase_show()

    def grow(self) -> None:
        if self.name == "Rose":
            self._height += 1
        elif self.name == "Sunflower":
            self._height = round(self._height + 0.4988, 2)
        elif self.name == "Cactus":
            self._height = round(self._height + 0.2, 2)
        else:
            self._height += 2
        self.statics.increase_growth()

    def age(self, day_of_age: int) -> None:
        for i in range(0, day_of_age):
            self.grow()
            self._age += 1
        self.statics.increase_age()

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
        print(f'{self.name}: {self._height}cm, {self._age} days old')
        print(f' Color : {self.color}')
        if not self.bloomed_tf:
            print(f' {self.name} has not bloomed yet')
        else:
            print(f" {self.name} is blooming  beautifully !")
        self.statics.increase_show()


class Seed(Flower):
    def seed_method(self) -> None:
        self.seed = 0
        if self.bloomed_tf:
            self.seed = 42

    def show(self) -> None:
        super().show()
        print(f"Seed : {self.seed}")


class Tree(Plant):

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.diameter = trunk_diameter
        self.shade_tf = False

    def shade(self) -> None:
        self.shade_tf = True
        self.statics.increase_shade()

    def show(self) -> None:
        print(f'{self.name}: {self._height}cm, {self._age} days old')
        print(f' Trunk Diameter : {self.diameter}')
        if not self.shade_tf:
            print(f'{self.name} is not producing a shade')
        else:
            print(f" Tree {self.name} now produces a shade of ", end="")
            print(f" {self._height}cm long and {self.diameter}cm wide.")
        self.statics.increase_show()


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
        self.statics.increase_growth()

    def show(self) -> None:
        print('=== Vegetable')
        print(f'{self.name}: {self._height}cm, {self._age} days old')
        print(f' Harvest season : {self.harvest}')
        print(f' Nutritional value : {self.nutritional_value}')
        self.statics.increase_show()


def display_statistics(cls: Plant) -> None:
    cls.statics.statistics_method()
    if cls.__class__.__name__ == "Tree":
        print(f"shade :{cls.statics._shade_stat}")


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old ===")
    Plant.year_check(30)
    Plant.year_check(400)
    print("")
    print("=== Flower")
    flower1 = Flower("Rose", 15.0, 10, "red")
    flower1.show()
    display_statistics(flower1)
    flower1.bloom()
    flower1.grow()
    flower1.show()
    display_statistics(flower1)
    tree1 = Tree("Oak", 200.0, 365, 5.0)
    print("")
    print("=== Tree")
    tree1.show()
    display_statistics(tree1)
    tree1.shade()
    tree1.show()
    display_statistics(tree1)
    print("")
    print("=== Seed")
    seed1 = Seed("Sunflower", 80.0, 45, "yellow")
    seed1.seed_method()
    seed1.show()
    seed1.bloom()
    seed1.age(1)
    seed1.seed_method()
    seed1.show()
    display_statistics(seed1)
    print("")
    print("=== Anonymous")
    anonym1 = Plant.create()
    anonym1.show()
    display_statistics(anonym1)


if __name__ == "__main__":
    main()
