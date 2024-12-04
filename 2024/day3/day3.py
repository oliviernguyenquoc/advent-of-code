import re

with open("./2024/day3/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

mult_list: list[tuple[str, str]] = []
for instruction in instruction_list:
    regex = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\))", instruction)
    mult_list += regex

integers: list[tuple[int, int]] = []
for multiplation in mult_list:
    integers.append(re.search(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", multiplation).groups())

total = 0
for i in integers:
    print(int(i[0]),int(i[1]))
    total += (int(i[0]) * int(i[1]))

print(f"Part 1: {total}")