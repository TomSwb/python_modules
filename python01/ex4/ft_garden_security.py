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
	def __init__(self, _name: str = "???", _height: int = 5,
		_days_old: int = 5, _growth_rate: int = 0.5):
		if _height < 0:
			print(f"{name}: Error: height can't be negative")
			return False
		else:
			self._height = _height
		if _days_old < 0:
			print(f"{name}: Error: age can't be negative")
			return False
		else:
			self._days_old = _days_old
		self._name = _name
		self._growth_rate = _growth_rate
		
	def show(self):
		print(
			f"{self._name}: {self._height:.1f}cm,"
			f" {self._days_old} days old"
		)
		
	def grow(self):
		self._height += self._growth_rate

	def age(self):
		self._days_old += 1

	def	set_height(self, _height: int):
		if _height < 0:
			print(f"{self._name}: Error: height can't be negative")
			print("Height update rejected")
		else:
			self._height = _height
			print(f"Height updated: {self._height}cm")

	def	set_age(self, _days_old: int):
		if _days_old < 0:
			print(f"{self._name}: Error: age can't be negative")
			print("Age update rejected")
		else:
			self._days_old = _days_old
			print(f"Age updated: {self._days_old} days")
	
	def	show_current_state(self):
		print(
			f"Current state: {self._name}: {self.get_height():.1f}cm,"
			f" {self.get_age()} days old"
		)

	def	get_height(self):
		return self._height

	def	get_age(self):
		return self._days_old

class Garden:
	def __init__(self):
		self.plants = []
		
	def add_plant(self, plant):
		self.plants.append(plant)
		print("Plant created:", end =" ")
		plant.show()
		
	def display_plants_creation(self):
		for plant in self.plants:
			plant.show()

	def display_plants(self):
		for plant in self.plants:
			plant.show()
			
	def growing_plant(self):
		for plant in plants:
			plant.grow()
			plant.age()

def main():
	rose = Plant("Rose", 25, 30, 0.8)
	# oak = Plant("Oak", 200, 365, 10)
	# cactus = Plant("Cactus", 5, 90, 1.6)
	# sunflower = Plant("Sunflower", 80, 45, 1.2)
	# fern = Plant("Fern", 15, 120, 1.6)

	garden = Garden()

	print("=== Garden Security System ===")
	garden.add_plant(rose)
	print("")
	rose.set_height(25)
	rose.set_age(30)
	print("")
	rose.set_height(-25)
	rose.set_age(-30)
	print("")
	rose.show_current_state()

	# garden.add_plant(oak)
	# garden.add_plant(cactus)
	# garden.add_plant(sunflower)
	# garden.add_plant(fern)

if __name__ == "__main__":
	main()

# dont forget chmod 777 to make executable