import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")

    arg_number = len(sys.argv)

    if arg_number == 1:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
        return

    try:
        arg_number -= 1
        arguments = sys.argv[1:]
        newlist = [int(score) for score in arguments]

        print("Scores processed:", newlist)
        print("Total players:", arg_number)
        print("Total score:", sum(newlist))
        print("Average score:", sum(newlist) / arg_number)
        print("High score:", max(newlist))
        print("Low score:", min(newlist))
        print("Score range:", max(newlist) - min(newlist))

    except ValueError:
        for argument in sys.argv[1:]:
            try:
                int(argument)
            except ValueError:
                print(f"Invalid parameter: '{argument}'")

        print("No scores provided, Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    ft_score_analytics()
