from collections import defaultdict

with open("./day1/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

list1, list2 = [], []
for instruction in instruction_list:
    nb1, nb2 = instruction.split()
    list1.append(int(nb1))
    list2.append(int(nb2))

list1.sort()
list2.sort()

# Part 1
distance = 0
for nb1, nb2 in zip(list1, list2):
    distance += max(nb1, nb2) - min(nb1, nb2)

print(f"Part 1: {distance}")

# Part 2
nb_freq_dict: dict[int, int] = defaultdict(int)
for i in list2:
    nb_freq_dict[i] += 1

total = 0
for i in list1:
    total += (nb_freq_dict[i] * i)

print(f"Part 2: {total}")
