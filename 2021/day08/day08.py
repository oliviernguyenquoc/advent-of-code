import pathlib


def part1(instruction_list):
    output_value_list = [
        instruction.split(" | ")[1] for instruction in instruction_list
    ]
    output_value_list = [output_value.split() for output_value in output_value_list]

    # digits_dict = {2: 1, 3: 7, 4: 4, 7: 8}
    count_digits = {2: 0, 3: 0, 4: 0, 7: 0}

    for output_value in output_value_list:
        for letters in output_value:
            if len(letters) in count_digits:
                count_digits[len(letters)] += 1

    return sum(count_digits.values())


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
