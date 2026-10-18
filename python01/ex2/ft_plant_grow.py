# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_grow.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:53:18 by tschwab           #+#    #+#             #
#    Updated: 2026/10/18 18:12:02 by tschwab          ###   ########.ch       #
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

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days_old += 1


class Garden:
    def __init__(self) -> None:
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)

    def display_plants(self) -> None:
        for plant in self.plants:
            plant.show()

    def growing_plant(self) -> None:
        for plant in self.plants:
            plant.grow()
            plant.age()


def main() -> None:
    rose = Plant("Rose", 25, 30, 0.8)
    sunflower = Plant("Sunflower", 80, 45, 1.2)
    cactus = Plant("Cactus", 15, 120, 1.6)

    garden = Garden()

    garden.add_plant(rose)
    garden.add_plant(sunflower)
    garden.add_plant(cactus)

    print("=== Garden Plant Growth ===")
    rose.show()
    i = 1
    days = 7
    starting_height = rose.height
    while i <= days:
        print(f"=== Day{i} ===")
        rose.grow()
        rose.age()
        rose.show()
        i += 1
    growth = rose.height - starting_height
    print(f"Growth this week: {round(growth, 1)} cm")


if __name__ == "__main__":
    main()

# #!/usr/bin/env python3
# dont forget chmod 755 to make executable
