import itertools
import pathlib


def part1(instruction_list):
    key_list = []
    lock_list = []
    for batch in itertools.batched(instruction_list, 8):
        heights = [0, 0, 0, 0, 0]
        for y in range(7):
            for x in range(5):
                if batch[y][x] == "#":
                    heights[x] += 1
        # key
        if batch[0].strip() == "#####":
            key_list.append(heights)
        # lock
        else:
            lock_list.append(heights)

    nb_match = 0
    for key, lock in itertools.product(key_list, lock_list):
        if all([key[i] + lock[i] <= 7 for i in range(5)]):
            nb_match += 1

    return nb_match


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
