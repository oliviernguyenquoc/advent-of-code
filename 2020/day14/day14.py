"""Solution with lists"""

import itertools
import re
from typing import Dict, List


def _replace_fixed_bits(mask_dict: Dict[int, str], bit_value: str) -> int:
    for i, bit in mask_dict.items():
        if i <= len(bit_value) - 2:
            if i == 0:
                bit_value = bit_value[: -i - 1] + bit
            else:
                bit_value = bit_value[: -i - 1] + bit + bit_value[-i:]

    return bit_value


def modify_bits_part1(mask: str, bit_value: str) -> int:

    mask_dict = {
        len(mask) - i - 1: bit for i, bit in enumerate(mask) if bit in ["0", "1"]
    }
    bit_value = _replace_fixed_bits(mask_dict, bit_value)

    if len(mask) > len(bit_value) - 2:
        bit_value = (
            "0b"
            + mask[: len(mask) - (len(bit_value) - 2)].replace("X", "0")
            + bit_value[2:]
        )

    return int(bit_value, 2)


def modify_bits_part2(mask: str, bit_value: str) -> List[int]:
    mask_dict_1 = {len(mask) - i - 1: bit for i, bit in enumerate(mask) if bit == "1"}
    mask_dict_X = {len(mask) - i - 1: bit for i, bit in enumerate(mask) if bit == "X"}

    bit_value = _replace_fixed_bits(mask_dict_1, bit_value)

    possible_value_list = [bit_value]

    for i, bit in mask_dict_X.items():
        if i <= len(bit_value) - 2:
            temp_list = []
            for possible_value in possible_value_list:
                if i == 0:
                    temp_list += [
                        possible_value[: -i - 1] + "0",
                        possible_value[: -i - 1] + "1",
                    ]
                else:
                    temp_list += [
                        possible_value[: -i - 1] + "0" + possible_value[-i:],
                        possible_value[: -i - 1] + "1" + possible_value[-i:],
                    ]
            possible_value_list = temp_list

    root_possible_value_list = ["0b"]

    if len(mask) > len(bit_value) - 2:
        for i, bit in enumerate(mask):
            if i < len(mask) - (len(bit_value) - 2):
                if bit == "X":
                    temp_list = []
                    for root_possible_value in root_possible_value_list:
                        temp_list += [
                            root_possible_value + "0",
                            root_possible_value + "1",
                        ]
                    root_possible_value_list = temp_list
                else:
                    root_possible_value_list = [
                        root_possible_value + bit
                        for root_possible_value in root_possible_value_list
                    ]

    final_list = []
    for i, j in itertools.product(root_possible_value_list, possible_value_list):
        final_list.append(int(i + j[2:], 2))

    return final_list


f = open("./day14/input.txt")

instruction_list = f.readlines()

mask = ""
mem_part1 = {}
mem_part2 = {}

for instruction in instruction_list:
    if "mask = " in instruction:
        mask = re.findall(r"mask = ([0-9X]*)", instruction)[0]
        print(mask)

    if "mem" in instruction:
        mem_instruction = re.findall(r"mem\[([0-9]*)\] = ([0-9]*)", instruction)[0]
        memory = int(mem_instruction[0])
        value = int(mem_instruction[1])

        print(memory, bin(int(value)))

        mem_part1[memory] = modify_bits_part1(mask, bin(int(value)))

        memory_list = modify_bits_part2(mask, bin(int(memory)))
        for i in memory_list:
            mem_part2[i] = value

print(len(mem_part1))
print(f"Part 1 : {sum(mem_part1.values())}")

print(len(mem_part2))
print(f"Part 2 : {sum(mem_part2.values())}")

f.close()
