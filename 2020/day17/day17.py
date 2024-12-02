import copy
from typing import List


def neighbours_active(coord: List[str], z: int, j: int, i: int) -> (bool, bool):
    neighbours_list = [
        (a, b, c) for a in [-1, 0, 1] for b in [-1, 0, 1] for c in [-1, 0, 1]
    ]
    neighbours_list.remove((0, 0, 0))

    count_active = 0
    for z_n, j_n, i_n in neighbours_list:
        if (
            0 <= (z + z_n) <= len(coord) - 1
            and 0 <= (j + j_n) <= len(coord[0]) - 1
            and 0 <= (i + i_n) <= len(coord[0][0]) - 1
        ):
            if coord[z + z_n][j + j_n][i + i_n] == "#":
                count_active += 1

    is_two_or_three_active = False
    is_three_active = False

    if count_active == 3:
        is_two_or_three_active = True
        is_three_active = True
    elif count_active == 2:
        is_two_or_three_active = True

    return is_two_or_three_active, is_three_active


def count_active(coord: List[str]) -> int:
    counter_active = 0
    for z in range(len(coord)):
        for j in range(len(coord[z])):
            for i in range(len(coord[z][j])):
                if coord[z][j][i] == "#":
                    counter_active += 1
    return counter_active


def add_dimensions(coord: List[str]) -> List[str]:
    coord = (
        [["." * len(coord[0][0])] * len(coord[0])]
        + coord
        + [["." * len(coord[0][0])] * len(coord[0])]
    )

    for z in range(len(coord)):
        coord[z] = ["." * len(coord[0][0])] + coord[z] + ["." * len(coord[0][0])]

    for z in range(len(coord)):
        for j in range(len(coord[z])):
            coord[z][j] = "." + coord[z][j] + "."

    return coord


def d3print(coord):
    for z in range(len(coord)):
        print(f"\n z={z}")
        for j in range(len(coord[z])):
            print(coord[z][j])


f = open("./day17/input.txt")

coord = "".join(f.readlines()).split("\n")
coord = [coord]

for _ in range(6):
    coord = add_dimensions(coord)
    old_coord = copy.deepcopy(coord)

    for z in range(len(coord)):
        for j in range(len(coord[z])):
            for i in range(len(coord[z][j])):

                is_two_or_three_active, is_three_active = neighbours_active(
                    old_coord, z, j, i
                )
                if old_coord[z][j][i] == "#" and not is_two_or_three_active:
                    coord[z][j] = coord[z][j][:i] + "." + coord[z][j][i + 1 :]
                elif old_coord[z][j][i] == "." and is_three_active:
                    coord[z][j] = coord[z][j][:i] + "#" + coord[z][j][i + 1 :]

    nb_active = count_active(coord)
    print(nb_active)
f.close()