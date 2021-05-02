from dataclasses import dataclass


@dataclass
class Reaction:
    in_chemicals: dict
    out_chemicals: dict

    def produces(self, chemical: str) -> bool:
        return chemical in self.out_chemicals


class RequiredChemicals(dict):
    """Mapping chemicals to required quantities."""

    def update(self, reaction: Reaction, times: int):
        for k, v in reaction.in_chemicals.items():
            self[k] = self.get(k, 0) + times * v

        for k, v in reaction.out_chemicals.items():
            if k in self:
                self[k] -= times * v
                if self[k] == 0:
                    del self[k]

    def only_ore(self) -> bool:
        """Check if only ORE is left required."""
        return sum(map(lambda x: x > 0, self.values())) == 1 and "ORE" in self


with open("input", "r") as f:
    inputs = f.read().split("\n")


def parse_chemicals(chemicals_str: str) -> dict:
    chemicals = {}
    for chemical in chemicals_str.split(","):
        qty, name = chemical.strip().split(" ")
        chemicals[name] = int(qty)
    return chemicals


reactions = []
for reaction in inputs:
    in_chemicals, out_chemicals = reaction.split("=>")
    reactions.append(
        Reaction(parse_chemicals(in_chemicals), parse_chemicals(out_chemicals))
    )


def find_ore(required: RequiredChemicals):
    while not required.only_ore():
        # Next chemical to produce, skip "ORE" and negative quantitites
        chemical, qty = next(
            filter(lambda x: x[0] != "ORE" and x[1] > 0, required.items())
        )
        # reaction that produces chemical
        reaction = next(filter(lambda r: r.produces(chemical), reactions))

        # how often does this reaction happen
        times = max(1, qty // reaction.out_chemicals[chemical])
        required.update(reaction, times)

    return required["ORE"]


required = RequiredChemicals({"FUEL": 1})
ore_per_fuel = find_ore(required)
print(ore_per_fuel)

# TODO: Binary search for part two
