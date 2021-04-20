from dataclasses import dataclass
from operator import add, sub
from itertools import combinations, starmap
import re


# https://stackoverflow.com/a/16726462
sign = lambda x: x and (1, -1)[x < 0]


@dataclass
class Moon:
    position: tuple
    velocity: tuple = (0, 0, 0)

    def apply_velocity(self):
        self.position = tuple(map(add, self.position, self.velocity))

    @property
    def potential_energy(self):
        return sum(map(abs, self.position))

    @property
    def kinetic_energy(self):
        return sum(map(abs, self.velocity))

    @property
    def total_energy(self):
        return self.kinetic_energy * self.potential_energy


with open("input", "r") as f:
    inputs = f.read().split("\n")

moons = [
    Moon((1, -4, 3)),
    Moon((-14, 9, -4)),
    Moon((-4, -6, 7)),
    Moon((6, -9, -11)),
]

for _ in range(1000):
    for moon1, moon2 in combinations(moons, 2):
        gravity = tuple(map(sign, map(sub, moon1.position, moon2.position)))
        moon1.velocity = tuple(map(sub, moon1.velocity, gravity))
        moon2.velocity = tuple(map(add, moon2.velocity, gravity))

    for moon in moons:
        moon.apply_velocity()

print(sum([moon.total_energy for moon in moons]))
