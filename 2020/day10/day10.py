import functools
import pathlib


def count_adaptator_spaces(adaptator_list: list[int]) -> int:
    adaptator_list = sorted(adaptator_list)
    adaptator_list = [0] + adaptator_list + [adaptator_list[-1] + 3]

    diff_adaptator_list = [
        adaptator_list[i + 1] - adaptator_list[i]
        for i in range(len(adaptator_list) - 1)
    ]

    count_one = diff_adaptator_list.count(1)
    count_three = diff_adaptator_list.count(3)
    print(count_one, count_three)

    return count_one * count_three


@functools.lru_cache(maxsize=None)
def _multiplier(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return _multiplier(n - 1) + _multiplier(n - 2) + _multiplier(n - 3)


def count_combination_adaptator(adaptator_list: list[int]) -> int:
    nb_combination = 1
    adaptator_list = sorted(adaptator_list)
    adaptator_list = [0] + adaptator_list + [adaptator_list[-1] + 3]

    diff_adaptator_list = [
        adaptator_list[i + 1] - adaptator_list[i]
        for i in range(len(adaptator_list) - 1)
    ]

    print(diff_adaptator_list)

    n_one = 0

    # Compute number of consecutive 1 then multiply by the right factor
    for i in range(len(diff_adaptator_list) - 1, -1, -1):
        if diff_adaptator_list[i] == 3:
            if n_one != 0:
                nb_combination *= _multiplier(n_one)
            n_one = 0
        else:
            n_one += 1

    if n_one != 0:
        nb_combination *= _multiplier(n_one)

    return nb_combination


def part1(adaptator_list):
    adaptator_list = [int(i) for i in adaptator_list]

    nb = count_adaptator_spaces(adaptator_list)
    return nb


def part2(adaptator_list):
    nb_combination = count_combination_adaptator(adaptator_list)
    return nb_combination


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    instruction_list = [int(i.strip()) for i in instruction_list]

    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
