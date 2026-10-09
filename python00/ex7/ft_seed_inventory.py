# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomswb <tomswb@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/09 09:53:10 by tomswb            #+#    #+#              #
#    Updated: 2026/10/09 10:07:36 by tomswb           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	seed_type = seed_type.capitalize()
	if unit == "packets":
		print(seed_type, "seeds:", quantity, unit, "available")
	elif unit == "grams":
		print(seed_type, "seeds:", quantity, unit, "total")
	elif unit == "area":
		print(seed_type, "seeds: covers", quantity, "square meters")
	else:
		print("Unknown unit type")