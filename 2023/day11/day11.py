with open("./2023/day11/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

grid = [instruction.strip() for instruction in instruction_list]

y_len, x_len = len(grid), len(grid[0])

empty_y_idx = [y for y in range(y_len) if grid[y] == "." * y_len]
empty_x_idx = [
    x for x in range(x_len) if all([grid[y][x] == "." for y in range(y_len)])
]

# Shift indexes to apply on good indexes
empty_x_idx = [x + i for i, x in enumerate(empty_x_idx)]

# Expend grid
while empty_y_idx:
    y = empty_y_idx.pop(0)
    grid = grid[: y + 1] + ["." * y_len] + grid[y + 1 :]
    empty_y_idx = [i + 1 for i in empty_y_idx]

y_len = len(grid)

for y in range(y_len):
    for x in empty_x_idx:
        grid[y] = grid[y][:x] + "." + grid[y][x:]

x_len = len(grid[0])

star_list = [(x, y) for y in range(y_len) for x in range(x_len) if grid[y][x] == "#"]

distance_matrix = [
    [abs(i - x) + abs(j - y) for (i, j) in star_list] for (x, y) in star_list
]

total = 0
for y in range(len(distance_matrix)):
    total += sum(distance_matrix[y])

print(f"Part 1: {total // 2}")
