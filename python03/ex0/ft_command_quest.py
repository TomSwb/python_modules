# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_command_quest.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/19 18:41:06 by tschwab           #+#    #+#             #
#    Updated: 2026/11/20 12:57:58 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

import sys


def print_sys_arg() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    size = len(sys.argv)
    args = 0
    if size > 1:
        print(f"Arguments received: {size - 1}")
        for arg in sys.argv[1:]:
            args = args + 1
            print(f"Argument {args}: {arg}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {size}")


if __name__ == "__main__":
    print_sys_arg()
