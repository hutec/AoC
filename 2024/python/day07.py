from typing import Iterator
import re
from operator import mul, add


def concat(a, b):
    return int(str(a) + str(b))


operators = [mul, add, concat]


with open("../inputs/07", "r") as f:
    lines = f.readlines()


def compute(values) -> Iterator[int]:
    """Compute all possible results from the given values and operators."""
    if len(values) == 1:
        yield values[0]

    else:
        for operator in operators:
            yield from compute([operator(values[0], values[1])] + values[2:])


total = 0
for line in lines:
    nums = list(map(int, re.findall(r"\d+", line)))
    target, values = nums[0], nums[1:]
    if target in compute(values):
        total += target

print(total)
