import pathlib


def part1(instruction_list):
    grid = [
        [int(number_str) for number_str in instruction_line]
        for instruction_line in instruction_list
    ]

    grid_width = len(grid)
    grid_length = len(grid[0])

    low_points_height_list = []

    for i in range(grid_width):
        for j in range(grid_length):
            # print((i, j, grid_width, grid_length))
            if (
                (i - 1 < 0 or grid[i - 1][j] > grid[i][j])
                and (j - 1 < 0 or grid[i][j - 1] > grid[i][j])
                and (i + 1 >= grid_width or grid[i + 1][j] > grid[i][j])
                and (j + 1 >= grid_length or grid[i][j + 1] > grid[i][j])
            ):
                low_points_height_list.append(grid[i][j])

    return sum([point + 1 for point in low_points_height_list])


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
