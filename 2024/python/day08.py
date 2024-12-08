from itertools import combinations, starmap
from collections import defaultdict

with open("../inputs/08", "r") as f:
    lines = f.read().splitlines()


antennas = defaultdict(list)

for row_idx, row in enumerate(lines):
    for col_idx, col in enumerate(row):
        if col != "." and col != "#":
            antennas[col].append((row_idx, col_idx))

height = len(lines)
width = len(lines[0])


def antinodes(antenna1: tuple[int], antenna2: tuple[int]) -> list[tuple[int]]:
    """Return the two antinodes of the two antennas."""

    dr, dc = antenna1[0] - antenna2[0], antenna1[1] - antenna2[1]

    return [
        (antenna1[0] + dr, antenna1[1] + dc),
        (antenna2[0] - dr, antenna2[1] - dc),
    ]


def antinodes_v2(antenna1: tuple[int], antenna2: tuple[int]) -> list[tuple[int]]:
    """Return all antinodes of the two antennas."""

    dr, dc = antenna1[0] - antenna2[0], antenna1[1] - antenna2[1]

    nodes = set()

    i = 0
    while 0 <= antenna1[0] + i * dr < height and 0 <= antenna1[1] + i * dc < width:
        nodes.add((antenna1[0] + i * dr, antenna1[1] + i * dc))
        i += 1

    i = 0
    while 0 <= antenna1[0] + i * dr < height and 0 <= antenna1[1] + i * dc < width:
        nodes.add((antenna1[0] + i * dr, antenna1[1] + i * dc))
        i -= 1

    return nodes


seen = set()
for antenna, coords in antennas.items():
    for nodes in starmap(antinodes, combinations(coords, 2)):
        seen |= set(nodes)

# Filter out the nodes that are not in the grid
seen = list(filter(lambda node: 0 <= node[0] < height and 0 <= node[1] < width, seen))
print(len(seen))


seen = set()
for antenna, coords in antennas.items():
    for nodes in starmap(antinodes_v2, combinations(coords, 2)):
        seen |= set(nodes)

print(len(seen))
