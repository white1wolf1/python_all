import sys


def operations(argv_list_new: list[]) -> None:
    arg_number = len(argv_list_new)
    print("Scores processed:", argv_list_new)
    print("Total players:", arg_number)
    print("Total score:", sum(argv_list_new))
    print("Average score:", sum(argv_list_new) / arg_number)
    print("High score:", max(argv_list_new))
    print("Low score:", min(argv_list_new))
    print("Score range:", max(argv_list_new) - min(argv_list_new))


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")

    arg_number = len(sys.argv)
    if arg_number == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    try:
        newlist = [int(score) for score in sys.argv[1:]]
        operations(newlist)

    except ValueError:
        eror_list = []
        valid_list = []

        for argument in sys.argv[1:]:
            try:
                valid_list.append(int(argument))
            except ValueError:
                eror_list.append(argument)

        if eror_list:
            for argument in eror_list:
                print(f"Invalid parameter: '{argument}'")

        if valid_list:
            operations(valid_list)
        else:
            print("No valid scores provided. Usage: python3 "
                  "ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    ft_score_analytics()
