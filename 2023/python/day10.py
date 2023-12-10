from collections import defaultdict

# Format is (row, col)

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
DIRECTIONS = [NORTH, SOUTH, EAST, WEST]

CONNECTIONS = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST],
    ".": [],
}


def add(a, b):
    """Add two tuples."""
    return (a[0] + b[0], a[1] + b[1])


def main():
    with open("../inputs/10", "r") as f:
        seq = f.read()
        lines = seq.split("\n")

    grid = defaultdict(lambda: ".")
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "S":
                start = (row, col)
            grid[(row, col)] = char

    # Find compatible neighbors to start
    start_neighbors = []
    for direction in DIRECTIONS:
        neighbor = add(start, direction)

        for dir in CONNECTIONS[grid[neighbor]]:
            if add(neighbor, dir) == start:
                start_neighbors.append(neighbor)
                break

    # pick any start neighbor, doesn't matter since it's a loop
    neighbor = start_neighbors[0]
    path = [start, neighbor]
    while path[-1] != start:
        for dir in CONNECTIONS[grid[path[-1]]]:
            neighbor = add(path[-1], dir)
            if neighbor == path[-2]:
                continue

            path.append(neighbor)
            break

    print(len(path) // 2)


if __name__ == "__main__":
    main()
