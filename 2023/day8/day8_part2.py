import re
import copy
import itertools
import math

with open("./day8/input.txt", encoding="utf-8") as f:
    instructions: list[str] = f.readlines()

commands = instructions.pop(0).rstrip()
instructions.pop(0)

map_dict = {}
begin_points = []
for instruction in instructions:
    root, left, right = re.search(
        r"([1-9A-Z]*) = \(([1-9A-Z]*), ([1-9A-Z]*)\)", instruction
    ).groups()
    map_dict[root + " L"] = left
    map_dict[root + " R"] = right

    if root.endswith("A"):
        begin_points.append(root)

position_points = copy.deepcopy(begin_points)

j = 0
position_memory = {position: [] for position in position_points}

while not all([point.endswith("Z") for point in position_points]):
    left_or_right = commands[j % len(commands)]
    for i, point in enumerate(position_points):
        point = map_dict[point + " " + left_or_right]
        position_points[i] = point
        if point.endswith("Z"):
            position_memory[begin_points[i]].append(j + 1)
    j += 1

    if all([len(position_list) > 50 for position_list in position_memory.values()]):
        break

diff_dict = {
    position: [y - x for (x, y) in itertools.pairwise(position_list[:-20])]
    for position, position_list in position_memory.items()
}

print(math.lcm(*[diff[0] for diff in diff_dict.values()]))
