# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_raise_exception.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/02 14:21:54 by tschwab           #+#    #+#             #
#    Updated: 2026/11/02 14:34:53 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp <= 40 and temp >= 0:
        return temp
    else:
        if temp < 0:
            raise Exception
            (f"Caught input_temperature error: {temp}°C is too"
            f" cold for plants (min 0°C)\n")
        else:
            raise Exception
            (f"Caught input_temperature error: {temp}°C is too"
            f" hot for plants (min 40°C)\n")

def test_temperature() -> None:
    test1 = "25"
    test2 = "abc"
    test3 = "100"
    test4 = "-50"
    tests = [test1, test2, test3, test3]

    print("=== Garden Temperature Checker ===\n")

    while test in tests:
        try:
            print(f"Input data is '{test}'")
            temp = input_temperature(test)
            print(f"Temperature is now {temp}°C\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
