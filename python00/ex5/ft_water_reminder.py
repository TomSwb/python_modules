# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_water_reminder.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tomswb <tomswb@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/14 13:48:01 by tomswb            #+#    #+#             #
#    Updated: 2026/10/14 13:49:39 by tomswb           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
