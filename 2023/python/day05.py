from typing import Optional
from dataclasses import dataclass, field


with open("../inputs/05", "r") as f:
    seq = f.read()
    blocks = seq.split("\n\n")


@dataclass
class Range:
    target: int
    source: int
    length: int

    def source_contains(self, x: int) -> bool:
        return self.source <= x <= self.source + self.length

    def target_contains(self, x: int) -> bool:
        return self.target <= x <= self.target + self.length

    def transform(self, x: int) -> int:
        if not self.source_contains(x):
            raise ValueError("Can only transform values in range.")

        return self.target + (x - self.source)

    @property
    def source_end(self) -> int:
        return self.source + self.length

    @property
    def target_end(self) -> int:
        return self.target + self.length


@dataclass
class Map:
    name: str
    ranges: list[Range]
    cache: dict[int, int] = field(default_factory=dict)

    @classmethod
    def from_str(cls, block):
        name, rest = block.split(":\n")
        ranges = [
            Range(*[int(x) for x in line.split(" ")]) for line in rest.split("\n")
        ]
        return cls(name, ranges)

    def transform(self, x):
        if x in self.cache:
            return self.cache[x]

        for range in self.ranges:
            if range.source_contains(x):
                r = range.transform(x)
                self.cache[x] = r
                return r

        self.cache[x] = x
        return x


seeds = list(map(int, blocks[0].split(":")[1].strip().split(" ")))
maps = [Map.from_str(block) for block in blocks[1:]]


r = []
for seed in seeds:
    for map in maps:
        seed = map.transform(seed)
    r.append(seed)

print(min(r))
