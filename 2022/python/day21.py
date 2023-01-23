import operator

operations = {
    "*": operator.mul,
    "/": operator.truediv,
    "+": operator.add,
    "-": operator.sub,
}


def calc(monkeys, key: str) -> int:
    if isinstance(monkeys[key], int):
        return monkeys[key]

    m1, op, m2 = monkeys[key]
    return operations[op](calc(monkeys, m1), calc(monkeys, m2))


def main():
    with open("../inputs/day21", "r") as f:
        lines = f.read().split("\n")
        monkeys = {}
        for line in lines:
            key, val = line.split(":")
            val = val.strip().split(" ")
            if len(val) == 1:
                val = int(val[0])
            monkeys[key] = val

    # Part 1
    print(int(calc(monkeys, "root")))

    # Part 2
    monkeys["root"][1] = "-"

    min_ = 0
    max_ = calc(monkeys, "root")
    while True:
        t = (min_ + max_) // 2
        monkeys["humn"] = int(t)
        r = calc(monkeys, "root")
        if r == 0:
            print(monkeys["humn"])
            break
        elif r < 0:
            max_ = t
        elif r > 0:
            min_ = t


if __name__ == "__main__":
    main()