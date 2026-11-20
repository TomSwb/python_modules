# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_score_analytics.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tschwab <tschwab@student.42lausanne.ch>    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/19 18:41:47 by tschwab           #+#    #+#             #
#    Updated: 2026/11/20 13:42:38 by tschwab          ###   ########.ch       #
#                                                                             #
# *************************************************************************** #

import sys


def process_scores() -> None:
    print("=== Player Score Analytics ===")

    scores = []

    for score in sys.argv[1:]:
        try:
            n = int(score)
            scores.append(n)
        except ValueError:
            print(f"Invalid parameter: {score!r}")

    size_scores = len(scores)

    if size_scores == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...\n")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {size_scores}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / size_scores}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}\n")


if __name__ == "__main__":
    process_scores()
