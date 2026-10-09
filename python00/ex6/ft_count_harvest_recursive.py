# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomswb <tomswb@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/09 09:36:54 by tomswb            #+#    #+#              #
#    Updated: 2026/10/09 09:50:33 by tomswb           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	
	def	count(today):
		if today > days:
			return
		print("Day", today)
		count(today + 1)
	
	count(1)
	print("Harvest time!")
