with open("./2023/day9/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

total_part1, total_part2 = 0, 0
for instruction in instruction_list:
    derivation = [[int(k) for k in instruction.strip().split()]]
    i = 0
    while any([nb != 0 for nb in derivation[i]]):
        derivation.append([x - derivation[i][k - 1] for k, x in enumerate(derivation[i])][1:])
        i += 1

    # Part 1
    tmp = 0
    for i in range(len(derivation)-1, -1, -1):
        tmp += derivation[i][-1]
    total_part1 += tmp

    # Part 2
    tmp = 0
    for i in range(len(derivation)-1, -1, -1):
        tmp = derivation[i][0] - tmp

    total_part2 += tmp

print(f"Part1: {total_part1}")
print(f"Part2: {total_part2}")