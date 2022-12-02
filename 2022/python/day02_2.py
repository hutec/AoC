from enum import Enum
from dataclasses import dataclass


class Outcome(Enum):
    LOST = 0
    DRAW = 3
    WON = 6


@dataclass
class Rock:
    score: int = 1

    def vs(self, outcome: Outcome):
        if outcome == Outcome.DRAW:
            return Rock()
        elif outcome == Outcome.WON:
            return Paper()
        elif outcome == Outcome.LOST:
            return Scissors()


@dataclass
class Paper:
    score: int = 2

    def vs(self, outcome: Outcome):
        if outcome == Outcome.DRAW:
            return Paper()
        elif outcome == Outcome.WON:
            return Scissors()
        elif outcome == Outcome.LOST:
            return Rock()


@dataclass
class Scissors:
    score: int = 3

    def vs(self, outcome: Outcome):
        if outcome == Outcome.DRAW:
            return Scissors()
        elif outcome == Outcome.WON:
            return Rock()
        elif outcome == Outcome.LOST:
            return Paper()


to_shapes = {
    "A": Rock(),
    "B": Paper(),
    "C": Scissors(),
}

to_outcomes = {
    "X": Outcome.LOST,
    "Y": Outcome.DRAW,
    "Z": Outcome.WON,
}


with open("../inputs/day02", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

total_score = 0
for line in lines:
    s1 = to_shapes[line.split(" ")[0]]
    outcome = to_outcomes[line.split(" ")[1]]

    s2 = s1.vs(outcome)
    new_score = s2.score + outcome.value
    print(f"{s1} vs {outcome} -> {s2} ({new_score})")
    total_score += new_score

print(f"Total score: {total_score}")
