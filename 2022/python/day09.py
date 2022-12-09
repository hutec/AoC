import operator
from collections import defaultdict
from itertools import starmap

with open("../inputs/day09", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0),
}

visited = set()
head = tail = (0, 0)  # (y , x)


def is_adjacent(pos1, pos2) -> bool:
    return abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1


def add(t1, t2):
    return tuple(starmap(operator.add, zip(t1, t2)))


for line in lines:
    if line:
        d, steps = line.split(" ")
    else:
        break

    for _ in range(int(steps)):
        head = add(head, directions[d])
        if not is_adjacent(head, tail):
            dy, dx = head[0] - tail[0], head[1] - tail[1]
            dy = dy // abs(dy) if dy != 0 else 0
            dx = dx // abs(dx) if dx != 0 else 0
            tail = add(tail, (dy, dx))

        visited.add(tail)

print(f"Visited {len(visited)} cells.")