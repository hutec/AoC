from collections import defaultdict

with open("../inputs/day01", "r") as f:
    seq = f.read()
    lines = seq.split("\n")

calories_per_elf = defaultdict(int)
elf = 0
for line in lines:
    if line == "":
        elf += 1
    else:
        calories_per_elf[elf] += int(line)

max_elf = max(calories_per_elf, key=calories_per_elf.get)
print(f"Elf {max_elf} carries the most calories: {calories_per_elf[max_elf]}.")

sorted_calories = sorted(calories_per_elf.values())
sum_max_3_calories = sum(sorted_calories[-3:])
print(f"The top three elves carry {sum_max_3_calories} calories.")
