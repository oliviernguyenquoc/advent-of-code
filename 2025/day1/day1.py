import pathlib


def part1(instruction_list) -> int:
    index: int = 50
    nb_zero_positions: int = 0

    for instruction in instruction_list:
        match instruction[0]:
            case "L":
                index = (index - int(instruction[1:])) % 100
            case "R":
                index = (index + int(instruction[1:])) % 100
        if index == 0:
            nb_zero_positions += 1
    return nb_zero_positions


def part2(instruction_list) -> int:
    current_position: int = 50
    nb_zero_positions: int = 0

    for instruction in instruction_list:
        instruction = instruction.strip()
        lr_command, nb_moves = instruction[0], int(instruction[1:])

        nb_zero_positions += nb_moves // 100
        nb_moves = nb_moves % 100

        match lr_command:
            case "L":
                before_moving_position = current_position
                current_position -= nb_moves
                if current_position < 0 < before_moving_position:
                    nb_zero_positions += 1
                current_position = current_position % 100

            case "R":
                before_moving_position = current_position
                current_position += nb_moves
                if current_position > 100 > before_moving_position:
                    nb_zero_positions += 1
                current_position = current_position % 100

        if current_position == 0 or current_position == 100:
            current_position = 0
            nb_zero_positions += 1

    return nb_zero_positions


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")  # 5828 / 4817
