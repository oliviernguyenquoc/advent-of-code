import pathlib


def part1(instruction_list):
    number_list = [int(instruction) for instruction in instruction_list]

    increase_count = 0
    previous_number = number_list[0]

    for number in number_list[1:]:
        if number > previous_number:
            increase_count += 1
        previous_number = number

    return increase_count


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
