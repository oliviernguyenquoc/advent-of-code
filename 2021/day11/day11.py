import pathlib


def _apply_change(grid: list[list[int]], i: int, j: int) -> list[list[int]]:
    if 0 < grid[i][j] < 10:
        grid[i][j] += 1
    if grid[i][j] > 9:
        grid[i][j] = 0
        grid = change_neighbours(grid, i, j)

    return grid


def change_neighbours(grid: list[list[int]], i: int, j: int) -> list[list[int]]:
    if i - 1 >= 0:
        grid = _apply_change(grid, i - 1, j)
    if i - 1 >= 0 and j - 1 >= 0:
        grid = _apply_change(grid, i - 1, j - 1)
    if i - 1 >= 0 and j + 1 < len(grid[0]):
        grid = _apply_change(grid, i - 1, j + 1)
    if i + 1 < len(grid):
        grid = _apply_change(grid, i + 1, j)
    if i + 1 < len(grid) and j - 1 >= 0:
        grid = _apply_change(grid, i + 1, j - 1)
    if i + 1 < len(grid) and j + 1 < len(grid[0]):
        grid = _apply_change(grid, i + 1, j + 1)
    if j - 1 >= 0:
        grid = _apply_change(grid, i, j - 1)
    if j + 1 < len(grid[0]):
        grid = _apply_change(grid, i, j + 1)

    return grid


def print_grid(grid_octopus):
    for i in range(len(grid_octopus)):
        print(grid_octopus[i])


def solve(instruction_list, part):
    if part == 1:
        STEP_NUMBER = 100
    else:
        STEP_NUMBER = 10000

    grid_octopus: list[list[int]] = [
        [int(number_str) for number_str in instruction_line]
        for instruction_line in instruction_list
    ]

    nb_total_flash: int = 0
    step_all_flash: int = 0

    for step in range(STEP_NUMBER):
        # Add 1 everywhere in the grid
        grid_octopus = [[number + 1 for number in line] for line in grid_octopus]

        for i in range(len(grid_octopus)):
            for j in range(len(grid_octopus[0])):
                if grid_octopus[i][j] > 9:
                    grid_octopus[i][j] = 0
                    grid_octopus = change_neighbours(grid_octopus, i, j)

        for i in range(len(grid_octopus)):
            for j in range(len(grid_octopus[0])):
                if grid_octopus[i][j] == 0:
                    nb_total_flash += 1

        if part == 2 and all([number == 0 for line in grid_octopus for number in line]):
            step_all_flash = step
            break

    print_grid(grid_octopus)

    if part == 1:
        return nb_total_flash
    else:
        return step_all_flash + 1


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
