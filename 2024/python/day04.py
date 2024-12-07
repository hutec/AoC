from collections import defaultdict
from itertools import product

with open("../inputs/04", "r") as f:
    lines = f.readlines()


# Parse the puzzle into a dict
puzzle = defaultdict(lambda: ".")
for row_idx, row in enumerate(lines):
    for col_idx, col in enumerate(row):
        puzzle[(row_idx, col_idx)] = col

DIRECTIONS = [d for d in product([-1, 0, 1], repeat=2) if d != (0, 0)]


def add(xs, ys):
    """Tuple addition"""
    return tuple(map(sum, zip(xs, ys)))


def mul(xs, i):
    """Tuple multiplication"""
    return tuple(map(lambda x: x * i, xs))


def check_word_in_direction(position, direction, puzzle, word="XMAS"):
    for i in range(len(word)):
        if puzzle[add(position, mul(direction, i))] != word[i]:
            return False
    return True


xmas_count = 0
for pos, val in puzzle.copy().items():
    if val == "X":
        for direction in DIRECTIONS:
            if check_word_in_direction(pos, direction, puzzle):
                xmas_count += 1

print(xmas_count)


def check_diagonal(position, puzzle, word="MAS"):
    _word1 = (
        puzzle[add(position, (-1, -1))]
        + puzzle[position]
        + puzzle[add(position, (1, 1))]
    )
    _word2 = (
        puzzle[add(position, (-1, 1))]
        + puzzle[position]
        + puzzle[add(position, (1, -1))]
    )

    return (_word1 == word or _word1 == word[::-1]) and (
        _word2 == word or _word2 == word[::-1]
    )


xmas_count = 0
for pos, val in puzzle.copy().items():
    if val == "A":
        xmas_count += check_diagonal(pos, puzzle)

print(xmas_count)
