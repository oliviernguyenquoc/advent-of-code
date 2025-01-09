import pathlib

def part1(instruction_list):
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
        while (
            y - 1 >= 0
            and (x, y - 1) not in rock_tilt
            and (x, y - 1) not in cube_rock_list
        ):
            y -= 1
        rock_tilt.append((x, y))

    total = 0
    y_len = len(grid)
    for x, y in rock_tilt:
        total += y_len - y

    return total


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
