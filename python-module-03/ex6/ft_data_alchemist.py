import random


def ft_data_alchemist() -> None:
    mixed_names = ['Alice', 'bob', 'Charlie', 'dylan',
                   'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    capitalized_all_names = [x.capitalize() for x in mixed_names]
    capitalize_names = [x for x in mixed_names if x == x.capitalize()]

    print("Initial list of players:", mixed_names)
    print("New list with all names capitalized:", capitalized_all_names)
    print("New list of capitalized names only:", capitalize_names)
    print("")

    newdict = {x: random.randint(22, 2004) for x in capitalized_all_names}
    avarage_score = sum(newdict.values())/len(newdict.values())
    higher_scores = {(x, score) for x, score in newdict.items()
                     if score >= avarage_score}
    print("Score dict: ", newdict)
    print("Score average is ", round(avarage_score, 2))
    print("High scores:", higher_scores)


def main() -> None:
    print("=== Game Data Alchemist ===")
    ft_data_alchemist()


if __name__ == "__main__":
    main()
