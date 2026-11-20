# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_coordinate_system.py                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/19 18:42:16 by tschwab           #+#    #+#             #
#    Updated: 2026/11/20 14:42:29 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

import math


def get_distance(a: tuple[float, float, float],
                 b: tuple[float, float, float]) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b
    distance = math.sqrt(((x2 - x1) ** 2) +
                         ((y2 - y1) ** 2) + ((z2 - z1) ** 2))
    return round(distance, 4)


def get_player_pos() -> tuple[float, float, float]:

    while True:
        res = []
        string = input("Enter new coordinates as floats "
                       "in format 'x,y,z': ")
        pos = string.split(",")
        if len(pos) != 3:
            print("Invalid syntax")
            continue
        try:
            for position in pos:
                n = float(position)
                res.append(n)
            result = (res[0], res[1], res[2])
            return result
        except ValueError as e:
            print(f"Error on parameter {position!r}: {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    distance_first = get_distance(first, (0.0, 0.0, 0.0))
    print(f"Distance to center: {distance_first}\n")
    print("Get a second set of coordinates")
    second = get_player_pos()
    distance_both = get_distance(first, second)
    print(f"Distance between the 2 sets of coordinates: {distance_both}")
