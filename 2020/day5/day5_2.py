import pathlib


def part2(seat_list):
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

    id_list = []

    for row, col in seat_position_list:
        id_list.append(8 * row + col)

    for i in range(13, 880):
        if i not in sorted(id_list):
            print(i)
    return sorted(id_list)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
