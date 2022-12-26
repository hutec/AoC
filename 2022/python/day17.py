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


def print_grid(grid):
    for y in range(max_y(grid), 0, -1):
        for x in range(7):
            if grid[(x, y)]:
                print("#", end="")
            else:
                print(".", end="")
        print()


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
    while True:
        for rock in rocks:
            xy = (2, max_y(grid) + 4)
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

            n_rocks += 1

            if n_rocks == 2022:
                print(max_y(grid))
                exit()


if __name__ == "__main__":
    main()
