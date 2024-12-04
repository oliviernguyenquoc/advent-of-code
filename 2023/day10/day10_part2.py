import dataclasses


@dataclasses.dataclass
class Position:
    grid: list[str]
    x1: int
    y1: int
    x2: int
    y2: int

def find_start(instruction_list: list[str]) -> tuple[int, int]:
    for j, instruction in enumerate(instruction_list):
        for i, char in enumerate(instruction):
            if char == "S":
                return (i, j)


with open("./2023/day10/test_input2.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

grid = [instruction.strip() for instruction in instruction_list]

start_x, start_y = find_start(instruction_list)

enable_in = [False] * len(grid[0])
memory = {"F": [False] * len(grid[0]),
"7": [False] * len(grid[0]),
}

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if grid[y][x]  == '-':
            enable_in[x] = not enable_in[x]
        if grid[y][x] == "F":
            memory["F"][x] = True
