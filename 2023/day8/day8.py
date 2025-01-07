import re


def part1(instructions):
    commands = instructions.pop(0).rstrip()
    instructions.pop(0)

    map_dict = {}
    for instruction in instructions:
        root, left, right = re.search(
            r"([A-Z]*) = \(([A-Z]*), ([A-Z]*)\)", instruction
        ).groups()
        map_dict[root + " L"] = left
        map_dict[root + " R"] = right

    point = "AAA"
    i = 0
    while point != "ZZZ":
        left_or_right = commands[i % len(commands)]
        point = map_dict[point + " " + left_or_right]
        i += 1

    # nb_iter = i // len(commands)
    return i


if __name__ == "__main__":
    with open("./day8/test_input_part2.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()
    print(f"Part 1: {part1(instruction_list)}")
