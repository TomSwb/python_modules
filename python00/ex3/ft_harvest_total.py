# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_harvest_total.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tomswb <tomswb@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:47:44 by tomswb            #+#    #+#             #
#    Updated: 2026/10/14 13:49:04 by tomswb           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total():
    day_1 = int(input("Day 1 harvest: "))
    day_2 = int(input("Day 2 harvest: "))
    day_3 = int(input("Day 3 harvest: "))
    total = day_1 + day_2 + day_3
    print("Total harvest:", total)
