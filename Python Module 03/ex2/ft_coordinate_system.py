import math


def create_pos(x: int, y: int, z: int, print_logs: bool = True
               ) -> tuple[int, int, int]:
    """Creates a position tuple

    Args:
        x (int): X coordinate.
        y (int): Y coordinate.
        z (int): Z coordinate.
        print_logs (bool, optional): Prints the coordinates. Defaults to True.

    Returns:
        tuple[int, int, int]: New coordinates.
    """
    pos: tuple[int, int, int] = x, y, z
    if print_logs:
        print(f"\nPosition created: {pos}")
    return (pos)


def parse_pos(s: str) -> tuple[int, int, int]:
    """Parses an string representing coordinates in integer to a coord tuple.

    Args:
        s (str): String of coordinates. Separated by ',' (ex: 0,0,0).

    Returns:
        tuple[int, int, int]: Parsed coordinates. If error returns (0, 0, 0).
    """
    print(f"\nParsing coordinates: {s}")
    try:
        x, y, z = s.split(",")
        pos = create_pos(int(x), int(y), int(z), False)
    except ValueError as e:
        print(f"Error parsing coordinates: {e.args[0]}\n"
              f"Error details - Type: ValueError, {e.args}")
        return create_pos(0, 0, 0, False)
    print(f"Parsed position: {pos}")
    return (pos)


def calculate_distance(origin: tuple[int, int, int],
                       dest: tuple[int, int, int]) -> None:
    """Calculates the distance between two coordinates using.

    Args:
        origin (tuple[int, int, int]): Origin coordinates.
        dest (tuple[int, int, int]): Destination coordinates.
    """
    dist = math.sqrt((dest[0] - origin[0]) ** 2 + (dest[1] - origin[1]) ** 2 +
                     (dest[2] - origin[2]) ** 2)
    print(f"Distance between {origin} and {dest}: {dist:.2f}")


def print_cords(cords: tuple[int, int, int]) -> None:
    """Prints formated the coordinates.

    Args:
        cords (tuple[int, int, int]): Coordinates.
    """
    print(f"Coordinates: X={cords[0]}, Y={cords[1]}, Z={cords[2]}")


print("=== Game Coordinate System ==")
pos1 = create_pos(10, 20, 5)
calculate_distance((0, 0, 0), pos1)

pos2 = parse_pos("3, 4, 0")
calculate_distance((0, 0, 0), pos2)

parse_pos("abc,def,ghi")

print("\nUnpacking demonstration:\n"
      "Player at x=3, y=4, z=0")
print_cords(pos2)
