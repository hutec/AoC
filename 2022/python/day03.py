with open("../inputs/day03", "r") as f:
    seq = f.read()
    rucksacks = seq.split("\n")


def priority(item: str) -> int:
    """Return the priotity of an item.

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    """
    return ord(item) - 38 if item.isupper() else ord(item) - 96


priority_sum = 0
for rucksack in rucksacks:
    mid = len(rucksack) // 2
    left = rucksack[:mid]
    right = rucksack[mid:]
    shared_item = set(left).intersection(right).pop()
    priority_sum += priority(shared_item)

print(f"Sum of priorities: {priority_sum}")


priority_sum = 0
for i in range(len(rucksacks) // 3):
    group = rucksacks[i * 3 : i * 3 + 3]
    shared_item = set(group[0]).intersection(group[1], group[2]).pop()
    priority_sum += priority(shared_item)

print(f"Sum of priorities in groups: {priority_sum}")
