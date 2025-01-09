import pathlib


def part1(seat_list):
    seat_position_list = []

    for seat in seat_list:
        min_row = 0
        max_row = 128
        min_col = 0
        max_col = 8

        for instruction in seat:
            # print(instruction)
            if instruction == "F":
                max_row = max_row - ((max_row - min_row) // 2)
            elif instruction == "B":
                min_row = min_row + ((max_row - min_row) // 2)
            elif instruction == "R":
                min_col = min_col + ((max_col - min_col) // 2)
            elif instruction == "L":
                max_col = max_col - ((max_col - min_col) // 2)

        if min_row == max_row - 1 and min_col == max_col - 1:
            seat_position_list.append((min_row, min_col))
        else:
            raise Exception("ERROR")

    print(seat_position_list)

    max_id = 0

    for row, col in seat_position_list:
        if 8 * row + col > max_id:
            max_id = 8 * row + col

    return max_id


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
