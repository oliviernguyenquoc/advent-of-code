import string
import pathlib


def part1(instruction_list):
    score = 0
    score_dict = {letter: n + 1 for n, letter in enumerate(string.ascii_letters)}

    for instruction in instruction_list:
        rucksacks_str1 = instruction[: (len(instruction) // 2)]
        rucksacks_str2 = instruction[len(instruction) // 2 :]
        common = set(rucksacks_str1).intersection(set(rucksacks_str2))
        assert len(common) == 1

        score += score_dict[common.pop()]

    return score


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
