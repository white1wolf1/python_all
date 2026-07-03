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

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color:str) ->None:
        super().__init__( name, height, age)
        self.color = color
        self.bloom = False
    
    def bloom(self) -> None:
        self.bloom = True

class Tree(Plant):
    

    def show(self) -> None:
        print(f"Current state {self.name}: {self._height}cm, {self._days} days old")

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
        i = 1
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
        if height > 0 :
            self._height = height
            print(f" Height Updated : {self._height}cm ")
        else:
            print(" Error ,your height can't be negative ")
            print("update rejected")

    def set_age(self, age) -> None:
        if age > 0 :
            self._days = age
            print(f" Age Updated : {self._days} days ")
        else:
            print("Error, your age can't be negative ")
            print("update rejected")
