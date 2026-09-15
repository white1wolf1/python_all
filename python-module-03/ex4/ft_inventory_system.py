import sys


def parametr_control() -> dict[str, int]:
    user_input_list = list(sys.argv[1:])
    input_amount = len(user_input_list)
    if input_amount == 0:
        print("No parameters were given !")
        return {}

    new_dict: dict[str, int] = {}
    for item in user_input_list:
        i = 0
        while len(item) > i:
            if item[i] != ':':
                i += 1
            else:
                break
        if len(item) == i:
            print(f"Error: - invalid parameter '{item}'")
            continue

        word = item[:i]
        number = item[i + 1:]

        try:
            new_dict.update({word: int(number)})
        except ValueError as e:
            print(f"quantity error for {word} :", e)
            continue

    return new_dict


def percentage(invintory: dict[str, int], key: str) -> float:
    total = sum(invintory.values())
    return (invintory[key] / total) * 100


def main() -> None:
    print("=== Inventory System Analysis ===")
    new_dict = parametr_control()
    print(f"Got inventory: {new_dict}")
    print(f"Item list: {list(new_dict.keys())}")
    print(
        f"Total quantity of {len(new_dict)} items is "
        f"{sum(new_dict.values())}"
    )

    for word in new_dict:
        pct = percentage(new_dict, word)
        print(f"Item {word} represents {pct:.1f}%")

    print(
        f"Item most abundant: {max(new_dict.keys())} "
        f"with quantity {max(new_dict.values())}"
    )
    print(
        f"Item least abundant: {min(new_dict.keys())} "
        f"with quantity {min(new_dict.values())}"
    )

    new_dict.update({'newdict': 2})
    print(f"{new_dict}")


if __name__ == "__main__":
    main()
