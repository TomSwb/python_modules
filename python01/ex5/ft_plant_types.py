# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_types.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tomswb <tomswb@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:56:35 by tomswb            #+#    #+#             #
#    Updated: 2026/10/14 14:20:41 by tomswb           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

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


class Plant:
    def __init__(self, name: str = "???", height: int = 0,
                 days_old: int = 0, growth_rate: float = 0):
        self._name = name.capitalize()
        if height < 0:
            print(f"{name}: Error: height can't be negative")
            self._height = height
        else:
            self._height = height
        if days_old < 0:
            print(f"{name}: Error: age can't be negative")
            self._days_old = days_old
        else:
            self._days_old = days_old
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

    def set_height(self, _height: int):
        if _height < 0:
            print(f"{self._name}: Error: height can't be negative")
            print("Height update rejected")
        else:
            self._height = _height
            print(f"Height updated: {self._height}cm")

    def set_age(self, _days_old: int):
        if _days_old < 0:
            print(f"{self._name}: Error: age can't be negative")
            print("Age update rejected")
        else:
            self._days_old = _days_old
            print(f"Age updated: {self._days_old} days")

    def show_current_state(self):
        print(
            f"Current state: {self._name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )

    def get_height(self):
        return self._height

    def get_age(self):
        return self._days_old


class Flower(Plant):
    def __init__(self, name: str, height: int, days_old: int,
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

    def bloom(self):
        print(f"[asking the {self._name.lower()} to bloom]")
        self._bloom = True


class Tree(Plant):
    def __init__(self, name: str, height: int, days_old: int,
                 growth_rate: int, trunk_diameter: int, producing_shade: bool):
        super().__init__(name, height, days_old, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._producing_shade = producing_shade

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self):
        print(f"[asking the {self._name.lower()} to produce shade]")
        self._producing_shade = True
        print(
            f"Tree {self._name} now produces a shade of {self._height:.1f}cm "
            f"long and {self._trunk_diameter:.1f}cm wide."
            )


class Vegetable(Plant):
    def __init__(self, name: str, height: int, days_old: int,
                 growth_rate: int, harvest_season: str,
                 nutritional_value: int):
        super().__init__(name, height, days_old, growth_rate)
        self._harvest_season = harvest_season.capitalize()
        self._nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow_and_age(self, time: int):
        print(f"[make {self._name.lower()} grow and age for {time} days]")
        for days in range(time):
            super().grow()
            super().age()
            self._nutritional_value += 1


def main():
    print("=== Garden Plant Types ===")

    garden = Garden()

    rose = Flower("Rose", 15, 10, 0.8, "red", False)
    oak = Tree("Oak", 200, 365, 10, 5, False)
    tomato = Vegetable("Tomato", 5, 10, 2.1, "April", 0)

    garden.add_plant(rose)
    garden.add_plant(oak)
    garden.add_plant(tomato)

    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato.show()
    tomato.grow_and_age(20)
    tomato.show()


if __name__ == "__main__":
    main()


# #!/usr/bin/env python3
# dont forget chmod 755 to make executable
