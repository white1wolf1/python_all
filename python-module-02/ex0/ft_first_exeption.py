def input_tempriture(temp_str: str) -> int:
    int_str = int(temp_str)
    return int_str


def test_temperature(ramdom_str: str) -> None:
    print(f" Input data is '{ramdom_str}'")
    try:
        print(f"Temperature is now {input_tempriture(ramdom_str)}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e} ")


def main() -> None:
    print("=== Garden Temperature ===")
    print("")
    test_temperature("25")
    print("")
    test_temperature("ABC")
    print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
