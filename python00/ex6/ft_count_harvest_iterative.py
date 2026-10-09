# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomswb <tomswb@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/09 09:31:10 by tomswb            #+#    #+#              #
#    Updated: 2026/10/09 09:35:47 by tomswb           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	today = 1
	while today <= days:
		print("Day", today)
		today = today + 1
	print("Harvest time!")