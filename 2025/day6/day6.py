import pathlib
import math


def _to_int_list(inst):
    return [int(nb_str) for nb_str in inst.strip().split(" ") if nb_str != ""]


def _to_str_list(inst):
    return [nb_str for nb_str in inst.strip().split(" ") if nb_str != ""]


def part1(instruction_list) -> int:
    nb_list = []

    inst = instruction_list.pop(0)
    while inst[0] not in ["+", "*"]:
        nb_list.append(_to_int_list(inst))
        inst = instruction_list.pop(0)

    operations = _to_str_list(inst)

    total = 0
    for i, op in enumerate(operations):
        match op:
            case "*":
                total += math.prod([nb[i] for nb in nb_list])

            case "+":
                total += sum([nb[i] for nb in nb_list])
    return total


def part2(instruction_list) -> int:
    MAX_X, MAX_Y = len(instruction_list[0]), len(instruction_list)

    nb_list = []
    tmp_list = []
    for x in range(MAX_X):
        res_str = ""
        for y in range(MAX_Y - 1):
            if instruction_list[y][x] != "":
                res_str += instruction_list[y][x].strip()
        if res_str == "":
            nb_list.append(tmp_list)
            tmp_list = []
        else:
            tmp_list.append(int(res_str))

    nb_list.append(tmp_list)
    operations = _to_str_list(instruction_list[MAX_Y - 1])

    total = 0
    for i, op in enumerate(operations):
        match op:
            case "*":
                total += math.prod(nb_list[i])

            case "+":
                total += sum(nb_list[i])
    return total


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list.copy())}")
    print(f"Part 2: {part2(instruction_list)}")
