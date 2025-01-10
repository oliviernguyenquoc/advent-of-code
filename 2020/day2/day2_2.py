import pathlib
import re


def part2(instruction_list):
    total_true_password = 0

    for arr in instruction_list:
        min_letter, max_letter, letter, password = re.search(
            r"(\d+)-(\d+) ([a-z]): ([a-z]+)", arr
        ).groups()
        min_letter, max_letter = int(min_letter), int(max_letter)
        # print((min_letter, max_letter, letter, password))
        if (password[min_letter - 1] == letter) != (password[max_letter - 1] == letter):
            total_true_password += 1
            print("true")

    return total_true_password


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
