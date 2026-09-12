import random


def ft_data_alchemist():
    mixed_names = ['Alice', 'bob', 'Charlie', 'dylan',
                   'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    capitalized_all_names = [x.capitalize() for x in mixed_names]
    capitalize_names = [x for x in mixed_names if x == x.capitalize()]

    print("Initial list of players:", mixed_names)
    print("New list with all names capitalized:", capitalized_all_names)
    print("New list of capitalized names only:", capitalize_names)

    newdict = {x:random.randint(22, 2004) for x in capitalized_all_names}
    avarage_score = sum(newdict)/len(newdict)
    higer_scores = {x for x in avarage_score if x >= avarage_score}
    print(higer_scores)

def main():
    print("=== Game Data Alchemist ===")
    ft_data_alchemist()


if __name__ == "__main__":
    main()
