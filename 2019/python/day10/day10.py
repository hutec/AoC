import math
from dataclasses import dataclass
from collections import defaultdict
from itertools import cycle


@dataclass
class Asteroid:
    x: int
    y: int

    def direction_to(self, other) -> tuple:
        """Returns normalized direction."""
        x_dir = other.x - self.x
        y_dir = other.y - self.y
        gcd = math.gcd(x_dir, y_dir)
        return (x_dir / gcd, y_dir / gcd)

    def distance_to(self, other) -> int:
        return abs(other.x - self.x) + abs(other.y - self.y)


with open("input", "r") as f:
    inputs = f.read().split("\n")

asteroids = []
for y, row in enumerate(inputs):
    for x, val in enumerate(row):
        if val == "#":
            asteroids.append(Asteroid(x, y))

best_asteroid = None
max_visible_asteroids = 0
for candidate in asteroids:
    remaining_asteroids = asteroids.copy()
    remaining_asteroids.remove(candidate)
    visible_asteroids = set(
        [candidate.direction_to(asteroid) for asteroid in remaining_asteroids]
    )

    if len(visible_asteroids) > max_visible_asteroids:
        max_visible_asteroids = len(visible_asteroids)
        best_asteroid = candidate

print(f"{max_visible_asteroids} visible from {best_asteroid}")

# Part 2
remaining_asteroids = asteroids.copy()
remaining_asteroids.remove(best_asteroid)
visible = defaultdict(list)
for asteroid in remaining_asteroids:
    direction = best_asteroid.direction_to(asteroid)
    # Handle the coordination system (y is pointing down)
    angle = math.degrees(math.atan2(direction[0], -direction[1])) % 360
    visible[angle].append(asteroid)


vaporized = 1
for direction in cycle(sorted(visible.keys())):
    asteroids = visible[direction]
    if not asteroids:
        continue

    closest = min(asteroids, key=lambda a: best_asteroid.distance_to(a))
    visible[direction].remove(closest)
    vaporized += 1

    if vaporized == 201:
        print(closest.x * 100 + closest.y)
        break