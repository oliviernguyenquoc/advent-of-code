import re

with open("./day4/input.txt", encoding="utf-8") as f:
    instructions: list[str] = f.readlines()

instersect_list: list[set[int]] = []

for instruction in instructions:
    idx, winning_str, own_str = re.search(
        r"Card *([0-9]*): ([0-9 ]*) \| ([0-9 ]*)", instruction
    ).groups()
    winning_nbr = set(int(nb) for nb in winning_str.split(" ") if nb != "")
    own_nbr = set(int(nb) for nb in own_str.split(" ") if nb != "")

    instersect_list.append(winning_nbr.intersection(own_nbr))

part1 = sum(
    [2 ** (len(nb_list) - 1) for nb_list in instersect_list if len(nb_list) != 0]
)

# Part 1
print(f"Part 1: {part1}")

# Part 2
total_list: list[int] = [1] * len(instersect_list)
total_list += [0] * len(instersect_list)

for i, inter in enumerate(instersect_list):
    nb_win = len(inter)
    for j in range(1, nb_win + 1):
        total_list[i + j] += total_list[i]


print(f"Part 2: {sum(total_list)}")
