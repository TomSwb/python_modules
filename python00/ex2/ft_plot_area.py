# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plot_area.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/09 09:13:45 by tschwab           #+#    #+#             #
#    Updated: 2026/10/14 13:48:44 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print("Plot area:", area)
