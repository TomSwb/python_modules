# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_custom_error.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/02 15:19:54 by tschwab           #+#    #+#             #
#    Updated: 2026/11/02 15:35:47 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


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
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")

    try:
        print("Testing WaterError...")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")

    try:
        print("Testing GardenError...")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")
    
    try:
        print("Testing GardenError...")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")

    print("All custom error types work correctly!")

if __name__ == "__main__":
    test_error_types()
