import re
from functools import reduce
from collections import defaultdict
from operator import mul


with open("../inputs/02", "r") as f:
    seq = f.read()
    lines = seq.split("\n")


# Part 1
games = {}
for line in lines:
    game, draws = line.split(":")
    id = int(game.split(" ")[-1])
    draws = draws.strip()

    cubes = defaultdict(int)
    for count, color in re.findall(r"(\d+) (\w+)", draws):
        cubes[color] = max(cubes[color], int(count))

    games[id] = cubes


def is_possible(cubes):
    return cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14


print(
    sum(
        map(
            lambda game: game[0],
            filter(lambda game: is_possible(game[1]), games.items()),
        )
    )
)

# Part 2


def power(cubes):
    return reduce(mul, cubes.values())


print(sum(map(power, games.values())))
