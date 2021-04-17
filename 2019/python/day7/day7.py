import itertools


def add(memory, instruction_ptr, modes):
    *args, target_addr = memory[instruction_ptr + 1 : instruction_ptr + 4]
    val1, val2 = read_with_modes(*args, memory=memory, modes=modes)
    memory[target_addr] = val1 + val2

    return instruction_ptr + 4


def multiply(memory, instruction_ptr, modes):
    *args, target_addr = memory[instruction_ptr + 1 : instruction_ptr + 4]
    val1, val2 = read_with_modes(*args, memory=memory, modes=modes)
    memory[target_addr] = val1 * val2

    return instruction_ptr + 4


def write(memory, instruction_ptr, modes, external_input=None):
    target_addr = memory[instruction_ptr + 1]
    if external_input is not None:
        memory[target_addr] = external_input
    else:
        memory[target_addr] = int(input("User input: "))

    return instruction_ptr + 2


def output(memory, instruction_ptr, modes):
    args = memory[instruction_ptr + 1 : instruction_ptr + 2]
    (val1,) = read_with_modes(*args, memory=memory, modes=modes)
    return instruction_ptr + 2, val1


def jump_if_true(memory, instruction_ptr, modes):
    args = memory[instruction_ptr + 1 : instruction_ptr + 3]
    val1, val2 = read_with_modes(*args, memory=memory, modes=modes)

    if val1 != 0:
        return val2

    return instruction_ptr + 3


def jump_if_false(memory, instruction_ptr, modes):
    args = memory[instruction_ptr + 1 : instruction_ptr + 3]
    val1, val2 = read_with_modes(*args, memory=memory, modes=modes)

    if val1 == 0:
        return val2

    return instruction_ptr + 3


def less_than(memory, instruction_ptr, modes):
    *args, target_addr = memory[instruction_ptr + 1 : instruction_ptr + 4]
    val1, val2 = read_with_modes(*args, memory=memory, modes=modes)

    memory[target_addr] = int(val1 < val2)
    return instruction_ptr + 4


def equals(memory, instruction_ptr, modes):
    *args, target_addr = memory[instruction_ptr + 1 : instruction_ptr + 4]
    val1, val2 = read_with_modes(*args, memory=memory, modes=modes)
    memory[target_addr] = int(val1 == val2)
    return instruction_ptr + 4


def read_with_modes(*args, memory, modes):
    return [memory[v] if m == "0" else v for v, m in zip(args, modes[::-1])]


class Computer:
    """An IntCode computer."""

    def __init__(self, program, inputs=None):
        self.memory = program.copy()
        self.inputs = inputs
        self.instruction_ptr = 0
        self.output = None
        self.finished = False

    def run(
        self,
    ):
        while True:
            opcode, modes = parse_instruction(self.memory[self.instruction_ptr])
            if opcode == 99:
                self.finished = True
                return self.output
            elif opcode == 3:
                # If there are no inputs left, pause the computer
                try:
                    self.instruction_ptr = write(
                        self.memory,
                        self.instruction_ptr,
                        modes,
                        external_input=next(self.inputs),
                    )
                except StopIteration:
                    return self.output

            elif opcode == 4:
                self.instruction_ptr, self.output = output(
                    self.memory, self.instruction_ptr, modes
                )
            else:
                self.instruction_ptr = instructions[opcode](
                    self.memory, self.instruction_ptr, modes
                )


# Mapping opcodes to functions
instructions = {
    1: add,
    2: multiply,
    3: write,
    4: output,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals,
}


def parse_instruction(instruction):
    instruction = str(instruction)
    opcode = int(instruction[-2:])
    # Assuming that 3 parameters are maximum
    modes = instruction[:-2].zfill(3)
    return opcode, modes


with open("input", "r") as f:
    program = list(map(int, f.read().split(",")))

max_output = 0
for phase_order in itertools.permutations(range(5)):
    amplifier_input = 0
    for phase in phase_order:
        amplifier_input = Computer(program, inputs=iter([phase, amplifier_input])).run()
    if amplifier_input > max_output:
        max_output = amplifier_input
        max_order = phase_order

print(max_output)


max_output = 0
for phase_order in itertools.permutations(range(5, 10)):
    amplifier_input = 0
    amps = [Computer(program) for _ in range(5)]
    # First round with phase order
    for amp, phase in zip(amps, phase_order):
        amp.inputs = iter([phase, amplifier_input])
        amplifier_input = amp.run()

    # Only the amplifier inputs
    for amp in itertools.cycle(amps):
        amp.inputs = iter([amplifier_input])
        amplifier_input = amp.run()
        if all(map(lambda x: x.finished, amps)):
            break
    if amplifier_input > max_output:
        max_output = amplifier_input

print(max_output)
