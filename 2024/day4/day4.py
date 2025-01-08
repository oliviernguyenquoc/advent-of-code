import pathlib


def part1(instruction_list):
    grid = [instruction.strip() for instruction in instruction_list]

    len_y, len_x = len(grid), len(grid[0])
    directions = [
        [(0, i) for i in range(4)],
        [(i, 0) for i in range(4)],
        [(-i, -i) for i in range(4)],
        [(i, i) for i in range(4)],
        [(0, -i) for i in range(4)],
        [(-i, 0) for i in range(4)],
        [(-i, i) for i in range(4)],
        [(i, -i) for i in range(4)],
    ]

    count_xmas = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for direction in directions:
                joined_str = ""
                for point in direction:
                    if 0 <= x + point[0] < len_x and 0 <= y + point[1] < len_y:
                        joined_str += grid[y + point[1]][x + point[0]]
                    else:
                        break

                if joined_str == "XMAS":
                    count_xmas += 1

    return count_xmas


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
