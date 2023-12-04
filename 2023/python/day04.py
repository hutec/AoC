from collections import defaultdict
from functools import reduce

with open("../inputs/04", "r") as f:
    seq = f.read()
    lines = seq.split("\n")


def parse(numbers: str):
    def _int(seq, val):
        if val.isdigit():
            seq.append(int(val))
            return seq
        return seq

    return list(reduce(_int, numbers.strip().split(" "), []))


scores = {}
multipliers = defaultdict(lambda: 1)
for line in lines:
    card, numbers = line.split(":")
    card_id = int(card.split(" ")[-1])
    winning_numbers, numbers_you_have = map(parse, numbers.split("|"))

    overlap = set(winning_numbers).intersection(numbers_you_have)
    if len(overlap) > 0:
        scores[card_id] = 2 ** (len(overlap) - 1)

    for _ in range(multipliers[card_id]):
        for i in range(card_id + 1, card_id + len(overlap) + 1):
            multipliers[i] += 1

print(sum(scores.values()))
print(sum(multipliers.values()))
