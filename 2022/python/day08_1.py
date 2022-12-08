from copy import deepcopy
from typing import List
from functools import reduce


with open("../inputs/day08", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

grid = [list(map(int, l)) for l in lines]


def visible_from_top(grid) -> List[List[bool]]:
    """Converts a grid of heights to a grid of booleans indicating whether a cell is visible from top."""
    n_cols = len(grid[0])
    n_rows = len(grid)
    visible_top = deepcopy(grid)
    for row in range(n_rows):
        for col in range(n_cols):
            if row == 0:
                visible_top[row][col] = (True, grid[row][col])  # (visible, max height)
            else:
                is_higher = grid[row][col] > visible_top[row - 1][col][1]
                if is_higher:
                    visible_top[row][col] = (True, grid[row][col])
                else:
                    visible_top[row][col] = (False, visible_top[row - 1][col][1])

    return [list(map(lambda x: x[0], row)) for row in visible_top]


def rotate_90(grid):
    transposed = zip(*grid)
    return [list(reversed(row)) for row in transposed]


def rotate_270(grid):
    return rotate_90(rotate_90(rotate_90(grid)))


def grid_or(grid1, grid2):
    for row in range(len(grid1)):
        for col in range(len(grid1[0])):
            grid1[row][col] = grid1[row][col] or grid2[row][col]
    return grid1


grid_top = visible_from_top(grid)
grid_bottom = visible_from_top(grid[::-1])[::-1]
grid_left = rotate_270(visible_from_top(rotate_90(grid)))
grid_right = rotate_90(visible_from_top(rotate_270(grid)))
visible = [grid_top, grid_bottom, grid_left, grid_right]

v = reduce(grid_or, visible[1:], visible[0])
visible_trees = sum(map(sum, v))

print(f"There are {visible_trees} visible trees.")