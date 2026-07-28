class GardenError(Exception):
    def __init__(self, error_message: str = "Unknown plant error") -> None:
        super().__init__(error_message)


class PlantError(GardenError):
    def __init__(
        self,
        error_message: str = "The tomato plant is wilting!"
    ) -> None:
        super().__init__(error_message)


def water_plant(plant_name: str) -> None:
    if plant_name.capitalize() == plant_name:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water:'{plant_name}'")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")

    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    print("")
    plants = ["Tomato", "Lettuce", "Carrots"]
    print("Testing valid plants...")
    test_watering_system(plants)
    plants[1] = "lettuce"
    print("")
    print("Testing invalid plants...")
    test_watering_system(plants)
    print("")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
