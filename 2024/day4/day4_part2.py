import collections
import pathlib


def part2(instruction_list):
    grid = [instruction.strip() for instruction in instruction_list]

    count_xmas = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            counter = collections.Counter(
                [
                    grid[y - 1][x - 1],
                    grid[y + 1][x - 1],
                    grid[y - 1][x + 1],
                    grid[y + 1][x + 1],
                ]
            )

            if (
                counter["M"] == counter["S"] == 2
                and grid[y - 1][x - 1] != grid[y + 1][x + 1]
                and grid[y][x] == "A"
            ):
                count_xmas += 1

    return count_xmas


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 2: {part2(instruction_list)}")
