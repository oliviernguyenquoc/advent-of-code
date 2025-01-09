import copy
import pathlib


def expand_space(grid: list[str], nb_spaces: int = 0) -> list[str]:
    y_len, x_len = len(grid), len(grid[0])

    empty_y_idx = [y for y in range(y_len) if grid[y] == "." * y_len]
    empty_x_idx = [
        x for x in range(x_len) if all([grid[y][x] == "." for y in range(y_len)])
    ]

    # Shift indexes to apply on good indexes
    empty_x_idx = [idx + i * (nb_spaces - 1) for i, idx in enumerate(empty_x_idx)]
    empty_y_idx = [idx + i * (nb_spaces - 1) for i, idx in enumerate(empty_y_idx)]

    # Expend grid
    for y in empty_y_idx:
        grid = grid[:y] + ["." * y_len] * nb_spaces + grid[y + 1 :]

    y_len = len(grid)

    for y in range(y_len):
        for x in empty_x_idx:
            grid[y] = grid[y][:x] + "." * nb_spaces + grid[y][x + 1 :]

    return grid


def solve(instruction_list, part, multiplier=500000):
    grid = [instruction.strip() for instruction in instruction_list]

    grid2 = copy.deepcopy(grid)
    grid0 = copy.deepcopy(grid)

    grid2 = expand_space(grid2, 2)

    x_len2, y_len2 = len(grid2[0]), len(grid2)
    star_list = [
        (x, y) for y in range(y_len2) for x in range(x_len2) if grid2[y][x] == "#"
    ]

    distance_matrix = [
        [abs(i - x) + abs(j - y) for (i, j) in star_list] for (x, y) in star_list
    ]

    total = 0
    for y in range(len(distance_matrix)):
        total += sum(distance_matrix[y])

    if part == 1:
        return total // 2

    grid0 = expand_space(grid0, 0)

    x_len0, y_len0 = len(grid0[0]), len(grid0)
    star_list0 = [
        (x, y) for y in range(y_len0) for x in range(x_len0) if grid0[y][x] == "#"
    ]

    distance_matrix0 = [
        [abs(i - x) + abs(j - y) for (i, j) in star_list0] for (x, y) in star_list0
    ]

    diff_matrix = []

    for y in range(len(distance_matrix)):
        line = []
        for x in range(len(distance_matrix[0])):
            line.append(distance_matrix0[y][x] - distance_matrix[y][x])
        diff_matrix.append(line)

    distance_matrix3 = [
        [
            multiplier * (distance_matrix[y][x] - distance_matrix0[y][x])
            + distance_matrix0[y][x]
            for x in range(len(distance_matrix[0]))
        ]
        for y in range(len(distance_matrix))
    ]

    total = 0
    for y in range(len(distance_matrix3)):
        total += sum(distance_matrix3[y])

    return total // 2


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
