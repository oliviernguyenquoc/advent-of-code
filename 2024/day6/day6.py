from collections import defaultdict
from tqdm import tqdm
import copy
import pathlib


def test_loop(
    grid: list[str],
    obstacle_list: list[tuple[int, int]],
    position_x: int,
    position_y: int,
) -> tuple[bool, set[tuple[int, int]]]:
    """
    Return (If there is a loop, visited positions)
    """

    DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    checking_position = defaultdict(bool)
    checking_position[(position_x, position_y)] = False
    is_checking = False

    i = 0
    while (0 <= position_x < len(grid[0]) and 0 <= position_y < len(grid)) and (
        not is_checking or any([not check for check in checking_position.values()])
    ):
        while (
            (
                position_x + DIRECTIONS[i][0],
                position_y + DIRECTIONS[i][1],
            )
            not in obstacle_list
            and (0 <= position_x < len(grid[0]) and 0 <= position_y < len(grid))
            and (
                not is_checking
                or any([not check for check in checking_position.values()])
            )
        ):
            position_x += DIRECTIONS[i][0]
            position_y += DIRECTIONS[i][1]

            if (position_x, position_y) not in checking_position.keys():
                checking_position[(position_x, position_y)] = False
                if is_checking:
                    is_checking = False
                    checking_position = {
                        position: False for position in checking_position.keys()
                    }
            elif checking_position[(position_x, position_y)]:
                return True, checking_position.keys()
            else:
                checking_position[(position_x, position_y)] = True
                is_checking = True

        i = (i + 1) % 4

    checking_position.pop((position_x, position_y), None)

    return (
        is_checking and all([check for check in checking_position.values()]),
        checking_position,
    )


def solve(instruction_list, part):
    grid = [instruction.strip() for instruction in instruction_list]

    obstacle_list = [
        (x, y)
        for y in range(len(grid))
        for x in range(len(grid[0]))
        if grid[y][x] == "#"
    ]

    start_x, start_y = [
        (x, y)
        for y in range(len(grid))
        for x in range(len(grid[0]))
        if grid[y][x] == "^"
    ][0]

    is_loop, position_visited = test_loop(grid, obstacle_list, start_x, start_y)

    if part == 1:
        return len(position_visited)

    possible_obstacle_list = copy.deepcopy(position_visited)

    print(f"{len(possible_obstacle_list)} points to check")

    nb_possible_obstacle_loop = 0
    for i, (x, y) in tqdm(enumerate(possible_obstacle_list)):
        # print(f"Point n°{i}: ({x}, {y})")
        is_loop, position_visited = test_loop(
            grid,
            obstacle_list=obstacle_list + [(x, y)],
            position_x=start_x,
            position_y=start_y,
        )
        if grid[y][x] not in obstacle_list and is_loop:
            nb_possible_obstacle_loop += 1

    return nb_possible_obstacle_loop


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
