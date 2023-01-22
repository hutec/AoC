from typing import List, Any
from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    value: int
    id: int


def move(seq: List[Any], idx: int, offset: int) -> List[Any]:
    """Move an item in a list from one position to another."""
    new_idx = idx + offset

    if new_idx >= len(seq) or new_idx < 0:
        new_idx = new_idx % (len(seq) - 1)
        if new_idx == 0:
            new_idx = len(seq) - 1

    seq.insert(new_idx, seq.pop(idx))
    return seq


def part1():
    with open("../inputs/day20", "r") as f:
        lines = f.read().split("\n")
        file = []
        nodes = []
        for idx, node in enumerate(lines):
            node = Node(int(node), idx)
            if node.value == 0:
                zero_node = node

            nodes.append(node)
            file.append(node)

    for node in nodes:
        current_idx = file.index(node)
        move(file, current_idx, node.value)

    print(solution(file, zero_node))


def part2():
    decrytpion_key = 811589153
    with open("../inputs/day20", "r") as f:
        lines = f.read().split("\n")
        file = []
        nodes = []
        for idx, node in enumerate(lines):
            node = Node(int(node) * decrytpion_key, idx)
            if node.value == 0:
                zero_node = node

            nodes.append(node)
            file.append(node)

    for _ in range(10):
        for node in nodes:
            current_idx = file.index(node)
            move(file, current_idx, node.value)

    print(solution(file, zero_node))


def solution(file, start_node) -> int:
    return sum(
        [
            file[(file.index(start_node) + offset) % len(file)].value
            for offset in [1000, 2000, 3000]
        ]
    )


if __name__ == "__main__":
    part1()
    part2()
