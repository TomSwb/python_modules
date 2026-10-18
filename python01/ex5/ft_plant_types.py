# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_types.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:56:35 by tschwab           #+#    #+#             #
#    Updated: 2026/10/18 19:25:49 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float,
                 days_old: int, growth_rate: float) -> None:
        self._name = name.capitalize()
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if days_old < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._days_old = 0
        else:
            self._days_old = days_old
        self._growth_rate = growth_rate

    def show(self) -> None:
        print(
            f"{self._name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._days_old += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, days_old: int) -> None:
        if days_old < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days_old = days_old
            print(f"Age updated: {self._days_old} days")

    def show_current_state(self) -> None:
        print(
            f"Current state: {self._name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_old


class Flower(Plant):
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: float, color: str, bloom: bool) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self._color = color.lower()
        self._bloom = bloom

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._bloom:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")

    def bloom(self) -> None:
        self._bloom = True


class Tree(Plant):
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: float, trunk_diameter: float,
                 producing_shade: bool) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._producing_shade = producing_shade

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self._producing_shade = True
        print(
            f"Tree {self._name} now produces a shade of {self._height:.1f}cm "
            f"long and {self._trunk_diameter:.1f}cm wide."
            )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: float, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self._harvest_season = harvest_season.capitalize()
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def grow_and_age(self, time: int) -> None:
        for _ in range(time):
            super().grow()
            self.age()


def main() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 15, 10, 0.8, "red", False)
    oak = Tree("Oak", 200, 365, 10, 5, False)
    tomato = Vegetable("Tomato", 5, 10, 2.1, "April", 0)

    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow_and_age(20)
    tomato.show()


if __name__ == "__main__":
    main()
