""" Version 2 with formal bits operation: Much better !"""

import re
from typing import List


def modify_bits_part1(mask: str, bit_value: str) -> int:

    bit_level = 0

    for bit in reversed(mask):
        if bit in ["0", "1"]:
            last_bit = bit_value >> bit_level
            if (last_bit & 0b1) != int(bit, 2):
                if (last_bit & 0b1) == 0b0:
                    bit_value += 2 ** bit_level
                else:
                    bit_value -= 2 ** bit_level

        bit_level += 1

    return bit_value


def modify_bits_part2(mask: str, bit_value: str) -> List[int]:

    bit_level = 0
    possible_value_list = [bit_value]

    for bit in reversed(mask):

        if bit == "1":
            for i, possible_value in enumerate(possible_value_list):
                if ((possible_value >> bit_level) & 0b1) == 0b0:
                    possible_value_list[i] = possible_value + 2 ** bit_level

        if bit == "X":
            tmp_list = possible_value_list.copy()

            for possible_value in possible_value_list:
                if ((possible_value >> bit_level) & 0b1) == 0b0:
                    tmp_list.append(possible_value + 2 ** bit_level)
                else:
                    tmp_list.append(possible_value - 2 ** bit_level)

            possible_value_list = tmp_list

        bit_level += 1

    return possible_value_list


f = open("./day14/input.txt")

instruction_list = f.readlines()

mask = ""
mem_part1 = {}
mem_part2 = {}

for instruction in instruction_list:
    if "mask = " in instruction:
        mask = re.findall(r"mask = ([0-9X]*)", instruction)[0]

    if "mem" in instruction:
        mem_instruction = re.findall(r"mem\[([0-9]*)\] = ([0-9]*)", instruction)[0]
        memory = int(mem_instruction[0])
        value = int(mem_instruction[1])

        # Part 1
        mem_part1[memory] = modify_bits_part1(mask, value)

        # Part 2
        memory_list = modify_bits_part2(mask, memory)
        for i in memory_list:
            mem_part2[i] = value

print(len(mem_part1))
print(f"Part 1 : {sum(mem_part1.values())}")

print(len(mem_part2))
print(f"Part 2 : {sum(mem_part2.values())}")

f.close()
