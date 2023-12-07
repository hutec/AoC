from dataclasses import dataclass

with open("../inputs/05", "r") as f:
    seq = f.read()
    blocks = seq.split("\n\n")


@dataclass(frozen=True)
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
    def offset(self) -> int:
        return self.target - self.source

    @property
    def source_end(self) -> int:
        return self.source + self.length

    @property
    def target_end(self) -> int:
        return self.target + self.length

    def __repr__(self) -> str:
        return (
            f"[{self.source}, {self.source_end}] -> [{self.target}, {self.target_end}]"
        )


@dataclass
class Map:
    name: str
    ranges: list[Range]

    @classmethod
    def from_str(cls, block):
        name, rest = block.split(":\n")
        ranges = [
            Range(*[int(x) for x in line.split(" ")]) for line in rest.split("\n")
        ]
        return cls(name, ranges)

    def transform(self, x):
        for range in self.ranges:
            if range.source_contains(x):
                return range.transform(x)
        return x


seeds = list(map(int, blocks[0].split(":")[1].strip().split(" ")))
maps = [Map.from_str(block) for block in blocks[1:]]


r = []
for seed in seeds:
    for map in maps:
        seed = map.transform(seed)
    r.append(seed)

print(min(r))


def c(r1: Range, r2: Range):
    """Cut range 1 with range 2."""
    result = []

    # Case 1: No overlap
    if (
        not r1.target_contains(r2.source)
        and not r1.target_contains(r2.source + r2.length)
        and not r2.source_contains(r1.target)
        and not r2.source_contains(r1.target + r1.length)
    ):
        return ([], [])

    # Case 2: Overlap in the end
    if r1.target_contains(r2.source) and not r1.target_contains(r2.source + r2.length):
        offset = r2.source - r1.target
        keep = [Range(r1.target, r1.source, offset)]
        new = [
            Range(
                r2.target,
                r1.source + offset,
                r1.length - offset,
            )
        ]
        return keep, new

    # Case 3: Overlap in the beginning
    if not r1.target_contains(r2.source) and r1.target_contains(r2.source + r2.length):
        offset = (r2.source + r2.length) - r1.target
        new = [Range(r2.target + (r2.length - offset), r1.source, offset)]
        keep = [Range(r1.target + offset, r1.source + offset, r1.length - offset)]
        return keep, new

    # Case 4: r1 fully contains r2
    if r1.target_contains(r2.source) and r1.target_contains(r2.source + r2.length):
        offset = r2.source - r1.target

        keep = [
            Range(r1.target, r1.source, offset),
            Range(
                r1.target + r2.length + offset,
                r1.source + r2.length + offset,
                r1.length - offset - r2.length,
            ),
        ]
        new = [Range(r2.target, r1.source + offset, r2.length)]

        return keep, new

    # Case 5: r2 fully contains r1
    if r2.source_contains(r1.target) and r2.source_contains(r1.target + r1.length):
        offset = r1.target - r2.source
        return [], [Range(r2.target + offset, r1.target, r1.length)]


seeds = {Range(s, s, l) for s, l in zip(seeds[::2], seeds[1::2])}

for map in maps:
    next = set()
    while len(seeds) > 0:
        seed = seeds.pop()
        for range in map.ranges:
            keep, new = c(seed, range)
            if keep or new:
                if len(keep) == 1 and keep[0] == seed:
                    continue
                seeds = seeds.union(keep)
                next = next.union(new)
                break
        else:
            # No matches
            next.add(seed)

    seeds = {r for r in next if r.length > 0}

print(min(r.target for r in seeds if r.length > 0))
