from collections import Counter

with open("./day23/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()


direction_list = ["N", "S", "E", "W"]


def check_all_direction(elf_set: set[tuple[int, int]], elf_x: int, elf_y: int):
    ALL_DIRECTION = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]
    return not any(
        [
            (elf_x + move_x, elf_y + move_y) in elf_set
            for move_x, move_y in ALL_DIRECTION
        ]
    )


def check_direction(
    elf_set: set[tuple[int, int]], elf_x: int, elf_y: int, direction: str
) -> bool:
    DIRECTION_DICT = {
        "W": [(1, 0), (1, -1), (1, 1)],
        "S": [(0, 1), (-1, 1), (1, 1)],
        "E": [(-1, 0), (-1, -1), (-1, 1)],
        "N": [(0, -1), (-1, -1), (1, -1)],
    }
    return not any(
        [
            (elf_x + move_x, elf_y + move_y) in elf_set
            for move_x, move_y in DIRECTION_DICT[direction]
        ]
    )


def move_direction(elf_x: int, elf_y: int, direction: str) -> tuple[int, int]:
    MOVE_DICT = {"W": (1, 0), "S": (0, 1), "E": (-1, 0), "N": (0, -1)}
    return (elf_x + MOVE_DICT[direction][0], elf_y + MOVE_DICT[direction][1])


elf_set = set()

for idx_y, instruction in enumerate(instruction_list):
    for idx_x, letter in enumerate(instruction):
        if letter == "#":
            elf_set.add((idx_x, idx_y))

# print(elf_set)
print(len(elf_set))
round = 1
while True:
    print(round)
    old_elf_set = elf_set.copy()
    elf_dict = {}

    for elf_x, elf_y in elf_set:
        have_elf_moved = False
        for direction in direction_list:
            if check_all_direction(elf_set, elf_x, elf_y):
                break
            if check_direction(elf_set, elf_x, elf_y, direction):
                elf_dict[(elf_x, elf_y)] = move_direction(elf_x, elf_y, direction)
                have_elf_moved = True
                break
        if not have_elf_moved:
            elf_dict[(elf_x, elf_y)] = (elf_x, elf_y)

    new_elf_list = [
        elf_position
        for elf_position, nb_values in Counter(elf_dict.values()).items()
        if nb_values == 1
    ]

    for elf_old_position, elf_new_position in elf_dict.items():
        if elf_new_position not in new_elf_list:
            new_elf_list.append(elf_old_position)

    direction_list = direction_list[1:] + [direction_list[0]]

    elf_set = set(new_elf_list)

    if elf_set == old_elf_set:
        break

    round += 1

print(len(elf_set))
x_min = min([x for x, _ in elf_set])
x_max = max([x for x, _ in elf_set])
y_min = min([y for _, y in elf_set])
y_max = max([y for _, y in elf_set])

print(f"Nb tiles empty: {((x_max - x_min+1) * (y_max - y_min+1)) - len(elf_set)}")
print(f"Nb round {round}")
