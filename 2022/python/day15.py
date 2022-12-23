import re
from typing import Tuple, List
from dataclasses import dataclass

with open("../inputs/day15", "r") as f:
    seq = f.read()
    lines = seq.split("\n")


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def y_overlap(sensor_x, sensor_y, radius, y) -> Tuple[int, int]:
    """Return the x coordinates of the overlap between a circle in taxicab geometry and a line."""
    dy = abs(sensor_y - y)
    if dy < radius:
        dx = radius - dy
        return sensor_x - dx, sensor_x + dx


def simplify_overlaps(overlaps: List[Tuple[int, int]]):
    """Simplify a list of overlaps by merging overlapping intervals."""
    overlaps.sort()
    simplified = []
    for overlap in overlaps:
        if not simplified:
            simplified.append(overlap)
            continue

        lo, hi = overlap
        slo, shi = simplified[-1]

        if lo > shi + 1:
            simplified.append(overlap)
            continue

        simplified[-1] = (slo, max(shi, hi))

    return simplified


def part1():
    overlaps = []
    for line in lines:
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall(r"-?\d+", line))
        radius = distance(sensor_x, sensor_y, beacon_x, beacon_y)
        overlap = y_overlap(sensor_x, sensor_y, radius, 2000000)
        if overlap is not None:
            overlaps.append(overlap)

    overlaps = simplify_overlaps(overlaps)
    print(sum([hi - lo for lo, hi in overlaps]))


def part2():
    t = []
    for line in lines:
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall(r"-?\d+", line))
        radius = distance(sensor_x, sensor_y, beacon_x, beacon_y)
        t.append((sensor_x, sensor_y, radius))

    y_max = 4000000
    for y in range(y_max):
        overlaps = []
        for sensor_x, sensor_y, radius in t:
            overlap = y_overlap(sensor_x, sensor_y, radius, y)
            if overlap is not None:
                overlap = max(0, overlap[0]), min(y_max, overlap[1])
                overlaps.append(overlap)

        overlaps = simplify_overlaps(overlaps)
        if len(overlaps) == 2:
            print((overlaps[0][1] + 1) * 4000000 + y)
            return


if __name__ == "__main__":
    part1()
    part2()
