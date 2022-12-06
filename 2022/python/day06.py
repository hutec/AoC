from typing import List


with open("../inputs/day06", "r") as f:
    seq = f.read().split("\n")[0]


def is_unique(s: List[str], n_unique: int) -> bool:
    """Check if sequence has `n_unique` unique characters."""
    return len(set(s)) == n_unique


def find_first_unique(seq, n_unique) -> int:
    """Find the first occurence of a sequence with `n_unique` unique characters."""
    for i in range(len(seq) - n_unique + 1):
        if is_unique(seq[i : i + n_unique], n_unique):
            return i
    return -1


part_1 = find_first_unique(seq, 4)
part_2 = find_first_unique(seq, 14)

print(f"First occurence part 1: {part_1 + 4}")
print(f"First occurence part 2: {part_2 + 14}")