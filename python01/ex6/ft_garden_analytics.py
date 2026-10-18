# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_analytics.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:59:36 by tschwab           #+#    #+#             #
#    Updated: 2026/10/18 19:48:57 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

# Plant class: inits the plant and control them
# Allow to show info, grow the plant and age them
# Record calls statistics
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
        self._statistics = Plant.Statistics(self)

    # Anonymous init of a plant if needed
    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0, 0)

    # ---- Display methods ----#

    # Display the plant main information
    def show(self) -> None:
        print(
            f"{self._name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )
        self._statistics.record_show()

    # Display the plant current state
    def show_current_state(self) -> None:
        print(
            f"Current state: {self._name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )

    # ---- Growth and Aging related methods ---- #

    # Grows the plant by one time its growth rate
    def grow(self, growth: float) -> None:
        if growth == 0:
            self._height += self._growth_rate
        else:
            self._height += growth
        self._statistics.record_growth()

    # Ages the plant by one day
    def age(self, days: int) -> None:
        if days == 0:
            self._days_old += 1
        else:
            self._days_old += days
        self._statistics.record_age()

    # Allow to set the height manually
    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self.get_height()}cm")

    # Allow to set the age manually
    def set_age(self, days_old: int) -> None:
        if days_old < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days_old = days_old
            print(f"Age updated: {self.get_age()} days")

    # Return the height of the plant
    def get_height(self) -> float:
        return self._height

    # Return the age of the plant
    def get_age(self) -> int:
        return self._days_old

    # static method to see if an age is more than a year or not
    @staticmethod
    def is_older_than_a_year(age: int) -> None:
        if age < 365:
            print(f"Is {age} days more than a year? -> False")
        else:
            print(f"Is {age} days more than a year? -> True")

    # ---- Statistics ---- #

    # Stat class records different functions calls
    # Display shades calls only if the instance is a Tree
    class Statistics:
        def __init__(self, plant: Plant) -> None:
            self._plant = plant
            self._show_calls = 0
            self._grow_calls = 0
            self._age_calls = 0
            self._producing_shade_calls = 0

        def record_show(self) -> None:
            self._show_calls += 1

        def record_growth(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_producing_shade(self) -> None:
            self._producing_shade_calls += 1

        def show(self) -> None:
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

    # Sets the bloom status
    def bloom(self) -> None:
        if self._bloom is False:
            self._bloom = True
        else:
            self._bloom = False


# Seed class adds a seed parameter, holding how many seeds the flower has
# once bloomed
class Seed(Flower):
    def __init__(self, name: str, height: float, days_old: int,
                 growth_rate: float, color: str, bloom: bool,
                 seeds: int) -> None:
        super().__init__(name, height, days_old, growth_rate, color, bloom)
        self._seeds = seeds

    def show(self) -> None:
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
                 growth_rate: int, trunk_diameter: int,
                 producing_shade: bool) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._producing_shade = producing_shade

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    # Sets the produce shade status
    def produce_shade(self) -> None:
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
                 growth_rate: float, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self._harvest_season = harvest_season.capitalize()
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    # age() override allows to increment the nutritional value
    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days

    # Allow the vegie to both grow and age at the same time
    def grow_and_age(self, time: int) -> None:
        for _ in range(time):
            super().grow(0)
            self.age(1)


# Displays the statistics
def show_statistics(self) -> None:
    self._statistics.show()


def main() -> None:
    print("=== Garden statistics ===")

    # Create the different plants for the garden
    rose = Flower("Rose", 15, 10, 0.8, "red", False)
    oak = Tree("Oak", 200, 365, 10, 5, False)
    sunflower = Seed("Sunflower", 80, 45, 1.5, "yellow", False, 42)
    anonymous = Plant.anonymous()

    # Testing year old check function
    print("=== Check year-old")
    Plant.is_older_than_a_year(30)
    Plant.is_older_than_a_year(400)
    print()

    # Testing flower display, functions and stats
    print("=== Flower")
    rose.show()
    rose.show_statistics()
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    rose.show_statistics()
    print()

    # Testing tree display, functions and stats
    print("=== Tree")
    oak.show()
    oak.show_statistics()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show_statistics()
    print()

    # Testing seed display, functions and stats
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    sunflower.show_statistics()
    print()

    # Testing anonymous display and stats
    print("=== Anonymous")
    anonymous.show()
    anonymous.show_statistics()


if __name__ == "__main__":
    main()
