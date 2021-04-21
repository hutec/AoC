from dataclasses import dataclass
from operator import add, sub
from functools import reduce
from itertools import combinations
import re
import math


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


# Split into x, y and z vectors
initial_xs, initial_ys, initial_zs = list(zip(*[m.position for m in moons]))

# Find cycle lenghts for x, y and z position independently
cycles = {}
i = 1
while len(cycles) != 3:
    for moon1, moon2 in combinations(moons, 2):
        gravity = tuple(map(sign, map(sub, moon1.position, moon2.position)))
        moon1.velocity = tuple(map(sub, moon1.velocity, gravity))
        moon2.velocity = tuple(map(add, moon2.velocity, gravity))

    for moon in moons:
        moon.apply_velocity()

    current_xs, current_ys, current_zs = list(zip(*[m.position for m in moons]))
    x_velocity, y_velocity, z_velocity = list(zip(*[m.velocity for m in moons]))
    if x_velocity == (0, 0, 0, 0) and current_xs == initial_xs:
        if "x" not in cycles:
            cycles["x"] = i

    if y_velocity == (0, 0, 0, 0) and current_ys == initial_ys:
        if "y" not in cycles:
            cycles["y"] = i

    if z_velocity == (0, 0, 0, 0) and current_zs == initial_zs:
        if "z" not in cycles:
            cycles["z"] = i

    if i == 1000:
        print(sum([moon.total_energy for moon in moons]))

    i += 1

# Calculate least common multiple
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


print(reduce(lcm, cycles.values()))
