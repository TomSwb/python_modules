# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_different_errors.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/02 14:41:32 by tschwab           #+#    #+#             #
#    Updated: 2026/11/02 15:55:05 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "hello" + 25  # type: ignore[operator]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for operation in range(5):
        try:
            print(f"Testing operation {operation}...")
            garden_operations(operation)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisonError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
