# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_grow.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tomswb <tomswb@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:53:18 by tomswb            #+#    #+#             #
#    Updated: 2026/10/14 14:12:20 by tomswb           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, height, days_old, growth_rate):
        self.name = name
        self.height = height
        self.days_old = days_old
        self.growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")

    def grow(self):
        self.height += self.growth_rate

    def age(self):
        self.days_old += 1


class Garden:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def display_plants(self):
        for plant in self.plants:
            plant.show()

    def growing_plant(self):
        for plant in self.plants:
            plant.grow()
            plant.age()


def main():
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
