import re
from itertools import cycle
from dataclasses import dataclass
import math


def main():
    with open("../inputs/08", "r") as f:
        seq = f.read()
        directions, nodes = seq.split("\n\n")

    network = {}
    for node in nodes.split("\n"):
        source, left, right = re.findall(r"[1-9|A-Z]+", node)
        network[source] = {"L": left, "R": right, "visited": []}

    current = "AAA"
    steps = 0
    for direction in cycle(directions):
        current = network[current][direction]
        steps += 1

        if current == "ZZZ":
            break

    print(steps)

    # Note: This solution works because **Z loops back to **Z in the same steps as
    #   as it takes to go from **A to **Z.
    counts = []
    for current in network.keys():
        if not current.endswith("A"):
            continue

        steps = 0
        for direction in cycle(directions):
            current = network[current][direction]
            steps += 1

            if current.endswith("Z"):
                counts.append(steps)
                break

    print(math.lcm(*counts))


if __name__ == "__main__":
    main()
