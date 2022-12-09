import operator
from typing import Tuple

with open("../inputs/day09", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0),
}


def is_adjacent(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> bool:
    return abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1


def add(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> Tuple[int, int]:
    return tuple(map(operator.add, pos1, pos2))


def simulate(lines: list, length: int) -> int:
    visited = set()
    knots = [(0, 0)] * length

    for line in lines:
        d, steps = line.split(" ")
        for _ in range(int(steps)):
            knots[0] = add(knots[0], directions[d])
            for i in range(1, len(knots)):
                if not is_adjacent(knots[i], knots[i - 1]):
                    dy = knots[i - 1][0] - knots[i][0]
                    dx = knots[i - 1][1] - knots[i][1]
                    dy = dy // abs(dy) if dy != 0 else 0
                    dx = dx // abs(dx) if dx != 0 else 0
                    knots[i] = add(knots[i], (dy, dx))

            visited.add(knots[-1])
    return len(visited)


print(simulate(lines, length=2))
print(simulate(lines, length=10))
