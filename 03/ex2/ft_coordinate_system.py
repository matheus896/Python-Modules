import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            x_str, y_str, z_str = raw.split(',')
        except ValueError:
            print("Invalid syntax")
            continue
        coords = []
        ok = True
        for part in (x_str, y_str, z_str):
            try:
                coords.append(float(part))
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                ok = False
                break
        if ok:
            x, y, z = coords
            return (x, y, z)


def distance(p1: tuple[float, float, float],
             p2: tuple[float, float, float]) -> float:
    return math.sqrt((p2[0] - p1[0])**2 +
                     (p2[1] - p1[1])**2 +
                     (p2[2] - p1[2])**2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    print("Distance to center: "
          f"{round(distance(p1, (0.0, 0.0, 0.0)), 4)}\n")
    print("Get a second set of coordinates")
    p2 = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(distance(p1, p2), 4)}")
