import copy
import pathlib


def tilt(
    rock_list: list[tuple[int, int]],
    cube_rock_list: list[tuple[int, int]],
    x_len: int,
    y_len: int,
    move: tuple[int, int],
) -> list[tuple[int, int]]:
    match move:
        case (0, 1):
            rock_list = sorted(rock_list, key=lambda x: x[1], reverse=True)
        case (0, -1):
            rock_list = sorted(rock_list, key=lambda x: x[1])
        case (1, 0):
            rock_list = sorted(rock_list, key=lambda x: x[0], reverse=True)
        case (-1, 0):
            rock_list = sorted(rock_list, key=lambda x: x[0])
    rock_tilt = []

    while rock_list:
        x, y = rock_list.pop(0)
        while (
            0 <= x + move[0] < x_len
            and 0 <= y + move[1] < y_len
            and (x + move[0], y + move[1]) not in rock_tilt
            and (x + move[0], y + move[1]) not in cube_rock_list
        ):
            x += move[0]
            y += move[1]
        rock_tilt.append((x, y))

    return rock_tilt


def part2(instruction_list, cycle_length=9):
    grid = [instroduction.strip() for instroduction in instruction_list]

    rock_list = []
    cube_rock_list = []

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
                rock_list.append((x, y))
            if grid[y][x] == "#":
                cube_rock_list.append((x, y))

    DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    rock_tilt = copy.deepcopy(rock_list)
    total = []

    for i in range(150):
        for direction in DIRECTIONS:
            rock_list = copy.deepcopy(rock_tilt)
            rock_tilt = tilt(
                rock_list,
                cube_rock_list,
                x_len=len(grid[0]),
                y_len=len(grid),
                move=direction,
            )

        tmp = 0
        y_len = len(grid)
        for x, y in rock_tilt:
            tmp += y_len - y

        total.append(tmp)
        if (i + 1) % cycle_length == 0:
            return tmp


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list, 13)}")
