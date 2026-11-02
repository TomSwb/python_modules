# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_finally_block.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/02 15:58:45 by tschwab           #+#    #+#             #
#    Updated: 2026/11/02 16:20:33 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Caught PlantError: Invalid name to water") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"... {plant_name}")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    plants = ["Tomato", "Lettuce", "Carrots"]

    try:
        print("Testing valid plants...")
        print("Opening watering system")
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"{e}")
        print("... ending tests and returning to main")
    finally:
        print("Closing watering system\n")

    plants = ["Tomato", "lettuce", "Carrots"]

    try:
        print("Testing valid plants...")
        print("Opening watering system")
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"{e}")
        print("... ending tests and returning to main")
    finally:
        print("Closing watering system\n")
    

if __name__ == "__main__":
    test_watering_system()
