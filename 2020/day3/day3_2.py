from functools import reduce
import pathlib


def part2(map_list):
    nb_tree_list = []
    direction_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(direction_list)
    for direction in direction_list:
        nb_tree = 0
        for n_line, line in enumerate(map_list):
            if (
                n_line % direction[1] == 0
                and line[(n_line // direction[1] * direction[0]) % (len(line) - 1)]
                == "#"
            ):
                nb_tree += 1

        nb_tree_list.append(nb_tree)

    print(nb_tree_list)
    return reduce((lambda x, y: x * y), nb_tree_list)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 2: {part2(instruction_list)}")
