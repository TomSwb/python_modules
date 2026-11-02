# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_finally_block.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/02 15:58:45 by tschwab           #+#    #+#             #
#    Updated: 2026/11/02 16:27:06 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    try:
        print("Testing valid plants...")
        print("Opening watering system")
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


def main() -> None:
    print("=== Garden Watering System ===\n")

    plants = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(plants)
    plants = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(plants)


if __name__ == "__main__":
    main()
