from functools import cache

with open("../inputs/11", "r") as f:
    stones = list(map(int, f.read().split()))


@cache
def n_stones(stone: int, level: int) -> int:
    if level == 0:
        return 1

    if stone == 0:
        return n_stones(1, level - 1)
    elif len(str(stone)) % 2 == 0:
        val = str(stone)
        left = int(val[: len(val) // 2])
        right = int(val[len(val) // 2 :])
        return n_stones(left, level - 1) + n_stones(right, level - 1)
    else:
        return n_stones(stone * 2024, level - 1)


print(sum(n_stones(stone, 25) for stone in stones))
print(sum(n_stones(stone, 75) for stone in stones))
