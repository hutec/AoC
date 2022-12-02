from enum import Enum
from dataclasses import dataclass


class Outcome(Enum):
    LOST = 0
    DRAW = 3
    WON = 6


@dataclass
class Rock:
    score: int = 1

    def vs(self, other):
        if isinstance(other, Rock):
            return self.score + Outcome.DRAW.value
        elif isinstance(other, Paper):
            return self.score + Outcome.LOST.value
        elif isinstance(other, Scissors):
            return self.score + Outcome.WON.value


@dataclass
class Paper:
    score: int = 2

    def vs(self, other):
        if isinstance(other, Rock):
            return self.score + Outcome.WON.value
        elif isinstance(other, Paper):
            return self.score + Outcome.DRAW.value
        elif isinstance(other, Scissors):
            return self.score + Outcome.LOST.value


@dataclass
class Scissors:
    score: int = 3

    def vs(self, other):
        if isinstance(other, Rock):
            return self.score + Outcome.LOST.value
        elif isinstance(other, Paper):
            return self.score + Outcome.WON.value
        elif isinstance(other, Scissors):
            return self.score + Outcome.DRAW.value


to_shapes = {
    "A": Rock(),
    "B": Paper(),
    "C": Scissors(),
    "X": Rock(),
    "Y": Paper(),
    "Z": Scissors(),
}


with open("../inputs/day02", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

total_score = 0
for line in lines:
    s1, s2 = map(to_shapes.get, line.split(" "))
    total_score += s2.vs(s1)

print(f"Total score: {total_score}")
