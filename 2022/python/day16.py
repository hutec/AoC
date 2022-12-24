import re
from typing import List, Set
from itertools import product
from dataclasses import dataclass

with open("../inputs/day16", "r") as f:
    seq = f.read()
    lines = seq.split("\n")


@dataclass
class Valve:
    name: str
    flow_rate: int
    neighbors: List["Valve"]

    def __hash__(self) -> int:
        return hash(self.name)


def get_or_create(name: str, valves: dict) -> Valve:
    if name in valves:
        return valves[name]
    else:
        valve = Valve(name, 0, [])
        valves[name] = valve
        return valve


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
        dist[v1, v3] = min(dist[v1, v3], dist[v1, v2] + dist[v2, v3])

    return dist


cache = {}


def dfs(
    valve: Valve,
    dist: dict,
    closed_valves: Set[Valve],
    flow: int,
    time_left: int,
) -> int:
    if time_left <= 0:
        return flow

    if (valve, closed_valves, flow, time_left) in cache:
        return cache[valve, closed_valves, flow, time_left]

    options = [flow * time_left]
    for next_valve in closed_valves:
        if next_valve.flow_rate == 0:
            continue

        if dist[valve, next_valve] < time_left - 1:
            options.append(
                flow * (dist[valve, next_valve] + 1)
                + dfs(
                    next_valve,
                    dist,
                    closed_valves - {next_valve},
                    flow + next_valve.flow_rate,
                    time_left - dist[valve, next_valve] - 1,
                )
            )

    cache[valve, closed_valves, flow, time_left] = max(options)
    return max(options)


def main():
    valves = {}
    for line in lines:
        source, *neighbors = re.findall(r"[A-Z]{2}", line)
        flow_rate = int(re.findall(r"\d+", line)[0])

        source = get_or_create(source, valves)
        neighbors = [get_or_create(neighbor, valves) for neighbor in neighbors]
        source.flow_rate = flow_rate
        source.neighbors = neighbors

    dist = floyd_warshall(valves.values())
    m = dfs(
        valves["AA"],
        dist,
        frozenset(valves.values()),
        0,
        30,
    )
    print(m)


if __name__ == "__main__":
    main()