import re
from typing import Tuple
from itertools import product
import operator


def add(x1: Tuple, x2: Tuple):
    """Tuple addition."""
    return tuple(map(operator.add, x1, x2))


def neighbors(x: Tuple):
    """Yield the neighbors of a coordinate."""
    for i in range(3):
        for dx in [-1, 1]:
            d = [0, 0, 0]
            d[i] = dx
            yield add(x, d)


grid = set()

with open("../inputs/day18", "r") as f:
    lines = f.read().split("\n")
    for line in lines:
        x, y, z = map(int, re.findall(r"-?\d+", line))
        grid.add((x, y, z))

open_sides = 0

for cube in grid:
    neighbour_count = 0
    for neighbor in neighbors(cube):
        if neighbor in grid:
            neighbour_count += 1

    open_sides += 6 - neighbour_count

print(open_sides)
