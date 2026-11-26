# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_inventory_system.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/19 18:45:03 by tschwab           #+#    #+#             #
#    Updated: 2026/11/19 18:45:04 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

import sys


if __name__ == "__main__":
    print("=== Inventory system analisys ===")

    items = []

    for item in sys.argv[1:]:
        try:
            i = int(item)
            item.append(i)
        except ValueError:
            print(f"Invalid parameter: {item!r}")