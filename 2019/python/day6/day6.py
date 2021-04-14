from dataclasses import dataclass, field
from operator import eq


@dataclass
class SpaceObject:
    """An object orbitting around ``self.center``."""

    name: str
    centers: list = field(default_factory=list)

    def trace(self):
        """Trace orbits back to COM."""
        if not self.centers:
            return []
        else:
            route = [self.name]
            for center in self.centers:
                route.extend(center.trace())
            return route


all_space_objects = {}

with open("input", "r") as f:
    orbit_maps = f.read().split("\n")

for orbit_map in orbit_maps:
    center_name, orbiter_name = orbit_map.split(")")

    center = all_space_objects.get(center_name, SpaceObject(center_name))
    orbiter = all_space_objects.get(orbiter_name, SpaceObject(orbiter_name))
    orbiter.centers.append(center)
    all_space_objects.update({center_name: center, orbiter_name: orbiter})

print(sum([len(o.trace()) for o in all_space_objects.values()]))

santa_transfers = all_space_objects["SAN"].trace()[::-1]
my_transfers = all_space_objects["YOU"].trace()[::-1]

# Find index of divergence
idx = list(map(eq, santa_transfers, my_transfers)).index(False)
print(len(santa_transfers) - idx + len(my_transfers) - idx - 2)
