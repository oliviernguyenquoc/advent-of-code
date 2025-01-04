from typing import List

STEP_NUMBER = 100
PART = 2

if PART == 2:
    STEP_NUMBER = 10000

with open("./day11/input.txt") as f:
    instruction_list = f.read().splitlines()

grid_octopus: List[List[int]] = [
    [int(number_str) for number_str in instruction_line]
    for instruction_line in instruction_list
]


def _apply_change(grid: List[List[int]], i: int, j: int) -> List[List[int]]:
    if 0 < grid[i][j] < 10:
        grid[i][j] += 1
    if grid[i][j] > 9:
        grid[i][j] = 0
        grid = change_neighbours(grid, i, j)

    return grid


def change_neighbours(grid: List[List[int]], i: int, j: int) -> List[List[int]]:
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

    if PART == 2 and all([number == 0 for line in grid_octopus for number in line]):
        step_all_flash = step
        break


for i in range(len(grid_octopus)):
    print(grid_octopus[i])
# print(new_grid_octopus)
print(nb_total_flash)
print(step_all_flash + 1)
# print(count_number_nine([[2, 2, 2, 2, 2], [2, 10, 10, 10, 2], [2, 10, 2, 10, 2], [2, 10, 10, 10, 2], [2, 2, 2, 2, 2]],2,2))
