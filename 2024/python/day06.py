from copy import deepcopy

with open("../inputs/06", "r") as f:
    lines = f.read().splitlines()

grid = {}
pos = (0, 0)
for row_idx, row in enumerate(lines):
    for col_idx, col in enumerate(row):
        grid[(row_idx, col_idx)] = col
        if col == "^":
            pos = (row_idx, col_idx)

DIRECTIONS = [
    (-1, 0),  # Up
    (0, 1),  # Right
    (1, 0),  # Down
    (0, -1),  # Left
]


def add(xs, ys):
    """Tuple addition"""
    return tuple(map(sum, zip(xs, ys)))


start_pos = pos

visited = set()
direction_idx = 0
while True:
    visited.add(pos)
    next_pos = add(pos, DIRECTIONS[direction_idx])

    if next_pos not in grid:
        break

    if grid[next_pos] == "." or grid[next_pos] == "^":
        pos = next_pos
    else:
        direction_idx = (direction_idx + 1) % 4

print(len(visited))


loops = 0
# Check all possible locations where one could put a new obstacle
for obstacle_pos, val in grid.items():
    if val == "#" or val == "^":
        continue

    grid[obstacle_pos] = "#"
    pos = start_pos

    # Run simulation and check if loop occurs
    visited = set()
    direction_idx = 0
    while True:
        if (pos, direction_idx) in visited:
            loops += 1
            break

        visited.add((pos, direction_idx))
        next_pos = add(pos, DIRECTIONS[direction_idx])

        if next_pos not in grid:
            break

        if grid[next_pos] == "." or grid[next_pos] == "^":
            pos = next_pos
        else:
            direction_idx = (direction_idx + 1) % 4

    grid[obstacle_pos] = "."

print(loops)
