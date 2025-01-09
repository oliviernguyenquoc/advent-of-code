import re
import pathlib


def parse_data(instructions):
    instersect_list: list[set[int]] = []

    for instruction in instructions:
        idx, winning_str, own_str = re.search(
            r"Card *([0-9]*): ([0-9 ]*) \| ([0-9 ]*)", instruction
        ).groups()
        winning_nbr = set(int(nb) for nb in winning_str.split(" ") if nb != "")
        own_nbr = set(int(nb) for nb in own_str.split(" ") if nb != "")

        instersect_list.append(winning_nbr.intersection(own_nbr))

    return instersect_list


def part1(instructions):
    instersect_list = parse_data(instructions)

    part1 = sum(
        [2 ** (len(nb_list) - 1) for nb_list in instersect_list if len(nb_list) != 0]
    )
    return part1


def part2(instructions):
    instersect_list = parse_data(instructions)

    total_list: list[int] = [1] * len(instersect_list)
    total_list += [0] * len(instersect_list)

    for i, inter in enumerate(instersect_list):
        nb_win = len(inter)
        for j in range(1, nb_win + 1):
            total_list[i + j] += total_list[i]

    return sum(total_list)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
