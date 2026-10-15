# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_seed_inventory.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:48:15 by tschwab           #+#    #+#             #
#    Updated: 2026/10/14 13:50:29 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit == "packets":
        print(seed_type, "seeds:", quantity, unit, "available")
    elif unit == "grams":
        print(seed_type, "seeds:", quantity, unit, "total")
    elif unit == "area":
        print(seed_type, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")
