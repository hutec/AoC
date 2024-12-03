import re
from operator import mul

with open("../inputs/03", "r") as f:
    memory = f.readlines()

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
enable_pattern = r"don't\(\)"
disable_pattern = r"do\(\)"

total = 0
for line in memory:
    matches = re.findall(mul_pattern, line)
    for numbers in matches:
        total += mul(*map(int, numbers))
print(total)

total = 0
enabled = True
for line in memory:
    # Assemble matches in a sorted stack walk through it
    mul_matches = list(re.finditer(mul_pattern, line))
    enable_matches = list(re.finditer(enable_pattern, line))
    disable_matches = list(re.finditer(disable_pattern, line))

    stack = mul_matches + enable_matches + disable_matches
    stack = sorted(stack, key=lambda m: m.start())

    for match in stack:
        if (numbers := match.groups()) and enabled:
            total += mul(*map(int, numbers))
        elif match.group() == "don't()":
            enabled = False
        elif match.group() == "do()":
            enabled = True

print(total)
