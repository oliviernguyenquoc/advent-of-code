import pathlib
import math


def get_bassin_size(
    grid: list[list[int]], position_x: int, position_y: int
) -> tuple[list[list[int]], int]:
    bassin_size = 0
    grid_width, grid_length = len(grid), len(grid[0])

    if grid[position_x][position_y] != 9:
        grid[position_x][position_y] = 9
        bassin_size += 1
    else:
        return grid, 0

    if position_x - 1 >= 0 and grid[position_x - 1][position_y] != 9:
        grid, sub_bassin_size = get_bassin_size(grid, position_x - 1, position_y)
        bassin_size += sub_bassin_size
    if position_y - 1 >= 0 and grid[position_x][position_y - 1] != 9:
        grid, sub_bassin_size = get_bassin_size(grid, position_x, position_y - 1)
        bassin_size += sub_bassin_size
    if position_x + 1 < grid_width and grid[position_x + 1][position_y] != 9:
        grid, sub_bassin_size = get_bassin_size(grid, position_x + 1, position_y)
        bassin_size += sub_bassin_size
    if position_y + 1 < grid_length and grid[position_x][position_y + 1] != 9:
        grid, sub_bassin_size = get_bassin_size(grid, position_x, position_y + 1)
        bassin_size += sub_bassin_size

    return grid, bassin_size


def part2(instruction_list):
    grid = [
        [int(number_str) for number_str in instruction_line]
        for instruction_line in instruction_list
    ]

    grid_width = len(grid)
    grid_length = len(grid[0])

    bassin_size_list = []

    for i in range(grid_width):
        for j in range(grid_length):
            grid, bassin_size = get_bassin_size(grid, i, j)
            if bassin_size != 0:
                bassin_size_list.append(bassin_size)

    print(bassin_size_list)
    print(sorted(bassin_size_list)[-3:])
    return math.prod(sorted(bassin_size_list)[-3:])


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
