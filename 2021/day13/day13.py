import pathlib


def print_coordinates(coordinates: set[tuple[int, int]]):
    max_x = max([coordinate[0] for coordinate in coordinates]) + 1
    max_y = max([coordinate[1] for coordinate in coordinates]) + 1

    img_str: str = ""
    for j in range(max_y):
        for i in range(max_x):
            if (i, j) in coordinates:
                img_str += "#"
            else:
                img_str += " "
        img_str += "\n"

    print(img_str)


def solve(instruction_list, part):
    coordinates: list[tuple[int, int]] = []
    for instruction_step, instruction in enumerate(instruction_list):
        if instruction == "":
            break_step: int = instruction_step
            break
        x, y = instruction.split(",")
        coordinates.append((int(x), int(y)))

    for instruction in instruction_list[break_step + 1 :]:
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

        if part == 1:
            break

    print_coordinates(set(coordinates))

    return len(set(coordinates))


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
