#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomswb <tomswb@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/10 20:16:03 by tomswb            #+#    #+#              #
#    Updated: 2026/10/10 20:16:04 by tomswb           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


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
        
    def display_plants_creation(self):
        for plant in self.plants:
            plant.show()

    def display_plants(self):
        for plant in self.plants:
            splant.show()
            
    def growing_plant(self):
        for plant in plants:
            plant.grow()
            plant.age()

def main():
	rose = Plant("Rose", 25, 30, 0.8)
	oak = Plant("Oak", 200, 365, 10)
	cactus = Plant("Cactus", 5, 90, 1.6)
	sunflower = Plant("Sunflower", 80, 45, 1.2)
	fern = Plant("Fern", 15, 120, 1.6)

	garden = Garden()

	garden.add_plant(rose)
	garden.add_plant(oak)
	garden.add_plant(cactus)
	garden.add_plant(sunflower)
	garden.add_plant(fern)

	print("=== Plant Factory Output ===")
	garden.display_plants_creation()

if __name__ == "__main__":
	main()

# dont forget chmod 777 to make executable