from typing import List, Tuple


def list_seats_arround_part1(
    position_list: list, seat_list: List[str], x: int, y: int, i: int, j: int
):

    if (
        x + i >= 0
        and x + i < len(seat_list)
        and y + j >= 0
        and y + j < len(seat_list[0])
        and seat_list[x + i][y + j] != "."
    ):
        position_list.append((x + i, y + j))

    return position_list


def list_seats_arround_part2(
    position_list: list, seat_list: List[str], x: int, y: int, i: int, j: int
):

    position_i = i
    position_j = j

    while (
        x + position_i >= 0
        and x + position_i < len(seat_list)
        and y + position_j >= 0
        and y + position_j < len(seat_list[0])
    ):
        if seat_list[x + position_i][y + position_j] == ".":
            position_i += i
            position_j += j
        else:
            position_list.append((x + position_i, y + position_j))
            break

    return position_list


def apply_rules_for_one_seat(
    seat_list: List[str], x: int, y: int, part: int = 1
) -> Tuple[str, int, int]:

    if seat_list[x][y] == ".":
        return None

    seats_arround_list = []

    # Get seats arround
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (i == j == 0):
                if part == 1:
                    seats_arround_list = list_seats_arround_part1(
                        seats_arround_list, seat_list, x, y, i, j
                    )
                elif part == 2:
                    seats_arround_list = list_seats_arround_part2(
                        seats_arround_list, seat_list, x, y, i, j
                    )

    count_occupied_seats, count_empty_seats = 0, 0

    for seat in seats_arround_list:
        seat_state = seat_list[seat[0]][seat[1]]
        if seat_state == "#":
            count_occupied_seats += 1
        if seat_state == "L":
            count_empty_seats += 1

    # Max seat depends on the part of the exercise
    if part == 1:
        MAX_OCCUPIED_SEATS = 4
    elif part == 2:
        MAX_OCCUPIED_SEATS = 5

    if count_occupied_seats >= MAX_OCCUPIED_SEATS:
        return ("L", x, y)
    if count_empty_seats == len(seats_arround_list):
        return ("#", x, y)


def iteration(seat_list: List[str], part: int = 1) -> List[str]:

    change_to_apply = []
    for x, seat_row in enumerate(seat_list):
        for y, _ in enumerate(seat_row):
            change_instruction = apply_rules_for_one_seat(seat_list, x, y, part)
            if change_instruction:
                change_to_apply.append(change_instruction)

    for change in change_to_apply:
        x, y = change[1], change[2]
        tmp_seat_list = list(seat_list[x])
        tmp_seat_list[y] = change[0]
        seat_list[x] = "".join(tmp_seat_list)

    return seat_list


def print_seat_list(seat_list):
    print("-------")
    for i in seat_list:
        print(i)


PART = 2

f = open("./day11/input.txt")

seat_list = f.readlines()
# print(seat_list)

# Appply first rule
seat_list = [line.replace("\n", "") for line in seat_list]

old_seat_list = seat_list.copy()

seat_list = iteration(seat_list, part=PART)
# print_seat_list(seat_list)

while seat_list != old_seat_list:
    old_seat_list = seat_list.copy()
    seat_list = iteration(seat_list, part=PART)
    # print_seat_list(seat_list)

print(sum([seat_row.count("#") for seat_row in seat_list]))


f.close()
