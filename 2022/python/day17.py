from typing import List, Tuple
from dataclasses import dataclass
from collections import defaultdict
from itertools import cycle


@dataclass
class Rock:
    """Coordinates start in the bottom left."""

    coordinates: List[Tuple[int, int]]
    width: int

    def check_collision(self, xy: Tuple[int], grid: dict) -> bool:
        for coordinate in self.coordinates:
            if grid[add(coordinate, xy)]:
                return True

        return False

    def solidify(self, xy: Tuple[int], grid: dict):
        for coordinate in self.coordinates:
            grid[add(coordinate, xy)] = True


def add(x1, x2):
    """Tuple addition."""
    return (x1[0] + x2[0], x1[1] + x2[1])


def max_y(grid: dict) -> int:
    return max([k[1] for k, v in grid.items() if v is True])


def grid_to_list(grid):

    return [
        int("".join(map(str, [int(grid[(x, y)]) for x in range(7)])), 2)
        for y in range(max_y(grid), 0, -1)
    ]


def find_cycle(t: list):
    """Find the cycle in a list of integers."""
    for i in range(10, len(t), 2):
        half = i // 2
        if t[:half] == t[half : 2 * half]:
            return half
    return None


rocks = [
    Rock([(0, 0), (1, 0), (2, 0), (3, 0)], 4),
    Rock([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)], 3),
    Rock([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], 3),
    Rock([(0, 0), (0, 1), (0, 2), (0, 3)], 1),
    Rock([(0, 0), (1, 0), (1, 1), (0, 1)], 2),
]

jets_to_dx = {
    ">": (1, 0),
    "<": (-1, 0),
}


def main():
    grid = defaultdict(bool)
    for i in range(7):
        grid[(i, 0)] = True

    with open("../inputs/day17", "r") as f:
        jets = cycle(f.read())

    n_rocks = 0
    for rock in cycle(rocks):
        m = max_y(grid)
        xy = (2, m + 4)
        while True:
            # Move horizontally
            jet = next(jets)
            if jet == ">":
                dx = 1 if xy[0] + rock.width < 7 else 0
            elif jet == "<":
                dx = -1 if xy[0] > 0 else 0

            if rock.check_collision(add(xy, (dx, 0)), grid) is False:
                xy = add(xy, (dx, 0))

            # Move vertically
            if rock.check_collision(add(xy, (0, -1)), grid) is False:
                xy = add(xy, (0, -1))
            else:
                rock.solidify(xy, grid)
                break

        if n_rocks == 2022:
            print(m)

        n_rocks += 1

        # two cylce, n_rocks = 3719
        # three cycles,  n_rocks = 5466, max_y = 8686
        # four cycles, n_rocks = 7210
        # five cycles, n_rocks = 8954
        # six cycle, n_rocks = 10698
        # +350 base

        # every 1744 rocks, there is a cycle that adds 2778 height

        # First try was 1592889908236


if __name__ == "__main__":
    main()
