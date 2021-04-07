import math

# Load inputs

with open("input", "r") as f:
    seq = f.read()
    masses = map(int, seq.split("\n"))

# Core functions

def compute_fuel(mass):
    return math.floor(mass / 3) - 2


def compute_fuel_recursive(mass, acc=0):
    fuel = compute_fuel(mass)
    if fuel <= 0:
        return acc

    return compute_fuel_recursive(fuel, acc + fuel)


# Testing Part 1

examples = [(12, 2), (14, 2), (1969, 654), (100756, 33583)]

for mass, expected in examples:
    assert compute_fuel(mass) == expected


# Testing Part 2

examples = [(14, 2), (1969, 966), (100756, 50346)]

for mass, expected in examples:
    assert compute_fuel_recursive(mass) == expected


print(sum(map(compute_fuel, masses)))
print(sum(map(compute_fuel_recursive, masses)))
