import statistics
import pathlib


def part1(instruction_list):
    position_list = [int(instruction) for instruction in instruction_list[0].split(",")]

    median_position = int(statistics.median(position_list))

    sum_fuel = sum([abs(position - median_position) for position in position_list])

    return sum_fuel


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
