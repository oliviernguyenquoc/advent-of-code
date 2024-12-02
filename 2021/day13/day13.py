from typing import List, Tuple, Set

STEP = 2

def print_coordinates(coordinates: Set[Tuple[int, int]]):

    max_x = max([coordinate[0] for coordinate in coordinates]) +1
    max_y = max([coordinate[1] for coordinate in coordinates]) +1

    img_str: str = ""
    for j in range(max_y):
        for i in range(max_x):
            if (i,j) in coordinates:
                img_str += "#"
            else:
                img_str += " "
        img_str += "\n"

    print(img_str)

with open("./day13/input.txt") as f:
    instruction_list = f.read().splitlines()

coordinates: List[Tuple[int, int]] = []
for instruction_step, instruction in enumerate(instruction_list):
    if instruction == '':
        break_step: int = instruction_step
        break
    x, y = instruction.split(",")
    coordinates.append((int(x), int(y)))

for instruction in instruction_list[break_step+1:]:
    if instruction[:10] == "fold along":
        match instruction[11]:
            case "y":
                fold_y: int = int(instruction[13:])
                for i, coordinate in enumerate(coordinates):
                    if coordinate[1] > fold_y:
                        coordinates[i] = (coordinate[0], 2 * fold_y - coordinate[1])
            case "x":
                fold_x: int = int(instruction[13:])
                for i, coordinate in enumerate(coordinates):
                    if coordinate[0] > fold_x:
                        coordinates[i] = (2 * fold_x - coordinate[0], coordinate[1])

    if STEP == 1:
        break

print(f"Number of dots: {len(set(coordinates))}")

print_coordinates(set(coordinates))

