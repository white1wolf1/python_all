def input_temperature(temp_str: str) -> int:
    int_str = int(temp_str)

    if int_str < 0:
        raise Exception(f"{int_str} °C is too cold for plants (min 0°C)")
    elif int_str > 40:
        raise Exception(f"{int_str} °C is too hot for plants (max 40°C)")
    return int_str


def test_temperature_input(random_str: str) -> None:

    print(f"Input data is '{random_str}'")
    try:
        print(f"Temperature is now {input_temperature(random_str)}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e} ")


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input("25")
    print("")
    test_temperature_input("abc")
    print("")
    test_temperature_input("100")
    print("")
    test_temperature_input("-50")
    print("")
    print("All tests completed - program didn't crash !")


if __name__ == "__main__":
    test_temperature()
