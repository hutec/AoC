import itertools


def follow_path(path) -> dict:
    """Builds a dict mapping position to step number of first visit."""
    x, y = 0, 0
    positions = {(0, 0): 0}
    step_count = 0
    for p in path:
        direction, steps = p[0], p[1:]
        steps = int(steps)
        if direction == "R":
            new_positions = itertools.product(range(x, x + steps), [y])
            x += steps
        elif direction == "L":
            new_positions = itertools.product(range(x, x - steps, -1), [y])
            x -= steps
        elif direction == "U":
            new_positions = itertools.product([x], range(y, y + steps))
            y += steps
        elif direction == "D":
            new_positions = itertools.product([x], range(y, y - steps, -1))
            y -= steps

        for pos in new_positions:
            if pos not in positions:
                positions[pos] = step_count

            step_count += 1

    return positions


def minimal_distance(path1, path2):
    """Returns the minimal distance to an intersection."""
    intersections = set(follow_path(path1).keys()).intersection(
        follow_path(path2).keys()
    )
    intersections.remove((0, 0))
    return min([abs(x) + abs(y) for x, y in intersections])


def minimal_delay(path1, path2):
    positions_path1 = follow_path(path1)
    positions_path2 = follow_path(path2)
    intersections = set(positions_path1.keys()).intersection(positions_path2.keys())
    intersections.remove((0, 0))

    return min(
        [positions_path1[isect] + positions_path2[isect] for isect in intersections]
    )


example = ["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]

assert minimal_distance(*example) == 6
assert minimal_delay(*example) == 30

with open("input", "r") as f:
    path1, path2 = f.read().split("\n")
    path1 = path1.split(",")
    path2 = path2.split(",")


print(minimal_distance(path1, path2))
print(minimal_delay(path1, path2))
