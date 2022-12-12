from typing import Tuple, List
import heapq


def elevation(x: str) -> int:
    if x == "S":
        return ord("a") - 1
    elif x == "E":
        return ord("z") + 1
    else:
        return ord(x)


def get_neighbors(grid: List[List[int]], pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    neighbors = []
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        y, x = pos
        yy, xx = y + dy, x + dx
        if 0 <= yy < len(grid) and 0 <= xx < len(grid[0]):
            if grid[yy][xx] - grid[y][x] <= 1:
                neighbors.append((yy, xx))
    return neighbors


def find_location(grid: List[List[int]], target: int) -> Tuple[int, int]:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == target:
                return (y, x)


with open("../inputs/day12", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

grid = [list(map(elevation, line)) for line in lines]


def dijsktra(grid):
    source = find_location(grid, ord("a") - 1)
    target = find_location(grid, ord("z") + 1)
    frontier = []
    heapq.heappush(frontier, (0, source))
    came_from = {source: None}
    cost_so_far = {source: 0}

    while len(frontier) != 0:
        _, current = heapq.heappop(frontier)
        if current == target:
            print(cost_so_far[target])
            break

        for neighbor in get_neighbors(grid, current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor))
                came_from[neighbor] = current

    return came_from, cost_so_far


dijsktra(grid)
