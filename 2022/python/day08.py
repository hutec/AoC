with open("../inputs/day08", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

grid = [list(map(int, l)) for l in lines]


def scenic_score(grid, row, col) -> int:
    """Get scenic score for a given tree in (row, col)."""
    height = grid[row][col]
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # up, left, right, down
    score = 1
    for dy, dx in directions:
        y, x = row, col
        trees = 0
        while (0 < y < len(grid) - 1) and (0 < x < len(grid[0]) - 1):
            y, x = y + dy, x + dx
            trees += 1
            if height <= grid[y][x]:
                break
        score *= trees
    return score


def is_visible(grid, row, col) -> bool:
    """Check if given tree is visible from the sides."""
    height = grid[row][col]
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # up, left, right, down
    for dy, dx in directions:
        y, x = row, col
        visible = True
        while (0 < y < len(grid) - 1) and (0 < x < len(grid[0]) - 1):
            y, x = y + dy, x + dx
            if height <= grid[y][x]:
                visible = False
                break
        if visible:
            return True
    return False


m = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        m += is_visible(grid, row, col)

print(f"{m} trees are visible from the sides.")

m = -1
for row in range(len(grid)):
    for col in range(len(grid[0])):
        m = max(m, scenic_score(grid, row, col))
print(f"Maximum scenic score is {m}.")