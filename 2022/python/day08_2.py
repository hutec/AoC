with open("../inputs/day08", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

grid = [list(map(int, l)) for l in lines]


def scenic_score(grid, row, col) -> int:
    """Get scenic score for a given tree in (row, col)."""
    if row == 0 or col == 0:
        return 0

    height = grid[row][col]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    score = 1
    for dx, dy in directions:
        y, x = row, col
        trees = 0
        while 0 <= y < len(grid) - 1 and 0 <= x < len(grid[0]) - 1:
            trees += 1
            x += dx
            y += dy
            if grid[y][x] >= height:
                break
        print(f"Saw {trees} trees in direction ({dx}, {dy})")
        score *= trees
    print(f"Scenic score for ({row}, {col}) is {score}")
    return score


scenic_score_tree(grid, 1, 2)
scenic_score_tree(grid, 3, 2)scenic_scorescenic_score