import math


def get_player_pos() -> tuple[float, float, float]:
    try:
        xyz = input("Enter coordinate for x,y,z :")
        parsed_xyz = xyz.split(",")
        newtuple = list()

        if len(parsed_xyz) != 3:
            try:
                raise TypeError
            except TypeError:
                print("Invalid syntax use 3 parameters !")
                return get_player_pos()

        for i in parsed_xyz:
            try:
                value = float(i)
                newtuple.append(value)
            except ValueError as e:
                print(f"Error on parameter: {e}")
                return get_player_pos()

        result = tuple(newtuple)
        return (result[0], result[1], result[2])
    except RecursionError as error_e:
        print("Too many wrong tries please restart the code", error_e)
        raise SystemExit()


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")

    dist_center = math.sqrt(
        first[0]**2 + first[1]**2 + first[2]**2
    )
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
