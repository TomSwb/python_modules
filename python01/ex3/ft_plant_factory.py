# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_factory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:53:48 by tschwab           #+#    #+#             #
#    Updated: 2026/10/18 18:23:24 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float,
                 days_old: int, growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.days_old = days_old
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")


class Garden:
    def __init__(self) -> None:
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print("Created:", end=" ")
        plant.show()


def main() -> None:
    rose = Plant("Rose", 25, 30, 0.8)
    oak = Plant("Oak", 200, 365, 10)
    cactus = Plant("Cactus", 5, 90, 1.6)
    sunflower = Plant("Sunflower", 80, 45, 1.2)
    fern = Plant("Fern", 15, 120, 1.6)

    garden = Garden()

    print("=== Plant Factory Output ===")
    garden.add_plant(rose)
    garden.add_plant(oak)
    garden.add_plant(cactus)
    garden.add_plant(sunflower)
    garden.add_plant(fern)


if __name__ == "__main__":
    main()
