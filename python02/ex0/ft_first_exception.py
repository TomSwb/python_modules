# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_first_exception.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/02 14:21:47 by tschwab           #+#    #+#             #
#    Updated: 2026/11/02 14:21:49 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    test1 = "25"
    test2 = "abc"

    print("=== Garden Temperature ===\n")

    try:
        print(f"Input data is '{test1}'")
        temp1 = input_temperature(test1)
        print(f"Temperature is now {temp1}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        print(f"Input data is '{test2}'")
        temp2 = input_temperature(test2)
        print(f"Temperature is now {temp2}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
