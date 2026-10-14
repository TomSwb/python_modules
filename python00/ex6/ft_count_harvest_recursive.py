# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tomswb <tomswb@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:48:10 by tomswb            #+#    #+#             #
#    Updated: 2026/10/14 13:51:23 by tomswb           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(today):
        if today > days:
            return
        print("Day", today)
        count(today + 1)

    count(1)
    print("Harvest time!")
