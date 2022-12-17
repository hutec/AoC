import ast
from functools import cmp_to_key
from copy import deepcopy


def compare(left, right):
    left = deepcopy(left)
    right = deepcopy(right)

    if type(left) == type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None

    left = [left] if type(left) == int else left
    right = [right] if type(right) == int else right

    while len(left) != 0 and len(right) != 0:
        c = compare(left.pop(0), right.pop(0))
        if c is not None:
            return c

    if len(left) == len(right) == 0:
        return None
    return len(left) == 0


def part1():
    with open("../inputs/day13", "r") as f:
        seq = f.read()
        lines = seq.split("\n\n")

    s = 0
    for idx, line in enumerate(lines):
        left, right = map(ast.literal_eval, line.split("\n"))
        if compare(left, right):
            s += idx + 1

    print(s)


def part2():
    with open("../inputs/day13", "r") as f:
        seq = f.read()
        lines = seq.split("\n")
    lines = [ast.literal_eval(l) for l in lines if l != ""]
    lines.append([[2]])
    lines.append([[6]])

    # Bubble sort
    for i in range(len(lines)):
        for j in range(len(lines) - 1):
            if not compare(lines[j], lines[j + 1]):
                lines[j], lines[j + 1] = lines[j + 1], lines[j]

    print((lines.index([[2]]) + 1) * (lines.index([[6]]) + 1))


if __name__ == "__main__":
    part1()
    part2()