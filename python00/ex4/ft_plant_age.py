# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_age.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:47:53 by tschwab           #+#    #+#             #
#    Updated: 2026/10/15 19:08:11 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

def ft_plant_age() -> None:
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
