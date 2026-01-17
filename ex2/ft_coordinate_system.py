import math


def calculate_distance(f_position, s_position):
    if (f_position and s_position):
        x1, y1, z1 = f_position
        x2, y2, z2 = s_position
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        print(f"Distance between {f_position} and {s_position}: ", end="")
        print(f"{distance:.2f}\n")


def parse_position(position):
    try:
        p = position.split(',')
        parsed_position = (int(p[0]), int(p[1]), int(p[2]))
        print(f"Parsed position: {parsed_position}")
    except Exception as e:
        print(f'Parsing invalid coordinates: "{position}"')
        print(f"Error parsing coordinates: {e}")
        print("Error details - Type: ValueError", end="")
        print(f', Arg: ("{e}",)\n')
        return
    return parsed_position


def ft_coordinate_system():
    print("=== Game Coordinate System ===\n")
    pos_a = (10, 20, 5)
    print(f"Position created: {pos_a}")
    pos_b = (0, 0, 0)
    calculate_distance(pos_b, pos_a)

    pos_a = "3, 4,0"
    print(f'Parsing coordinates: {pos_a}')
    pos_a = parse_position(pos_a)
    calculate_distance(pos_b, pos_a)

    pos_a = "abc,def,ghi"
    pos_a = parse_position(pos_a)
    calculate_distance(pos_b, pos_a)

    print("Unpacking demonstration:")
    x, y, z = (3, 4, 0)
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

ft_coordinate_system()
