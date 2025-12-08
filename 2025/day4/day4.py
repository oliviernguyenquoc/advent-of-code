import pathlib


def _parse_instruction(instruction_list) -> set[tuple[int, int]]:
    return {
        (row, col)
        for row, instruction in enumerate(instruction_list)
        for col, char in enumerate(instruction)
        if char == "@"
    }


def get_movable_rolls(
    roll_set: set[tuple[int, int]], MAX_X: int, MAX_Y: int
) -> set[tuple[int, int]]:
    DIRECTIONS = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if (x, y) != (0, 0)]
    movable_rolls: set[tuple[int, int]] = set()

    for roll_x, roll_y in roll_set:
        adjacent_rolls = 0
        for x, y in DIRECTIONS:
            if (
                0 <= roll_x + x <= MAX_X - 1
                and 0 <= roll_y + y <= MAX_Y - 1
                and (roll_x + x, roll_y + y) in roll_set
            ):
                adjacent_rolls += 1

        if adjacent_rolls < 4:
            movable_rolls.add((roll_x, roll_y))

    return movable_rolls


def part1(instruction_list) -> int:
    roll_set = _parse_instruction(instruction_list)
    movable_roll_set = get_movable_rolls(
        roll_set, len(instruction_list[0].strip()), len(instruction_list)
    )

    return len(movable_roll_set)


def part2(instruction_list) -> int:
    roll_set = _parse_instruction(instruction_list)
    movable_roll_set: set[tuple[int, int]] = {(-1, -1)}
    MAX_X, MAX_Y = len(instruction_list[0].strip()), len(instruction_list)
    total = 0

    while movable_roll_set:
        movable_roll_set = get_movable_rolls(roll_set, MAX_X, MAX_Y)
        total += len(movable_roll_set)
        roll_set = roll_set - movable_roll_set

    return total


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
