import math
from typing import List


def chinese_remainder(n: List[int], a: List[int]):
    sum_total = 0
    prod = math.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum_total += a_i * modular_multiplicative_inverse(p, n_i) * p
    return sum_total % prod


def modular_multiplicative_inverse(a: int, m: int) -> int:
    # ref: https://docs.python.org/3/whatsnew/3.8.html
    return pow(a, -1, m)


f = open("./day13/input.txt")

instruction_list = f.readlines()

departure = int(instruction_list[0])
bus_list = instruction_list[1].split(",")

print(bus_list)
bus_id_dict = {
    int(bus_id): int(bus_id) - i for i, bus_id in enumerate(bus_list) if bus_id != "x"
}

max_bus_id = max(bus_id_dict)
idx_max_bus_id = bus_id_dict[max_bus_id]

print(max_bus_id, idx_max_bus_id)

print(list(bus_id_dict.keys()), list(bus_id_dict.values()))
print(chinese_remainder(list(bus_id_dict.keys()), list(bus_id_dict.values())))

f.close()