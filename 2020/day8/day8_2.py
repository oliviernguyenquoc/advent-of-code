import pathlib


def test_algo(instruction_list):
    done_list = [False] * len(instruction_list)
    i = 0
    acc = 0

    while not done_list[i] and i != len(instruction_list) - 1:
        done_list[i] = True
        instruction, nb = instruction_list[i][0], int(instruction_list[i][1])
        if instruction == "acc":
            acc += nb
            i += 1
        elif instruction == "jmp":
            i += nb
        elif instruction == "nop":
            i += 1

    return i == len(instruction_list) - 1, acc


def part2(instruction_list):
    instruction_list = [tuple(instruction.split()) for instruction in instruction_list]

    right_algo, acc = test_algo(instruction_list)
    if right_algo:
        print("NO CHANGE:")
        print(acc)

    for index, instruction in enumerate(instruction_list):
        tmp_instruction_list = instruction_list.copy()
        instruction, nb = instruction_list[index][0], int(instruction_list[index][1])
        if instruction == "jmp" and nb != 0:
            tmp_instruction_list[index] = ("nop", nb)
        elif instruction == "nop" and nb != 0:
            tmp_instruction_list[index] = ("jmp", nb)

        right_algo, acc = test_algo(tmp_instruction_list)

        if right_algo:
            print(f"Test {index}: WORKING")
            print(acc)
            break
        if not right_algo:
            print(f"Test {index}: not working")

    return acc


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 2: {part2(instruction_list)}")
