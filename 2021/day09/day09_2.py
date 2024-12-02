from typing import List, Tuple
import math

with open("./day09/input.txt") as f:
    instruction_list = f.read().splitlines()

grid = [
    [int(number_str) for number_str in instruction_line]
    for instruction_line in instruction_list
]

grid_width = len(grid)
grid_length = len(grid[0])


def get_bassin_size(
    grid: List[List[int]], position_x: int, position_y: int
) -> Tuple[List[List[int]], int]:
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


bassin_size_list = []

for i in range(grid_width):
    for j in range(grid_length):
        grid, bassin_size = get_bassin_size(grid, i, j)
        if bassin_size != 0:
            bassin_size_list.append(bassin_size)


print(bassin_size_list)
print(sorted(bassin_size_list)[-3:])
print(math.prod(sorted(bassin_size_list)[-3:]))
