from typing import Iterator

# (row, col)
directions = [
    (1, 0),  # down
    (0, 1),  # right
    (-1, 0),  # up
    (0, -1),  # left
]


def add(xs, ys):
    return (xs[0] + ys[0], xs[1] + ys[1])


def get(grid, position):
    return grid[position[0]][position[1]]


def dfs(grid, position) -> Iterator[tuple[int, int]]:
    if get(grid, position) == 9:
        yield position

    for step in directions:
        new_position = add(position, step)
        if (
            0 <= new_position[0] < rows
            and 0 <= new_position[1] < cols
            and get(grid, new_position) == get(grid, position) + 1
        ):
            yield from dfs(grid, new_position)


grid = []
with open("../inputs/10", "r") as f:
    lines = f.read().splitlines()
    for row, line in enumerate(lines):
        grid.append(list(map(int, line)))

rows = len(grid)
cols = len(grid[0])
candidates = []
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == 0:
            candidates.append((r, c))


total = 0
for candidate in candidates:
    total += len(set(dfs(grid, candidate)))
print(total)

total = 0
for candidate in candidates:
    total += len(list(dfs(grid, candidate)))

print(total)
