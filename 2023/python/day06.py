import re

with open("../inputs/06", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

durations = list(map(int, re.findall(r"(\d+)", lines[0])))
distances = list(map(int, re.findall(r"(\d+)", lines[1])))

r = 1
for duration, distance in zip(durations, distances):
    possible_distances = [
        charge * (duration - charge) for charge in range(duration + 1)
    ]
    r *= sum(map(lambda d: d > distance, possible_distances))

print(r)

duration = int("".join(map(str, durations)))
distance = int("".join(map(str, distances)))

possible_distances = [charge * (duration - charge) for charge in range(duration + 1)]
print(sum(map(lambda d: d > distance, possible_distances)))
