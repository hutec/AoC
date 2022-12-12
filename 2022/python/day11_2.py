import operator
from functools import reduce
from math import gcd
from typing import List, Dict, Callable
from dataclasses import dataclass
from day11_1 import parse


@dataclass
class Monkey:
    items: List[int]
    operation: Callable[[int], int]
    test_divisibly_by: int
    if_true_throw_to: int
    if_false_throw_to: int
    activities: int = 0
    least_common_multiple: int = None

    def turn(self, monkeys: Dict[int, "Monkey"]):
        while self.items:
            self.activities += 1
            worry_level = self.items.pop(0)
            current_worry_level = self.operation(worry_level)
            # The following line is keeping the worrying level small
            # current_worry_level = current_worry_level % self.least_common_multiple
            if (current_worry_level % self.test_divisibly_by) == 0:
                monkeys[self.if_true_throw_to].items.append(current_worry_level)
            else:
                monkeys[self.if_false_throw_to].items.append(current_worry_level)


def main():
    monkeys: Dict[int, Monkey] = {}

    with open("../inputs/day11", "r") as f:
        seq = f.read()
        lines = seq.split("\n")

    i = 0
    while (i * 7) < len(lines):
        monkeys[i] = parse(lines[(i * 7) + 1 : (i * 7) + 6])
        i += 1

    # Find least common multiple of all monkeys' divisor to keep the worry level small
    divisors = [monkey.test_divisibly_by for monkey in monkeys.values()]
    lcm = reduce(lambda x, y: x * y // gcd(x, y), divisors)

    for monkey in monkeys.values():
        monkey.least_common_multiple = lcm

    for _ in range(1):
        for i in range(len(monkeys)):
            monkeys[i].turn(monkeys)

    activity_counts = [monkey.activities for monkey in monkeys.values()]
    monkey_buiness = operator.mul(*sorted(activity_counts)[-2:])
    print(f"Level of monkey business: {monkey_buiness}")


if __name__ == "__main__":
    main()