with open("./2024/day19/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

towel_stock = set(instruction_list.pop(0).strip().split(", "))


def nb_stripes_possible(
    stripes_to_find: str, towel_stock: set[str], memory: dict[str, int]
) -> int:
    nb_combination = 0

    if stripes_to_find == "":
        return 1

    if stripes_to_find in memory:
        return memory[stripes_to_find]

    for towel in towel_stock:
        if stripes_to_find[: len(towel)] == towel:
            nb_combination += nb_stripes_possible(
                stripes_to_find[len(towel) :], towel_stock, memory
            )

    memory[stripes_to_find] = nb_combination

    return nb_combination


# Skip empty line
instruction_list.pop(0)

total_part2 = 0
# total= {}
for instruction in instruction_list:
    stripes_to_find = instruction.strip()

    new_memory = {}
    nb_stripes = nb_stripes_possible(stripes_to_find, towel_stock, new_memory)
    # total[stripes_to_find] = nb_stripes
    total_part2 += nb_stripes

print(total_part2)
