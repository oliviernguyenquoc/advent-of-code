with open("./day09/input.txt") as f:
    instruction_list = f.read().splitlines()

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

print(sum([point + 1 for point in low_points_height_list]))
