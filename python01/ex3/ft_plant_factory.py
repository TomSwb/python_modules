# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_factory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:53:48 by tschwab           #+#    #+#             #
#    Updated: 2026/10/18 18:31:45 by tschwab          ###   ########.ch       #
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


def main() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30, 0.8)
    print("Created:", end=" ")
    rose.show()
    oak = Plant("Oak", 200, 365, 10)
    print("Created:", end=" ")
    oak.show()
    cactus = Plant("Cactus", 5, 90, 1.6)
    print("Created:", end=" ")
    cactus.show()
    sunflower = Plant("Sunflower", 80, 45, 1.2)
    print("Created:", end=" ")
    sunflower.show()
    fern = Plant("Fern", 15, 120, 1.6)
    print("Created:", end=" ")
    fern.show()


if __name__ == "__main__":
    main()
