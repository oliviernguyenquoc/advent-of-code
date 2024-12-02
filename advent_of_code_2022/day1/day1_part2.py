with open("./day1/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

max_weight_list: list[int] = [0, 0, 0]
current_elf_weight: int = 0

for instruction in instruction_list:
    if instruction != "":
        current_elf_weight += int(instruction)
    else:
        if max_weight_list[0] < current_elf_weight:
            max_weight_list[0] = current_elf_weight
            max_weight_list.sort()
        current_elf_weight = 0

print(max_weight_list)
print(sum(max_weight_list))
