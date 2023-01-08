import re
from typing import List, Tuple
from functools import lru_cache
import operator
import math


TYPES = ["ore", "clay", "obsidian", "geode"]


def get_blueprints() -> List[Tuple[Tuple[int]]]:
    blueprints = []
    with open("../inputs/day19", "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            blueprint = []
            for section in line.split(": ")[1].split(". "):
                recipe = [0, 0, 0, 0]
                for (cost, robot) in re.findall(r"(\d+) (\w+)", section):
                    recipe[TYPES.index(robot)] = int(cost)
                blueprint.append(tuple(recipe))
            blueprints.append(tuple(blueprint))

    return blueprints


@lru_cache(maxsize=None)
def sub(v1: Tuple, v2: Tuple) -> Tuple:
    return tuple(map(operator.sub, v1, v2))


@lru_cache(maxsize=None)
def add(v1: Tuple, v2: Tuple) -> Tuple:
    return tuple(map(operator.add, v1, v2))


@lru_cache(maxsize=None)
def mul(v1: Tuple, v2: Tuple) -> Tuple:
    return tuple(map(operator.mul, v1, v2))


robot_diffs = [
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
]


cache = {}


@lru_cache(maxsize=None)
def maxwait(costs, elements, robots) -> int:
    wait = 0
    for cost, element, robot in zip(costs, elements, robots):
        if cost == 0:
            continue
        if robot == 0:
            return None
        wait = max(wait, math.ceil((cost - element) / robot))
    return wait


def dfs(
    elements: Tuple[int],
    robots: Tuple[int],
    blueprint: Tuple[Tuple],
    maxrobots: Tuple[int],
    time_left: int,
) -> int:
    """Perform a depth-first search to find plan that maximizes geodes."""
    if time_left == 0:
        return elements[3]

    cache_index = (elements, robots, blueprint, time_left)
    if cache_index in cache:
        return cache[cache_index]

    m = elements[3] + robots[3] * time_left

    for idx, (robot_diff, cost) in enumerate(zip(robot_diffs, blueprint)):
        if idx != 3 and robots[idx] >= maxrobots[idx]:
            continue

        wait = maxwait(cost, elements, robots)
        if wait is None or (new_time := time_left - wait - 1) <= 0:
            continue

        new_elements = add(elements, mul(robots, (wait + 1,) * 4))
        new_elements = sub(new_elements, cost)
        new_robots = add(robots, robot_diff)

        new_time = time_left - wait - 1
        m = max(m, dfs(new_elements, new_robots, blueprint, maxrobots, new_time))

    cache[cache_index] = m
    return m


def part1():
    blueprints = get_blueprints()
    elements = (0, 0, 0, 0)
    robots = (1, 0, 0, 0)
    quality_level = 0
    for idx, blueprint in enumerate(blueprints):
        maxrobots = tuple(map(max, zip(*blueprint)))
        geode = dfs(elements, robots, blueprint, maxrobots, 24)
        quality_level += (idx + 1) * geode
    print(quality_level)


def part2():
    blueprints = get_blueprints()
    elements = (0, 0, 0, 0)
    robots = (1, 0, 0, 0)
    r = 1
    for blueprint in blueprints[:3]:
        maxrobots = tuple(map(max, zip(*blueprint)))
        r *= dfs(elements, robots, blueprint, maxrobots, 32)
    print(r)


if __name__ == "__main__":
    part1()
    part2()
