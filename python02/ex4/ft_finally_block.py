# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_finally_block.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/02 15:58:45 by tschwab           #+#    #+#             #
#    Updated: 2026/11/02 16:13:16 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Invalid name to water") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "") -> None:
        super().__init__(message)


def check_tank(level: int) -> None:
    if level < 2:
        raise PlantError()
    elif level < 5:
        raise WaterError()


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    plants = {"Tomato", "Lettuce", "Carrots"}

    print("Testing valid plants...")
    print("Open watering system")
    for plant in plants:
        try:
            water_plant(plant)
        except GardenError as e:
            print(f"Caught PlantError: {e}: '{plant}'")
            print("... ending tests and returning to main")
        finally:
            print("Closing watering system")
    

if __name__ == "__main__":
    test_watering_system()
