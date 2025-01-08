import pathlib


def part2(instruction_list):
    number_list = [int(instruction) for instruction in instruction_list]

    increase_count = 0

    for i in range(1, len(number_list[1:-1])):
        if sum(number_list[i : i + 3]) > sum(number_list[i - 1 : i + 2]):
            increase_count += 1

    return increase_count


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
