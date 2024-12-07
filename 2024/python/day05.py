from functools import reduce

with open("../inputs/05", "r") as f:
    rules, updates = f.read().split("\n\n")

rules = [list(map(int, rule.split("|"))) for rule in rules.splitlines()]
updates = [list(map(int, update.split(","))) for update in updates.splitlines()]


def is_satisfied(rule: list[int], update: list[int]) -> bool:
    """Check if the rule is satisfied by the update

    Args:
        rule: The rule to check against in form x before y.
        update: The list of numbers to check.
    """
    x, y = rule
    if x not in update or y not in update:
        return True
    return update.index(x) < update.index(y)


def reorder(update: list[int], rule: list[int]) -> list[int]:
    """Reorder the update list to satisfy the rule

    Args:
        rule: The rule to check against in form x before y.
        update: The list of numbers to check.
    """
    x, y = rule
    if is_satisfied(rule, update):
        return update

    x_idx, y_idx = update.index(x), update.index(y)
    update[x_idx], update[y_idx] = update[y_idx], update[x_idx]
    return update


total_correct_updates = 0
total_incorrect_updates = 0

for update in updates:
    if all(is_satisfied(rule, update) for rule in rules):
        total_correct_updates += update[len(update) // 2]
    else:
        # Apply the rules until the update is converged
        while True:
            fixed_update = reduce(reorder, rules, update.copy())
            if fixed_update == update:
                break
            update = fixed_update

        total_incorrect_updates += fixed_update[len(fixed_update) // 2]

print(total_correct_updates)
print(total_incorrect_updates)
