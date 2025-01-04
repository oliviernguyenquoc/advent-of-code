import re
import pathlib

# Register A: 0
# Register B: 2024
# Register C: 43690

# Program: 4,0


def parse_data(instruction_list):
    a = re.search(r"Register A: (\d+)", instruction_list[0].strip()).groups()[0]
    b = re.search(r"Register B: (\d+)", instruction_list[1].strip()).groups()[0]
    c = re.search(r"Register C: (\d+)", instruction_list[2].strip()).groups()[0]
    program_str = re.search(
        r"Program: ([0-9,]+)", instruction_list[4].strip()
    ).groups()[0]

    program = [int(p) for p in program_str.split(",")]
    a, b, c = int(a), int(b), int(c)

    return program, a, b, c


def run_program(
    program: list[int], a: int, b: int, c: int
) -> tuple[list[int], int, int, int]:
    output = []
    i = 0
    while i < len(program):
        instruction_opcode, operand = program[i], program[i + 1]

        if instruction_opcode not in (1, 3):
            match operand:
                case 4:
                    operand = a
                case 5:
                    operand = b
                case 6:
                    operand = c
                case 7:
                    raise Exception("Not valid")

        match instruction_opcode:
            case 0:
                a = a // (2**operand)
            case 1:
                b = b ^ operand
            case 2:
                b = operand % 8
            case 3:
                if a != 0:
                    i = operand
            case 4:
                b = b ^ c
            case 5:
                output.append(operand % 8)
            case 6:
                b = a // (2**operand)
            case 7:
                c = a // (2**operand)
        if not (instruction_opcode == 3 and a != 0):
            i += 2

    return output


def part1(instruction_list):
    program, a, b, c = parse_data(instruction_list)
    output = run_program(program, a, b, c)

    print(f"Program: {program}")
    print(f"Part 1: {",".join(map(str, output))}")

    return ",".join(map(str, output))


def part2(instruction_list):
    program, a, b, c = parse_data(instruction_list)

    # Just shift to 3 digits (binary)
    A = 0
    for i in reversed(range(len(program))):
        print(i, A, program[i:])
        A <<= 3
        while run_program(program, A, 0, 0) != program[i:]:
            A += 1

    print(f"Program: {program}")
    print(f"Part 2: {A}")
    return A


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    part1(instruction_list)
    part2(instruction_list)
