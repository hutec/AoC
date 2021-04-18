import itertools


class Computer:
    """An IntCode computer."""

    def __init__(self, program, inputs=None):
        self.memory = program.copy()
        self.ptr = 0
        self.relative_base = 0
        self.inputs = inputs
        self.output = None
        self.finished = False

        # Mapping opcodes to functions
        self.instructions = {
            1: self.add_op,
            2: self.multiply_op,
            3: self.write_op,
            4: self.output_op,
            5: self.jump_if_true_op,
            6: self.jump_if_false_op,
            7: self.less_than_op,
            8: self.equals_op,
        }

    def __getitem__(self, key):
        addr, mode = key
        # For simplicity the address is passed relativ to self.ptr
        addr = self.ptr + addr

        if mode == "0":  # position mode
            return self.memory[self.memory[addr]]
        elif mode == "1":  # immediate mode
            return self.memory[addr]
        elif mode == "2":  # relative mode
            return self.memory[self.relative_base + self.memory[addr]]
        else:
            raise ValueError(f"Unkown parameter mode {mode}")

    def __setitem__(self, key, value):
        addr, mode = key
        addr = self.ptr + addr

        if mode == "0":  # position mode
            self.memory[self.memory[addr]] = value
        elif mode == "1":  # immediate mode
            raise ValueError("Writing parameters shouldn't be in immediate mode")
        elif mode == "2":  # relative mode
            self.memory[self.relative_base + self.memory[addr]] = value
        else:
            raise ValueError(f"Unkown parameter mode {mode}")

    def run(self):
        while True:
            opcode, modes = self.get_instruction()
            if opcode == 99:
                self.finished = True
                return self.output
            try:
                self.instructions[opcode](modes)
            except StopIteration:
                return self.output

    def get_instruction(self):
        """Parses instruction and mode at current intstruction pointer."""
        instruction = str(self.memory[self.ptr])
        opcode = int(instruction[-2:])
        # Assuming that 3 parameters are maximum
        modes = instruction[:-2].zfill(3)[::-1]
        return opcode, modes

    def add_op(self, modes):
        self[(3, modes[2])] = self[(1, modes[0])] + self[(2, modes[1])]
        self.ptr += 4

    def multiply_op(self, modes):
        self[(3, modes[2])] = self[(1, modes[0])] * self[(2, modes[1])]
        self.ptr += 4

    def write_op(self, modes):
        _input = next(self.inputs)
        self[(1, modes[0])] = _input
        self.ptr += 2

    def output_op(self, modes):
        self.output = self[(1, modes[0])]
        self.ptr += 2

    def jump_if_true_op(self, modes):
        if self[(1, modes[0])] != 0:
            self.ptr = self[(2, modes[1])]
        else:
            self.ptr += 3

    def jump_if_false_op(self, modes):
        if self[(1, modes[0])] == 0:
            self.ptr = self[(2, modes[1])]
        else:
            self.ptr += 3

    def less_than_op(self, modes):
        self[(3, modes[2])] = int(self[(1, modes[0])] < self[(2, modes[1])])
        self.ptr += 4

    def equals_op(self, modes):
        self[(3, modes[2])] = int(self[(1, modes[0])] == self[(2, modes[1])])
        self.ptr += 4


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
