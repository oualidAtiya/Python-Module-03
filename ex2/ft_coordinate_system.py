# import sys
import math


def parcing(coordinates):
    try:
        coordinates_list = []
        for c in coordinates.split(','):
            coordinates_list.append(int(c))
        coordinates_tuple = tuple((coordinates_list))

        print(f'Parsing coordinates: "{coordinates}"')
        print(f"Parsed position: {coordinates_tuple}")
        return coordinates_tuple
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{coordinates}"')
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e}\n")


def calculate_distance(x, y, z):
    x1, y1, z1 = tuple((0, 0, 0))
    x2, y2, z2 = tuple((x, y, z))
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}): {d}\n")


def ft_coordinate_system():
    print("=== Game Coordinate System ===")
    x, y, z = tuple((10, 20, 5))
    print(f"position created: ({x}, {y}, {z})")
    calculate_distance(x, y, z)
    x, y, z = parcing("3,4,0")
    calculate_distance(x, y, z)
    parcing("abc,def,ghi")
    try:
        x, y, z = tuple((3, 4, 0))
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except TypeError:
        return


ft_coordinate_system()
