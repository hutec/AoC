from collections import defaultdict

with open("../inputs/day14", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

grid = defaultdict(bool)


def populate_grid(coords: list):
    # Iterate over pairs of coordinates
    for i in range(len(coords) - 1):
        c1 = coords[i]
        c2 = coords[i + 1]

        # Iterate over all coordinates between the two
        for col in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1):
            for row in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1):
                grid[(col, row)] = True


for line in lines:
    coords = []
    for cs in line.split("->"):
        col, row = map(int, cs.strip().split(","))
        coords.append((col, row))

    populate_grid(coords)

abyss = max(grid.keys(), key=lambda x: x[1])[1]


def simulate_sand(grid) -> bool:
    """In-place simulation of falling sand. Return false if sand fell out of the grid, true otherwise.

    Sand falls down, left-down or right-down.
    """

    # Down, left-down, right-down
    directions = [(0, 1), (-1, 1), (1, 1)]
    sand_cur_position = (500, 0)
    sand_next_position = None
    while sand_next_position is None or sand_cur_position != sand_next_position:
        if sand_next_position is not None:
            sand_cur_position = sand_next_position

        if sand_cur_position[1] >= abyss:
            return False

        for dx, dy in directions:
            if not grid[(sand_cur_position[0] + dx, sand_cur_position[1] + dy)]:
                sand_next_position = (
                    sand_cur_position[0] + dx,
                    sand_cur_position[1] + dy,
                )
                break

    grid[sand_cur_position] = True
    return True


i = 0
while simulate_sand(grid):
    i += 1

print(i)
