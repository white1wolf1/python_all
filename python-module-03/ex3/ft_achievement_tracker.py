import random


def gen_player_achivments(sayi: int) -> set:
    achivment_pool = {
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Unstoppable",
        "Boss Slayer",
        "Strategist",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Hidden Path Finder"
    }
    requestet_set = set(random.sample(list(achivment_pool), sayi))
    return requestet_set


def main() -> None:
    alex = gen_player_achivments(7)
    ilyas = gen_player_achivments(5)
    ayse = gen_player_achivments(1)
    ahmet = gen_player_achivments(3)
    print("=== Achievement Tracker System ===")
    print("Player Alex:", alex)
    print("Player Ilyas:", ilyas)
    print("Player Ayse:", ayse)
    print("Player Ahmet:", ahmet)
    print("")
    print("Common achievement:",
          set.intersection(alex, ilyas, ayse, ahmet))
    print("")
    print("Only Alex has:",
          alex.difference(ilyas, ayse, ahmet))
    print("Only Ilyas has:",
          ilyas.difference(alex, ayse, ahmet))
    print("Only Ayse has:",
          ayse.difference(alex, ilyas, ahmet))
    print("Only Ahmet has:",
          ahmet.difference(alex, ilyas, ayse))
    print("")
    print("Alex is missing:",
          (alex | ilyas | ayse | ahmet) - alex)
    print("Ilyas is missing:",
          (alex | ilyas | ayse | ahmet) - ilyas)
    print("Ayse is missing:",
          (alex | ilyas | ayse | ahmet) - ayse)
    print("Ahmet is missing:",
          (alex | ilyas | ayse | ahmet) - ahmet)


if __name__ == "__main__":
    main()
