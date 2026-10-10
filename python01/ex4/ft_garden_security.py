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
	def __init__(self, name: str, height: int,
		days_old: int, growth_rate: int):
		if height < 0:
			print(f"{name}: Error: height can't be negative")
			self._height = 0
		else:
			self._height = height
		if days_old < 0:
			print(f"{name}: Error: age can't be negative")
			self._days_old = 0
		else:
			self._days_old = days_old
		self._name = name
		self._growth_rate = growth_rate
		
	def show(self):
		print(
			f"{self._name}: {self.get_height():.1f}cm, "
			f"{self.get_age()} days old"
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
			f"Current state: {self._name}: {self.get_height():.1f}cm, "
			f"{self.get_age()} days old"
		)

	def	get_height(self):
		return self._height

	def	get_age(self):
		return self._days_old

class Garden:
	def __init__(self):
		self._plants = []
		
	def add_plant(self, plant):
		self._plants.append(plant)
		print("Plant created:", end =" ")
		plant.show()

	def display_plants(self):
		for plant in self._plants:
			plant.show()
			
	def growing_plant(self):
		for plant in self._plants:
			plant.grow()
			plant.age()

def main():
	print("=== Garden Security System ===")

	garden = Garden()
	rose = Plant("Rose", -15, -10, 0.8)

	garden.add_plant(rose)
	print("")
	rose.set_height(25)
	rose.set_age(30)
	print("")
	rose.set_height(-25)
	rose.set_age(-30)
	print("")
	rose.show_current_state()

if __name__ == "__main__":
	main()

# dont forget chmod 777 to make executable