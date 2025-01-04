import re

with open("./day8/input.txt", encoding="utf-8") as f:
    instructions: list[str] = f.readlines()

commands = instructions.pop(0).rstrip()
instructions.pop(0)

map_dict = {}
for instruction in instructions:
    root, left, right = re.search(
        r"([A-Z]*) = \(([A-Z]*), ([A-Z]*)\)", instruction
    ).groups()
    map_dict[root + " L"] = left
    map_dict[root + " R"] = right

point = "AAA"
i = 0
while point != "ZZZ":
    left_or_right = commands[i % len(commands)]
    point = map_dict[point + " " + left_or_right]
    i += 1

nb_iter = i // len(commands)
print(i)
