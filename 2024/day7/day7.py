import re

with open("./2024/day7/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

eq = []
for instruction in instruction_list:
    # print(instruction)
    res, nbs = re.search(r"(\d*): (.*)", instruction).groups()
    eq.append((int(res), [int(nb) for nb in nbs.split(" ")]))


def get_combinations(nb_list: list[int]) -> list[int]:
    if len(nb_list) == 1:
        return [nb_list[0]]

    res = [nb_list[-1] + nb for nb in get_combinations(nb_list[:-1])] + [
        nb_list[-1] * nb for nb in get_combinations(nb_list[:-1])
    ]

    return res


def get_combinations_part2(nb_list: list[int]) -> list[int]:
    if len(nb_list) == 1:
        return [nb_list[0]]

    res = (
        [nb_list[-1] + nb for nb in get_combinations_part2(nb_list[:-1])]
        + [nb_list[-1] * nb for nb in get_combinations_part2(nb_list[:-1])]
        + [int(str(nb) + str(nb_list[-1])) for nb in get_combinations_part2(nb_list[:-1])]
    )

    return res


nb_possibilities = 0
for res, nbs in eq:
    comb = get_combinations(nbs)
    if res in comb:
        nb_possibilities += res
        eq.remove((res, nbs))

print(f"Part 1: {nb_possibilities}")

nb_possibilities = 0
for res, nbs in eq:
    comb = get_combinations_part2(nbs)
    if res in comb:
        nb_possibilities += res

print(f"Part 2: {nb_possibilities}")
