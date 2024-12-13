import re
import itertools
import numpy as np

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X = 18641, Y = 10279

# a_x * nb_button_1 + a_y * nb_button_2 = 18641
# b_x * nb_button_1 + b_y * nb_button_2 = 10279


def get_resolution(
    a_x: int, a_y: int, b_x: int, b_y: int, prize_x: int, prize_y: int
) -> tuple[int, int]:

    matrix = np.array([[a_x, b_x], [a_y, b_y]])
    prize_arr = np.array([prize_x, prize_y])
    det = np.linalg.det(matrix)

    if det != 0:
        inv_matrix = np.linalg.inv(matrix)
        nb_button_1, nb_button_2 = np.dot(inv_matrix, prize_arr)
        if (
            round(nb_button_1) > 0
            and round(nb_button_2) > 0
            and np.array_equal(
                np.dot(matrix, np.array([round(nb_button_1), round(nb_button_2)])),
                prize_arr,
            )
        ):
            return round(nb_button_1), round(nb_button_2)

    return 0, 0


with open("./2024/day13/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

instruction_list = [
    instruction.strip() for instruction in instruction_list if instruction != "\n"
]

total = 0
total_part2 = 0

for button_A_instruct, button_B_instruct, prize_instruct in itertools.batched(
    instruction_list, 3
):
    a_x, a_y = re.search(r"Button A: X\+(\d*), Y\+(\d*)", button_A_instruct).groups()
    b_x, b_y = re.search(r"Button B: X\+(\d*), Y\+(\d*)", button_B_instruct).groups()
    prize_x, prize_y = re.search(r"Prize: X=(\d*), Y=(\d*)", prize_instruct).groups()

    nb_button_1, nb_button_2 = get_resolution(
        int(a_x), int(a_y), int(b_x), int(b_y), int(prize_x), int(prize_y)
    )
    total += 3 * nb_button_1 + nb_button_2

    nb_button_1_part2, nb_button_2_part2 = get_resolution(
        int(a_x),
        int(a_y),
        int(b_x),
        int(b_y),
        10000000000000 + int(prize_x),
        10000000000000 + int(prize_y),
    )
    total_part2 += 3 * nb_button_1_part2 + nb_button_2_part2

print(f"Part 1: {total}")
print(f"Part 2: {total_part2}")
