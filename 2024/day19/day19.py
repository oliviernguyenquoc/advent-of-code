with open("./2024/day19/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

towel_stock = set(instruction_list.pop(0).strip().split(", "))


def is_stripes_possible(stripes_to_find: str, towel_stock: set[str]) -> bool:
    if stripes_to_find == "":
        return True
    for towel in towel_stock:
        if stripes_to_find[: len(towel)] == towel:
            if is_stripes_possible(stripes_to_find[len(towel) :], towel_stock):
                return True

    return False


# Skip empty line
instruction_list.pop(0)

total = 0
for instruction in instruction_list:
    stripes_to_find = instruction.strip()

    if is_stripes_possible(stripes_to_find, towel_stock):
        total += 1

print(total)
