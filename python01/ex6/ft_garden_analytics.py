# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_analytics.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tomswb <tomswb@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:59:36 by tomswb            #+#    #+#             #
#    Updated: 2026/10/14 14:35:22 by tomswb           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

# Garden class, initialising the whole garden array,
# Allow to see the whole garden registry
# Allow to grow the whole garden at once
class Garden:
    def __init__(self):
        self._plants = []

    def add_plant(self, plant):
        self._plants.append(plant)
        # print("Plant created:", end =" ")
        # plant.show()

    def display_plants(self):
        for plant in self._plants:
            plant.show()

    def growing_plant(self):
        for plant in self._plants:
            plant.grow()
            plant.age()


# Plant class: inits the plant and control them
# Allow to show info, grow the plant and age them
# Record calls statistics
class Plant:
    def __init__(self, name: str = "???", height: float = 0,
                 days_old: int = 0, growth_rate: float = 0):
        self._name = name.capitalize()
        if height < 0:
            print(f"{name}: Error: height can't be negative")
            self._height = 0
        else:
            self._height = height
        if days_old < 0:
            print(f"{name}: Error: age can't be negative")
            self._days_old = days_old
        else:
            self._days_old = days_old
        self._growth_rate = growth_rate
        self._statistics = Plant.Statistics(self)

    # Anonymous init of a plant if needed
    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0, 0, 0)

    # ---- Display methods ----#

    # Display the plant main information
    def show(self):
        print(
            f"{self._name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )
        self._statistics.record_show()

    # Display the plant current state
    def show_current_state(self):
        print(
            f"Current state: {self._name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )

    # Displays the plant calls statistics
    def show_statistics(self):
        self._statistics.show()

    # ---- Growth and Aging related methods ---- #

    # Grows the plant by one time its growth rate
    def grow(self, _growth: float):
        if _growth == 0:
            self._height += self._growth_rate
        else:
            self._height += _growth
        self._statistics.record_growth()

    # Ages the plant by one day
    def age(self, _days: int):
        if _days == 0:
            self._days_old += 1
        else:
            self._days_old += _days
        self._statistics.record_age()

    # Allow to set the height manually
    def set_height(self, _height: float):
        if _height < 0:
            print(f"{self._name}: Error: height can't be negative")
            print("Height update rejected")
        else:
            self._height = _height
            print(f"Height updated: {self.get_height()}cm")

    # Allow to set the age manually
    def set_age(self, _days_old: int):
        if _days_old < 0:
            print(f"{self._name}: Error: age can't be negative")
            print("Age update rejected")
        else:
            self._days_old = _days_old
            print(f"Age updated: {self.get_age()} days")

    # Return the height of the plant
    def get_height(self):
        return self._height

    # Return the age of the plant
    def get_age(self):
        return self._days_old

    # static method to see if an age is more than a year or not
    @staticmethod
    def is_older_than_a_year(_age):
        if _age < 365:
            print(f"Is {_age} days more than a year? -> False")
        else:
            print(f"Is {_age} days more than a year? -> True")

    # ---- Statistics ---- #

    # Stat class records different functions calls
    # Display shades calls only if the instance is a Tree
    class Statistics:
        def __init__(self, plant):
            self._plant = plant
            self._show_calls = 0
            self._grow_calls = 0
            self._age_calls = 0
            self._producing_shade_calls = 0

        def record_show(self):
            self._show_calls += 1

        def record_growth(self):
            self._grow_calls += 1

        def record_age(self):
            self._age_calls += 1

        def record_producing_shade(self):
            self._producing_shade_calls += 1

        def show(self):
            print(f"[statistics for {self._plant._name}]")
            print(
                f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                f"{self._show_calls} show"
                )
            if isinstance(self._plant, Tree):
                print(f" {self._producing_shade_calls} shade")


# Flower class adds a color and bloom parameters
# Color is self-explanotory, Bloom allows to see if the flower has bloom or not
# The show() override allow to display the new information
class Flower(Plant):
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: int, color: str, bloom: bool):
        super().__init__(name, height, days_old, growth_rate)
        self._color = color.lower()
        self._bloom = bloom

    def show(self):
        super().show()
        print(f" Color: {self._color}")
        if not self._bloom:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")

    # Sets the bloom status
    def bloom(self):
        if self._bloom is False:
            self._bloom = True
        else:
            self._bloom = False


# Seed class adds a seed parameter, holding how many seeds the flower has
# once bloomed
class Seed(Flower):
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: int, color: str, bloom: bool, seeds: int):
        super().__init__(name, height, days_old, growth_rate, color, bloom)
        self._seeds = seeds

    def show(self):
        super().show()
        if not self._bloom:
            print(" Seeds: 0")
        else:
            print(f" Seeds: {self._seeds}")


# Tree class adds a trunk diameter and a producing shade status
# Trunk diameter is self-explanotory, Producing shade allows to see if the
# tree has has a shade or not
# The show() override allow to display the new information
class Tree(Plant):
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: int, trunk_diameter: int, producing_shade: bool):
        super().__init__(name, height, days_old, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._producing_shade = producing_shade

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    # Sets the produce shade status
    def produce_shade(self):
        if self._producing_shade is False:
            self._producing_shade = True
            print(
                f"Tree {self._name} now produces a shade of {self._height:.1f}"
                f"cm long and {self._trunk_diameter:.1f}cm wide."
                )
            self._statistics.record_producing_shade()
        else:
            self._producing_shade = False


# Vegetable class adds a harvest season and a nutritional value
# Both are self-explanotory.
# The show() override allow to display the new information
class Vegetable(Plant):
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: int, harvest_season: str,
                 nutritional_value: int):
        super().__init__(name, height, days_old, growth_rate)
        self._harvest_season = harvest_season.capitalize()
        self._nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    # Allow the vegie to both grow and age at the same time
    def grow_and_age(self, time: int):
        print(f"[make {self._name.lower()} grow and age for {time} days]")

        for days in range(time):
            super().grow(time)
            super().age(time)
            self._nutritional_value += 1


def main():
    print("=== Garden statistics ===")

    # Create the garden
    garden = Garden()

    # Create the different plants for the garden
    rose = Flower("Rose", 15, 10, 0.8, "red", False)
    oak = Tree("Oak", 200, 365, 10, 5, False)
    sunflower = Seed("Sunflower", 80, 45, 1.5, "yellow", False, 42)
    anonymous = Plant.anonymous()

    # Addubg all the plants to the garden, allows to display them all
    garden.add_plant(rose)
    garden.add_plant(oak)
    garden.add_plant(sunflower)
    garden.add_plant(anonymous)

    # Testing year old check function
    print("=== Check year-old")
    Plant.is_older_than_a_year(30)
    Plant.is_older_than_a_year(400)

    # Testing flower display, functions and stats
    print("\n=== Flower")
    rose.show()
    rose.show_statistics()
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    rose.show_statistics()

    # Testing tree display, functions and stats
    print("\n=== Tree")
    oak.show()
    oak.show_statistics()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show_statistics()

    # Testing seed display, functions and stats
    print("\n=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    sunflower.show_statistics()

    # Testing anonymous display and stats
    print("\n=== Anonymous")
    anonymous.show()
    anonymous.show_statistics()


if __name__ == "__main__":
    main()


# #!/usr/bin/env python3
# dont forget chmod 755 to make executable
