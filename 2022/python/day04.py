import re
from typing import List


def contains(range1: List[int], range2: List[int]) -> bool:
    """Return True if range1 is contained within range2."""
    return range1[0] >= range2[0] and range1[1] <= range2[1]


def overlaps(range1: List[int], range2: List[int]) -> bool:
    """Return True if range1 overlaps range2."""
    return range1[0] <= range2[1] and range1[1] >= range2[0]


with open("../inputs/day04", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

count_contained = 0
count_overlapping = 0
for sections in lines:
    m = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", sections)
    ranges = list(map(int, m.groups()))
    range1 = ranges[:2]
    range2 = ranges[2:]
    if contains(range1, range2) or contains(range2, range1):
        count_contained += 1

    if overlaps(range1, range2) or overlaps(range2, range1):
        count_overlapping += 1

print(f"Count of contained ranges: {count_contained}")
print(f"Count of overlapping ranges: {count_overlapping}")