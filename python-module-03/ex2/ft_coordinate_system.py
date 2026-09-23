import math


def get_player_pos() -> tuple[float, float, float]:
    xyz = (input("Enter coordinate for x,y,z :"))
    parsed_xyz = xyz.split(",")
    newtuple =list()

    for i in parsed_xyz:
        try:
            i = float(i)  #amk malı float a çevirmiyo mu neden hata veriyo
            newtuple.append(i)
        except ValueError as e:
            print(f"Error on parameter: {e}")
            return get_player_pos()
    newtuple = tuple(newtuple)
    return (newtuple)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")

    dist_center = math.sqrt(first[0]**2 + first[1]**2 + first[2]**2)
    print(f"Distance to center: {round(dist_center, 4)}\n")

    print("Get a second set of coordinates")
    second = get_player_pos()

    dist = math.sqrt(
        (second[0] - first[0])**2 +
        (second[1] - first[1])**2 +
        (second[2] - first[2])**2
    )
    print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}")


if __name__ == "__main__":
    main()
