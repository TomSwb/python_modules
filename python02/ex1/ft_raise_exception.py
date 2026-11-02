# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_raise_exception.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/02 14:21:54 by tschwab           #+#    #+#             #
#    Updated: 2026/11/02 14:40:36 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp <= 40 and temp >= 0:
        return temp
    else:
        if temp < 0:
            raise Exception(
                f"{temp}°C is too cold for plants (min 0°C)")
        else:
            raise Exception(
                f"{temp}°C is too hot for plants (max 40°C)")


def test_temperature() -> None:

    tests = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===\n")

    for test in tests:
        try:
            print(f"Input data is '{test}'")
            temp = input_temperature(test)
            print(f"Temperature is now {temp}°C\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
