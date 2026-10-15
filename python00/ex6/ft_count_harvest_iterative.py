# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:48:05 by tschwab           #+#    #+#             #
#    Updated: 2026/10/14 13:49:53 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    today = 1
    while today <= days:
        print("Day", today)
        today = today + 1
    print("Harvest time!")
