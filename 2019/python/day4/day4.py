from collections import Counter


def check(val):
    """Checks if ``val`` meets password criterias."""
    val = str(val)
    valid = False
    for i in range(len(val) - 1):
        if val[i] > val[i + 1]:  # non-decreasing
            return False

        if val[i] == val[i + 1]:
            valid = True
    return valid


def check2(val):
    """Checks if ``val`` meets new password criterias."""
    val = str(val)
    if not "".join(sorted(val)) == val:
        return False

    return 2 in Counter(val).values()


assert check(111111) == True
assert check(223450) == False
assert check(123789) == False

assert check2(112233) == True
assert check2(123444) == False
assert check2(111122) == True

print(len(list(filter(check, range(108457, 562042)))))
print(len(list(filter(check2, range(108457, 562042)))))
