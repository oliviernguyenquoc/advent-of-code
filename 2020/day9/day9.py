from typing import List, Tuple


def check_there_is_two_number_sum(a: int, x: List[int]) -> bool:
    """ O(nlog(n)) complexity, O(1) space algo Yeah !"""

    x = sorted(x)

    i, j = 0, len(x) - 1

    while i != j:
        if x[i] + x[j] == a:
            return True
        if x[i] + x[j] > a:
            j -= 1
        elif x[i] + x[j] < a:
            i += 1

    return False


def find_continuous_sum(a: int, x: List[int]) -> Tuple[int]:

    i, j = 0, 1

    while i != len(x) or j != len(x):
        sum_sub_x = sum(x[i:j])
        if sum_sub_x == a:
            return (i, j)
        elif sum_sub_x < a:
            j += 1
        elif sum_sub_x > a:
            i += 1

    return (0, 0)


f = open("./day9/input.txt")

nb_list = f.readlines()
nb_list = [int(nb) for nb in nb_list]
LEN_CHECK = 25

""" Complexity n * k*log(k) with k=25"""
for i in range(len(nb_list) - LEN_CHECK):
    if not check_there_is_two_number_sum(
        nb_list[i + LEN_CHECK], nb_list[i : i + LEN_CHECK]
    ):
        break

print(i)
print(f"Solution 1: {nb_list[i + LEN_CHECK]}")

a, b = find_continuous_sum(nb_list[i + LEN_CHECK], nb_list)
print(f"Solution 2: {min(nb_list[a:b])+ max(nb_list[a:b])}")

f.close()
