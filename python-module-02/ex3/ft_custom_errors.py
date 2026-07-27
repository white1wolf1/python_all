class GardenError(Exception):
    def __init__(self, error_message: str = "Unknown plant error") -> None:
        super().__init__(error_message)


class WaterErrorr(GardenError):
    def __init__(self, error_message: str =
                 "Not enough water in the tank !") -> None:
        super().__init__(error_message)


class PlantError(GardenError):
    def __init__(self, error_message: str =
                 "The tomato plant is wilting !") -> None:
        super().__init__(error_message)


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("testing PlantError ...")
    try:
        raise PlantError()
    except PlantError as e:
        print("Caught PlantError:", e)
    print("")
    print("testing WaterError ...")
    try:
        raise WaterErrorr()
    except WaterErrorr as e:
        print("Caught WaterError :", e)
    print("")
    print("Testing catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as e:
        print("Caught GardenError:", e)
    try:
        raise WaterErrorr()
    except GardenError as e:
        print("Caught GardenError:", e)
    print("")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
