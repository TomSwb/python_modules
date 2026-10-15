# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_harvest_total.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:47:44 by tschwab           #+#    #+#             #
#    Updated: 2026/10/14 13:49:04 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total():
    day_1 = int(input("Day 1 harvest: "))
    day_2 = int(input("Day 2 harvest: "))
    day_3 = int(input("Day 3 harvest: "))
    total = day_1 + day_2 + day_3
    print("Total harvest:", total)
