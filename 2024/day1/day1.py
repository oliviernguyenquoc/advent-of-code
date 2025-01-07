from collections import defaultdict
import pathlib


def parse_data(instruction_list):
    list1, list2 = [], []
    for instruction in instruction_list:
        nb1, nb2 = instruction.split()
        list1.append(int(nb1))
        list2.append(int(nb2))

    list1.sort()
    list2.sort()

    return list1, list2


def part1(instruction_list):
    list1, list2 = parse_data(instruction_list)

    distance = 0
    for nb1, nb2 in zip(list1, list2):
        distance += max(nb1, nb2) - min(nb1, nb2)

    return distance


def part2(instruction_list):
    list1, list2 = parse_data(instruction_list)

    nb_freq_dict: dict[int, int] = defaultdict(int)
    for i in list2:
        nb_freq_dict[i] += 1

    total = 0
    for i in list1:
        total += nb_freq_dict[i] * i

    return total


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
