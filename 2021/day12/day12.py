from typing import List, Tuple
import copy

with open("./day12/input.txt") as f:
    instruction_list = f.read().splitlines()

path_tuple_list: List[Tuple[str, str]] = []

for instruction in instruction_list:
    path_tuple_list.append(tuple(instruction.split("-")))

path_tuple_list += [(path_tuple[1], path_tuple[0]) for path_tuple in path_tuple_list]

all_path_list: List[List[str]] = [
    list(start_tuple) for start_tuple in path_tuple_list if start_tuple[0] == "start"
]
old_all_path_list: List[List[str]] = []

while old_all_path_list != all_path_list:
    old_all_path_list = copy.deepcopy(all_path_list)

    for path in all_path_list:
        for path_tuple in path_tuple_list:
            if path[-1] == "end":
                break
            if (
                path_tuple[1] != "start"
                and path_tuple[0] == path[-1]
                and (path_tuple[1].isupper() or path_tuple[1] not in path)
                and path + [path_tuple[1]] not in all_path_list
            ):
                all_path_list.append(copy.deepcopy(path))
                path.append(path_tuple[1])
        if path[-1] == "end":
            continue

all_path_list = [path for path in all_path_list if path[-1] == "end"]

# print(path_tuple_list)
# print(all_path_list)
print(len(all_path_list))
