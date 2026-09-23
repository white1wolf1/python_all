import sys


def parameter_control(args_list: list[str]) -> dict[str, int]:
    invalid_parameters = []
    duplicated_parameters = []
    not_valid_values = []
    checked_keys = []
    inventory = {}

    for arg in args_list:
        if ':' not in arg:
            invalid_parameters.append(arg)
            continue

        key, value = arg.split(':', 1)

        try:
            int_value = int(value)
        except ValueError:
            not_valid_values.append(arg)
            continue

        if key in checked_keys:
            duplicated_parameters.append(arg)
        else:
            checked_keys.append(key)

        inventory[key] = int_value

    for parameter in duplicated_parameters:
        key = parameter.split(':', 1)[0]
        print(f"Redundant item '{key}' - discarding")

    for parameter in invalid_parameters:
        print(f"Error - invalid parameter '{parameter}'")

    for parameter in not_valid_values:
        key, value = parameter.split(':')
        print
        (
            f"Quantity error for '{key}': "
            f"invalid literal for int() with base 10: '{value}'"
        )

    return inventory


def percentage(inventory: dict[str, int], key: str) -> float:
    total = sum(inventory.values())
    return float(inventory[key] / total) * 100


def main() -> None:
    print("=== Inventory System Analysis ===")
    new_dict = parameter_control(sys.argv[1:])
    print(f"Got inventory: {new_dict}")

    if not new_dict:
        print("No valid items in inventory.")
        return

    print(f"Item list: {list(new_dict.keys())}")
    print(
        f"Total quantity of {len(new_dict)} items is "
        f"{sum(new_dict.values())}"
    )

    for word in new_dict:
        pct = percentage(new_dict, word)
        print(f"Item {word} represents {pct:.1f}%")

    most_abundant = max(new_dict, key=lambda k: new_dict[k])
    least_abundant = min(new_dict, key=lambda k: new_dict[k])

    print(
        f"Item most abundant: {most_abundant} "
        f"with quantity {new_dict[most_abundant]}"
    )
    print(
        f"Item least abundant: {least_abundant} "
        f"with quantity {new_dict[least_abundant]}"
    )

    new_dict.update({'newdict': 2})
    print(f"Updated inventory: {new_dict}")


if __name__ == "__main__":
    main()
