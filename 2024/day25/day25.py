import itertools

with open("./2024/day25/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

key_list = []
lock_list = []
for batch in itertools.batched(instruction_list, 8):
    heights = [0, 0, 0, 0, 0]
    for y in range(7):
        for x in range(5):
            if batch[y][x] == "#":
                heights[x] += 1
    # key
    if batch[0].strip() == "#####":
        key_list.append(heights)
    # lock
    else:
        lock_list.append(heights)

nb_match = 0
for key, lock in itertools.product(key_list, lock_list):
    if all([key[i] + lock[i] <= 7 for i in range(5)]):
        nb_match += 1

print(f"Part 1: {nb_match}")
