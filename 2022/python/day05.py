from collections import defaultdict
from typing import Dict, List
import re
from copy import deepcopy

with open("../inputs/day05", "r") as f:
    seq = f.read()
    lines = seq.split("\n")


def split(line: str) -> Dict[str, List[int]]:
    result = defaultdict(list)
    for i in range(0, len(line)):
        crate = line[i * 4 : i * 4 + 4]
        crate = crate.strip()
        if bool(crate):
            result[i].append(crate[1])

    return result


stacks = defaultdict(list)

while "[" in lines[0]:
    line = lines.pop(0)
    for k, v in split(line).items():
        stacks[k].extend(v)

for k, v in stacks.items():
    stacks[k] = v[::-1]

stacks_1 = deepcopy(stacks)
stacks_2 = deepcopy(stacks)

for line in lines:
    m = re.search(r"move (\d+) from (\d+) to (\d+)", line)
    if m is None:
        continue

    how_many, from_stack, to_stack = map(int, m.groups())
    transfer = [stacks_1[from_stack - 1].pop() for _ in range(how_many)]
    stacks_1[to_stack - 1].extend(transfer)

    transfer = [stacks_2[from_stack - 1].pop() for _ in range(how_many)][::-1]
    stacks_2[to_stack - 1].extend(transfer)


print("".join([stacks_1[i][-1] for i in sorted(stacks_1.keys())]))
print("".join([stacks_2[i][-1] for i in sorted(stacks_2.keys())]))