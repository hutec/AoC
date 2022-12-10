from collections import defaultdict

with open("../inputs/day10", "r") as f:
    seq = f.read()
    lines = seq.split("\n")


register = [1]
for instruction in lines:
    if instruction == "noop":
        last_value = register[-1]
        register.append(last_value)
    elif instruction.startswith("addx"):
        x = int(instruction.split(" ")[1])
        last_value = register[-1]
        register.extend([last_value, last_value + x])

print(sum([register[r - 1] * r for r in range(20, 221, 40)]))

for row in range(6):
    screen = ""
    for col in range(40):
        cycle = row * 40 + col
        sprite_position = register[cycle]
        if sprite_position - 1 <= col <= sprite_position + 1:
            screen += "##"
        else:
            screen += "  "
    print(screen)
