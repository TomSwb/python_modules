# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:48:10 by tschwab           #+#    #+#             #
#    Updated: 2026/10/15 19:09:19 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def count(today):
        if today > days:
            return
        print(f"Day {today}")
        count(today + 1)

    count(1)
    print("Harvest time!")
