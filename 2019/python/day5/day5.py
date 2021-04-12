def add(memory, instruction_ptr, modes):
    modes = modes.zfill(3)
    addr1, addr2, target_addr = memory[instruction_ptr + 1 : instruction_ptr + 4]
    val1 = addr1 if modes[-1] == "1" else memory[addr1]
    val2 = addr2 if modes[-2] == "1" else memory[addr2]
    memory[target_addr] = val1 + val2

    return instruction_ptr + 4


def multiply(memory, instruction_ptr, modes):
    modes = modes.zfill(3)
    addr1, addr2, target_addr = memory[instruction_ptr + 1 : instruction_ptr + 4]
    val1 = addr1 if modes[-1] == "1" else memory[addr1]
    val2 = addr2 if modes[-2] == "1" else memory[addr2]
    memory[target_addr] = val1 * val2

    return instruction_ptr + 4


def write(memory, instruction_ptr, modes):
    target_addr = memory[instruction_ptr + 1]
    memory[target_addr] = int(input("User input: "))

    return instruction_ptr + 2


def output(memory, instruction_ptr, modes):
    modes = modes.zfill(1)
    addr1 = memory[instruction_ptr + 1]
    val1 = memory[addr1] if modes[-1] == "0" else addr1
    print(f"Output: {val1}")

    return instruction_ptr + 2


def jump_if_true(memory, instruction_ptr, modes):
    modes = modes.zfill(2)
    addr1, addr2 = memory[instruction_ptr + 1 : instruction_ptr + 3]
    val1 = addr1 if modes[-1] == "1" else memory[addr1]
    val2 = addr2 if modes[-2] == "1" else memory[addr2]

    if val1 != 0:
        return val2

    return instruction_ptr + 3


def jump_if_false(memory, instruction_ptr, modes):
    modes = modes.zfill(2)
    addr1, addr2 = memory[instruction_ptr + 1 : instruction_ptr + 3]
    val1 = addr1 if modes[-1] == "1" else memory[addr1]
    val2 = addr2 if modes[-2] == "1" else memory[addr2]

    if val1 == 0:
        return val2

    return instruction_ptr + 3


def less_than(memory, instruction_ptr, modes):
    modes = modes.zfill(3)
    addr1, addr2, target_addr = memory[instruction_ptr + 1 : instruction_ptr + 4]
    val1 = addr1 if modes[-1] == "1" else memory[addr1]
    val2 = addr2 if modes[-2] == "1" else memory[addr2]

    memory[target_addr] = int(val1 < val2)
    return instruction_ptr + 4


def equals(memory, instruction_ptr, modes):
    modes = modes.zfill(3)
    addr1, addr2, target_addr = memory[instruction_ptr + 1 : instruction_ptr + 4]
    val1 = addr1 if modes[-1] == "1" else memory[addr1]
    val2 = addr2 if modes[-2] == "1" else memory[addr2]

    memory[target_addr] = int(val1 == val2)
    return instruction_ptr + 4


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
    opcode = instruction[-2:]
    modes = instruction[:-2]
    return int(opcode), modes


def run(memory):
    instruction_ptr = 0

    while True:
        opcode, modes = parse_instruction(memory[instruction_ptr])
        if opcode == 99:
            break
        instruction_ptr = instructions[opcode](memory, instruction_ptr, modes)

    return memory


with open("input", "r") as f:
    program = list(map(int, f.read().split(",")))

run(program)
