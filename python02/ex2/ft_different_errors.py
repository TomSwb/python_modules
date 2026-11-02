# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_different_errors.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/02 14:41:32 by tschwab           #+#    #+#             #
#    Updated: 2026/11/02 14:55:32 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        raise ValueError
    elif operation_number == 1:
        raise ZeroDivisionError
    elif operation_number == 2:
        raise FileNotFoundError
    elif operation_number == 3:
        raise TypeError
    else:
        print("Operation completed successfully\n")
        return


def test_error_types() -> None:
    operation = 0

    while operation < 5:
        print(f"Testing operation {operation}...\n")
        try:
            garden_operations(operation)
        except Exception as e:
            print(f"{e}\n")
        operation += 1

    print("All error types tested successfully!\n")


if __name__ == "__main__":
    test_error_types()
