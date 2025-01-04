import pathlib

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def parse(instruction_list):
    grid = [
        [int(number_str) for number_str in instruction_line.strip()]
        for instruction_line in instruction_list
    ]

    trail_head_list = [
        (x, y)
        for y, nb_list in enumerate(grid)
        for x, nb in enumerate(nb_list)
        if nb == 0
    ]

    return grid, trail_head_list


def get_score(grid, x, y) -> int:
    LEN_X, LEN_Y = len(grid[0]), len(grid)

    end_points = set()
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for direction in DIRECTIONS:
            if (
                0 <= y + direction[1] < LEN_Y
                and 0 <= x + direction[0] < LEN_X
                and grid[y + direction[1]][x + direction[0]] == grid[y][x] + 1
            ):
                if grid[y + direction[1]][x + direction[0]] == 9:
                    end_points.add((x + direction[0], y + direction[1]))
                    continue
                else:
                    queue.append((x + direction[0], y + direction[1]))

    return len(end_points)


def part1(instruction_list):
    grid, trail_head_list = parse(instruction_list)

    total = 0
    for x, y in trail_head_list:
        total += get_score(grid, x, y)

    print(f"Part 1: {total}")
    return total


def get_score_part2(grid, x: int, y: int) -> int:
    total = 0

    if grid[y][x] == 9:
        return 1

    len_x, len_y = len(grid[0]), len(grid)

    for direction in DIRECTIONS:
        if (
            0 <= y + direction[1] < len_y
            and 0 <= x + direction[0] < len_x
            and grid[y + direction[1]][x + direction[0]] == grid[y][x] + 1
        ):
            total += get_score_part2(grid, x + direction[0], y + direction[1])

    return total


def part2(instruction_list):
    grid, trail_head_list = parse(instruction_list)

    total_part2 = 0
    for x, y in trail_head_list:
        total_part2 += get_score_part2(grid, x, y)

    print(f"Part 2: {total_part2}")
    return total_part2


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
