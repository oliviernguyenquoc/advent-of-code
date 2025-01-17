import pathlib
import re


def part1(instruction_list):
    total_true_password = 0

    for arr in instruction_list:
        min_letter, max_letter, letter, password = re.search(
            r"(\d+)-(\d+) ([a-z]): ([a-z]+)", arr
        ).groups()
        min_letter, max_letter = int(min_letter), int(max_letter)
        count_letter = password.count(letter)
        if count_letter >= min_letter and count_letter <= max_letter:
            total_true_password += 1

    return total_true_password


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
