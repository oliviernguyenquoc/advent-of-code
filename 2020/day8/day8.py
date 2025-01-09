import pathlib


def part1(instruction_list):
    done_list = [False] * len(instruction_list)

    i = 0
    acc = 0

    instruction_list = [tuple(instruction.split()) for instruction in instruction_list]

    while not done_list[i]:
        done_list[i] = True
        instruction, nb = instruction_list[i][0], int(instruction_list[i][1])
        if instruction == "acc":
            acc += nb
            i += 1
        elif instruction == "jmp":
            i += nb
        elif instruction == "nop":
            i += 1

    return acc


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
