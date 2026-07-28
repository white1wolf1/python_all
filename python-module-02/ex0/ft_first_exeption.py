def input_temperature(temp_str: str) -> int:
    int_str = int(temp_str)
    return int_str


def test_temperature_input(random_str: str) -> None:

    print(f"Input data is '{random_str}'")
    try:
        print(f"Temperature is now {input_temperature(random_str)}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e} ")


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature_input("25")
    print("")
    test_temperature_input("abc")
    print("")
    print("All tests completed - program didn't crash")


if __name__ == "__main__":
    test_temperature()
