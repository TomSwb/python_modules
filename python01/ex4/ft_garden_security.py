# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_security.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:55:14 by tschwab           #+#    #+#             #
#    Updated: 2026/10/18 19:25:44 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float,
                 days_old: int, growth_rate: float) -> None:
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if days_old < 0:
            print(f"{name}: Error, age can't be negative")
            self._days_old = 0
        else:
            self._days_old = days_old
        self._name = name
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


def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15, 10, 0.8)
    print("Plant created:", end=" ")
    rose.show()
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-25)
    rose.set_age(-30)
    print()

    rose.show_current_state()


if __name__ == "__main__":
    main()
