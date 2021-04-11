import copy
import itertools


def run(program):
    instruction_pointer = 0
    while program[instruction_pointer] != 99:
        opcode, param1, param2, param3 = program[
            instruction_pointer : instruction_pointer + 4
        ]
        if opcode == 1:
            program[param3] = program[param1] + program[param2]
        elif opcode == 2:
            program[param3] = program[param1] * program[param2]
        instruction_pointer += 4

    return program


examples = [
    ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
]

for program, expected in examples:
    assert run(program) == expected

with open("input", "r") as f:
    program = list(map(int, f.read().split(",")))


def run_with_noun_and_verb(program, noun, verb):
    program = copy.copy(program)
    program[1] = noun
    program[2] = verb
    return run(program)[0]


print(run_with_noun_and_verb(program, 12, 2))

for noun, verb in itertools.product(range(99), range(99)):
    if run_with_noun_and_verb(program, noun, verb) == 19690720:
        print(100 * noun + verb)
