import pathlib


def part1(map_list):
    nb_tree = 0

    for n_line, line in enumerate(map_list):
        if line[(n_line * 3) % (len(line) - 1)] == "#":
            nb_tree += 1

    return nb_tree


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
