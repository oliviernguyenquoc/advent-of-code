import string

with open("./day3/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

score: int = 0
rucksacks_list: list[set[str]] = []

score_dict = {letter: n + 1 for n, letter in enumerate(string.ascii_letters)}

for instruction in instruction_list:
    if len(rucksacks_list) == 3:
        rucksacks_list = []

    rucksacks_list.append(set(instruction))

    if len(rucksacks_list) == 3:
        badge = set(rucksacks_list[0].intersection(rucksacks_list[1])).intersection(
            rucksacks_list[2]
        )
        score += score_dict[badge.pop()]

print(score)
