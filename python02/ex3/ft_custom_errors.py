# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_custom_errors.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/02 15:19:54 by tschwab           #+#    #+#             #
#    Updated: 2026/11/02 15:51:17 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)

    def raising_error(num: int) -> None:
        if num == 0:
            raise PlantError()
        elif num == 1:
            raise WaterError()
        else:
            return

class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        GardenError.raising_error(0)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        print("Testing WaterError...")
        GardenError.raising_error(1)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    try:
        print("Testing catching all garden errors...")
        GardenError.raising_error(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        GardenError.raising_error(1)
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
