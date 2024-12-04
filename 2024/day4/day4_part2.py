import collections

with open("./2024/day4/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

grid = [instruction.strip() for instruction in instruction_list]

count_xmas = 0
for y in range(1, len(grid)-1):
    for x in range(1, len(grid[0])-1):
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

print(f"Part 2: {count_xmas}")
