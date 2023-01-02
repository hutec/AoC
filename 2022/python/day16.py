import re
from typing import List, Set
from itertools import product
from dataclasses import dataclass
from itertools import chain, combinations


@dataclass
class Valve:
    name: str
    flow_rate: int
    neighbors: List["Valve"]

    def __hash__(self) -> int:
        return hash(self.name)


def floyd_warshall(valves: List[Valve]) -> dict:
    """Build all pair shortest paths with Floyd-Warshall."""
    dist = {}
    for v1, v2 in product(valves, repeat=2):
        dist[v1, v2] = float("inf")

    for valve in valves:
        dist[valve, valve] = 0
        for neighbor in valve.neighbors:
            dist[valve, neighbor] = 1

    for v1, v2, v3 in product(valves, repeat=3):
        dist[v2, v3] = min(dist[v2, v3], dist[v2, v1] + dist[v1, v3])

    return dist


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def dfs(
    valve: Valve,
    closed_valves: Set[Valve],
    time_left: int,
) -> int:
    if (valve, closed_valves, time_left) in cache:
        return cache[valve, closed_valves, time_left]

    maxval = 0
    for next_valve in closed_valves:
        _time_left = time_left - dist[valve, next_valve] - 1
        if _time_left <= 0:
            continue

        maxval = max(
            maxval,
            next_valve.flow_rate * _time_left
            + dfs(
                next_valve,
                closed_valves - {next_valve},
                _time_left,
            ),
        )

    cache[valve, closed_valves, time_left] = maxval
    return maxval


with open("../inputs/day16", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

valves = {}
for line in lines:
    source, *neighbors = re.findall(r"[A-Z]{2}", line)
    flow_rate = int(re.findall(r"\d+", line)[0])

    source = valves.setdefault(source, Valve(source, 0, []))
    neighbors = [
        valves.setdefault(neighbor, Valve(neighbor, 0, [])) for neighbor in neighbors
    ]
    source.flow_rate = flow_rate
    source.neighbors = neighbors

dist = floyd_warshall(valves.values())

all_valves = frozenset(v for v in valves.values() if v.flow_rate != 0)
cache = {}

# Part 1
m = dfs(valves["AA"], all_valves, 30)
print(m)

# Part 2
m = 0
for valves1 in powerset(all_valves):
    valves1 = frozenset(valves1)
    valves2 = all_valves - valves1
    m = max(m, dfs(valves["AA"], valves1, 26) + dfs(valves["AA"], valves2, 26))

print(m)