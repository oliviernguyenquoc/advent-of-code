import re
import pathlib


def parse_data(instruction_list):
    eq = []
    for instruction in instruction_list:
        res, nbs = re.search(r"(\d*): (.*)", instruction).groups()
        eq.append((int(res), [int(nb) for nb in nbs.split(" ")]))

    return eq


def get_combinations(nb_list: list[int]) -> list[int]:
    if len(nb_list) == 1:
        return [nb_list[0]]

    res = [nb_list[-1] + nb for nb in get_combinations(nb_list[:-1])] + [
        nb_list[-1] * nb for nb in get_combinations(nb_list[:-1])
    ]

    return res


def get_combinations_part2(nb_list: list[int]) -> list[int]:
    if len(nb_list) == 1:
        return [nb_list[0]]

    res = (
        [nb_list[-1] + nb for nb in get_combinations_part2(nb_list[:-1])]
        + [nb_list[-1] * nb for nb in get_combinations_part2(nb_list[:-1])]
        + [
            int(str(nb) + str(nb_list[-1]))
            for nb in get_combinations_part2(nb_list[:-1])
        ]
    )

    return res


def part1(instruction_list):
    eq = parse_data(instruction_list)

    total_calibration = 0
    for res, nbs in eq:
        comb = get_combinations(nbs)
        if res in comb:
            total_calibration += res

    print(f"Part 1: {total_calibration}")
    return total_calibration


def part2(instruction_list):
    eq = parse_data(instruction_list)

    total_calibration = 0
    for res, nbs in eq:
        comb = get_combinations_part2(nbs)
        if res in comb:
            total_calibration += res

    return total_calibration


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(part1(instruction_list))
    print(part2(instruction_list))
