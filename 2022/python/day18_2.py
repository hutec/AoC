import re
from typing import Tuple
from collections import deque
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
            _x = add(x, d)
            if all(map(lambda x: -1 <= x <= 20, _x)):
                yield _x


cubes = set()
water = {(0, 0, 0)}
front = deque(water)

with open("../inputs/day18", "r") as f:
    lines = f.read().split("\n")
    for line in lines:
        x, y, z = map(int, re.findall(r"-?\d+", line))
        cubes.add((x, y, z))

while front:
    for neighbor in neighbors(front.pop()):
        if neighbor not in water and neighbor not in cubes:
            water.add(neighbor)
            front.append(neighbor)

exterior = 0

for cube in cubes:
    neighbour_count = 0
    for neighbor in neighbors(cube):
        if neighbor in water:
            exterior += 1

print(exterior)
