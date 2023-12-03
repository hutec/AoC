import re
import operator
from itertools import product
from collections import defaultdict

with open("../inputs/03", "r") as f:
    seq = f.read()
    lines = seq.split("\n")


def neighbors(positions):
    positions = set(positions)
    _neighbors = set()
    for y, x in positions:
        for dy, dx in product([-1, 0, 1], repeat=2):
            r = y + dy, x + dx
            if r not in positions:
                _neighbors.add(r)
    return _neighbors


def add(a, b):
    return tuple(map(operator.add, a, b))


# Build board
board = defaultdict(lambda: ".")
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        board[(y, x)] = char

# Find numbers and check their neighbours
part_numbers = []
for y, line in enumerate(lines):
    for match in re.finditer(r"\d+", line):
        positions = [(y, x) for x in range(match.start(), match.end())]
        if any([board[nb] != "." for nb in neighbors(positions)]):
            part_numbers.append(int(match.group()))

print(sum(part_numbers))

gears = defaultdict(list)

for y, line in enumerate(lines):
    for match in re.finditer(r"\d+", line):
        positions = [(y, x) for x in range(match.start(), match.end())]
        for nb in neighbors(positions):
            if board[nb] == "*":
                gears[nb].append(int(match.group()))

p = 0
for gear in gears.values():
    if len(gear) == 2:
        p += gear[0] * gear[1]

print(p)
