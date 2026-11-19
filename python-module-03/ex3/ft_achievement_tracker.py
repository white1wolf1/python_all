import random


def gen_player_achievements(number: int) -> set[str]:
    achievement_pool = {
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
    requested_set = set(random.sample(list(achievement_pool), number))
    return requested_set


def main() -> None:
    alex = gen_player_achievements(7)
    ilyas = gen_player_achievements(5)
    ayse = gen_player_achievements(9)
    ahmet = gen_player_achievements(10)
    print("=== Achievement Tracker System ===")
    print("Player Alex:", alex)
    print("Player Ilyas:", ilyas)
    print("Player Ayse:", ayse)
    print("Player Ahmet:", ahmet)
    print()
    print("All distinct achievements:", alex | ilyas | ayse | ahmet)
    print()
    print("Common achievements:",
          set.intersection(alex, ilyas, ayse, ahmet))
    print()
    print("Only Alex has:",
          alex.difference(ilyas, ayse, ahmet))
    print("Only Ilyas has:",
          ilyas.difference(alex, ayse, ahmet))
    print("Only Ayse has:",
          ayse.difference(alex, ilyas, ahmet))
    print("Only Ahmet has:",
          ahmet.difference(alex, ilyas, ayse))
    print()
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
