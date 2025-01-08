from collections import defaultdict
import itertools
import pathlib


def parse_data(instruction_list):
    antenna_freq_dict = defaultdict(list)

    for y, instruction in enumerate(instruction_list):
        for x, letter in enumerate(instruction.strip()):
            if letter.isalnum():
                antenna_freq_dict[letter].append((x, y))

    return antenna_freq_dict


def part1(instruction_list):
    antenna_freq_dict = parse_data(instruction_list)

    antinodes = set()

    y_len = len(instruction_list)
    x_len = len(instruction_list[0].strip())

    for antenna_frequency, antenna_list in antenna_freq_dict.items():
        for (x1, y1), (x2, y2) in itertools.combinations(antenna_list, 2):
            if (0 <= 2 * x2 - x1 < x_len) and (0 <= 2 * y2 - y1 < y_len):
                antinodes.add((2 * x2 - x1, 2 * y2 - y1))
            if (0 <= 2 * x1 - x2 < x_len) and (0 <= 2 * y1 - y2 < y_len):
                antinodes.add((2 * x1 - x2, 2 * y1 - y2))

    return len(antinodes)


def part2(instruction_list):
    antenna_freq_dict = parse_data(instruction_list)

    y_len = len(instruction_list)
    x_len = len(instruction_list[0].strip())

    antinodes_part2 = set()
    for antenna_frequency, antenna_list in antenna_freq_dict.items():
        for (x1, y1), (x2, y2) in itertools.combinations(antenna_list, 2):
            i = 1
            while (0 <= x2 + i * (x2 - x1) < x_len) and (
                0 <= y2 + i * (y2 - y1) < y_len
            ):
                antinodes_part2.add((x2 + i * (x2 - x1), y2 + i * (y2 - y1)))
                i += 1

            i = 1
            while (0 <= x2 + i * (x1 - x2) < x_len) and (
                0 <= y2 + i * (y1 - y2) < y_len
            ):
                antinodes_part2.add((x2 + i * (x1 - x2), y2 + i * (y1 - y2)))
                i += 1

    all_antenas = set(
        antena for antena_list in antenna_freq_dict.values() for antena in antena_list
    )
    return len(antinodes_part2.union(all_antenas))


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
