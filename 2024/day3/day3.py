import re
import pathlib


def solve(instruction_list, part=1):
    mult_list: list[tuple[str, str]] = []

    enable = True

    for instruction in instruction_list:
        i = 0
        while i < len(instruction):
            mult = []
            if instruction[i : i + 4] == "do()":
                enable = True
            elif instruction[i : i + 7] == "don't()":
                enable = False
            elif instruction[i : i + 4] == "mul(":
                mult = re.search(
                    r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", instruction[i : i + 12]
                )

            if mult:
                mult = mult.groups()
                mult_list.append((int(mult[0]), int(mult[1]), enable))

            i += 1

    total_part1, total_part2 = 0, 0
    for mul in mult_list:
        total_part1 += mul[0] * mul[1]
        if mul[2]:
            total_part2 += mul[0] * mul[1]

    if part == 1:
        print(f"Part 1: {total_part1}")
        return total_part1
    else:
        print(f"Part 2: {total_part2}")
        return total_part2


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    solve(instruction_list, part=1)
    solve(instruction_list, part=2)
