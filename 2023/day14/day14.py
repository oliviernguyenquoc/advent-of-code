with open("./2023/day14/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

grid = [instroduction.strip() for instroduction in instruction_list]

rock_list = []
cube_rock_list = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "O":
            rock_list.append((x, y))
        if grid[y][x] == "#":
            cube_rock_list.append((x, y))

rock_tilt = []

while rock_list:
    x, y = rock_list.pop(0)
    while y-1 >= 0 and (x, y - 1) not in rock_tilt and (x, y - 1) not in cube_rock_list:
        y -= 1
    rock_tilt.append((x, y))

total = 0
x_len, y_len = len(grid[0]), len(grid)
for x, y in rock_tilt:
    total += (y_len - y)

print(total)