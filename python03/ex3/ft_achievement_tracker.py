# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_achievement_tracker.py                          :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/19 18:42:45 by tschwab           #+#    #+#             #
#    Updated: 2026/11/19 18:42:46 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

import random


def gen_player_achievements(lst: list[str]) -> set[str]:

    i = random.randint(0, 14)
    player_has = set(random.sample(lst, i))
    return set(player_has)


if __name__ == "__main__":

    print("=== Achievement Tracker System ===\n")

    achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer', 'Hidden Pathfinder']

    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    distinct = alice.union(bob, charlie, dylan)

    print(f"All distinct archievements: {distinct}\n")

    common = alice.intersection(bob, charlie, dylan)

    print(f"Common achievements: {common}\n")

    only_alice = alice.difference(bob, charlie, dylan)
    only_bob = bob.difference(alice, charlie, dylan)
    only_charlie = charlie.difference(bob, alice, dylan)
    only_dylan = dylan.difference(bob, charlie, alice)

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}\n")

    achievement = set(achievements)

    missing_alice = achievement.difference(alice)
    missing_bob = achievement.difference(bob)
    missing_charlie = achievement.difference(charlie)
    missing_dylan = achievement.difference(dylan)

    print(f"Alice is missing: {missing_alice}")
    print(f"Bob is missing: {missing_bob}")
    print(f"Charlie is missing: {missing_charlie}")
    print(f"Dylan is missing: {missing_dylan}\n")
