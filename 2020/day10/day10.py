import functools
from typing import List

f = open("./day10/input.txt")

adaptator_list = f.readlines()
adaptator_list = [int(i) for i in adaptator_list]


def count_adaptator_spaces(adaptator_list: List[int]) -> int:
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


def count_combination_adaptator(adaptator_list: List[int]) -> int:

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


nb = count_adaptator_spaces(adaptator_list)
print(f"Answer part 1: {nb}")


nb_combination = count_combination_adaptator(adaptator_list)
print(f"Answer part 2: {nb_combination}")

f.close()
