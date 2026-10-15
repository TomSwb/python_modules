# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_data.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:52:56 by tschwab           #+#    #+#             #
#    Updated: 2026/10/14 14:11:28 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Garden:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def display_plants(self):
        for plant in self.plants:
            plant.show()


def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    garden = Garden()

    garden.add_plant(rose)
    garden.add_plant(sunflower)
    garden.add_plant(cactus)

    print("=== Garden Plant Registry ===")
    garden.display_plants()


if __name__ == "__main__":
    main()

# #!/usr/bin/env python3
# dont forget chmod 755 to make executable
