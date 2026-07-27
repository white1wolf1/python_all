def garden_operations(operation_number: int) -> int:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        24/0
    elif operation_number == 2:
        open("/non/existent/file.txt", "r")
    elif operation_number == 3:
        "string" + 1
    return operation_number


def test_error_types() -> None:
    i = 0
    print("=== Garden Error Types Demo ===")
    while i < 5:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print("Caught ValueErr:", e)
        except ZeroDivisionError as e:
            print("Caught ZeroDivisionError:", e)
        except FileNotFoundError as e:
            print("Caught FileNotFoundError:", e)
        except TypeError as e:
            print("Caught TypeErro", e)
        i = i+1
    print("Operation completed successfully")
    print("")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
