import operator
from typing import List, Dict, Callable
from dataclasses import dataclass
from functools import partial


@dataclass
class Monkey:
    items: List[int]
    operation: Callable[[int], int]
    test_divisibly_by: int
    if_true_throw_to: int
    if_false_throw_to: int
    activities: int = 0

    def turn(self, monkeys: Dict[int, "Monkey"]):
        while self.items:
            self.activities += 1
            worry_level = self.items.pop(0)
            current_worry_level = self.operation(worry_level) // 3
            if (current_worry_level % self.test_divisibly_by) == 0:
                monkeys[self.if_true_throw_to].items.append(current_worry_level)
            else:
                monkeys[self.if_false_throw_to].items.append(current_worry_level)


monkeys: Dict[int, Monkey] = {}

with open("../inputs/day11", "r") as f:
    seq = f.read()
    lines = seq.split("\n")


def parse_operation(line: str) -> Callable[[int, int], int]:
    operations = {
        "*": operator.mul,
        "+": operator.add,
    }
    op, factor = line.split("=")[1].strip().split(" ")[1:]
    operation = operations[op]
    if factor == "old":
        return lambda x: operation(x, x)

    return partial(operation, int(factor))


def parse(lines: List[str]) -> Monkey:
    items = [int(x.strip()) for x in lines[0].split(":")[1].split(",")]
    operation = parse_operation(lines[1])
    test_divisibly_by = int(lines[2].split(" ")[-1])
    if_true_throw_to = int(lines[3].split(" ")[-1])
    if_false_throw_to = int(lines[4].split(" ")[-1])
    return Monkey(
        items, operation, test_divisibly_by, if_true_throw_to, if_false_throw_to
    )


def main():
    i = 0
    while (i * 7) < len(lines):
        monkeys[i] = parse(lines[(i * 7) + 1 : (i * 7) + 6])
        i += 1

    for _ in range(20):
        for monkey in monkeys.values():
            monkey.turn(monkeys)

    activity_counts = [monkey.activities for monkey in monkeys.values()]
    monkey_buiness = operator.mul(*sorted(activity_counts)[-2:])
    print(f"Level of monkey business: {monkey_buiness}")


if __name__ == "__main__":
    main()