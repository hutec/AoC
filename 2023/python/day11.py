from itertools import combinations
from operator import itemgetter
from collections import defaultdict


def main():
    with open("../inputs/11", "r") as f:
        seq = f.read()

        lines = seq.split("\n")

    universe = defaultdict(lambda: ".")
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            universe[(row, col)] = char

    distance_between_galaxies(expand_universe(universe, 1))
    distance_between_galaxies(expand_universe(universe, 1000000))


def distance_between_galaxies(universe):
    s = 0
    for a, b in combinations(universe.keys(), 2):
        s += abs(a[0] - b[0]) + abs(a[1] - b[1])

    print(s)


def expand_universe(universe, factor):
    rows = max(universe.keys(), key=itemgetter(0))[0]
    cols = max(universe.keys(), key=itemgetter(1))[1]

    empty_rows = []
    for row in range(rows + 1):
        if all(universe[(row, col)] == "." for col in range(cols + 1)):
            empty_rows.append(row)

    factor = factor if factor == 1 else factor - 1

    empty_cols = []
    for col in range(cols + 1):
        if all(universe[(row, col)] == "." for row in range(rows + 1)):
            empty_cols.append(col)
    expanded_universe = defaultdict(lambda: ".")
    for galaxy in filter(lambda kv: kv[1] == "#", universe.items()):
        row, col = galaxy[0]

        drow = sum([row > empty_row for empty_row in empty_rows])
        dcol = sum([col > empty_col for empty_col in empty_cols])
        expanded_universe[(row + drow * factor, col + dcol * factor)] = "#"
    return expanded_universe


if __name__ == "__main__":
    main()
