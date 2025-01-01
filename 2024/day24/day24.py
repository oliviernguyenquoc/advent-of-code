import re
import itertools
import copy
import tqdm

# import graphviz
import random


class InfiniteLoopError(Exception):
    pass


def get_operations_results(
    instruct_list: list[tuple[str, str, str, str]], bit_dict: dict[str, int]
):
    iteration_limit = 10000
    iteration_count = 0

    instruct_tmp = copy.deepcopy(instruct_list)
    while instruct_tmp:
        iteration_count += 1
        if iteration_count > iteration_limit:
            # print("Infinite loop detected!")
            # print(f"Remaining instructions length: {len(instruct_tmp)}")
            raise InfiniteLoopError()

        bit1, op, bit2, bit_res = instruct_tmp.pop(0)
        if bit1 not in bit_dict or bit2 not in bit_dict:
            instruct_tmp.append((bit1, op, bit2, bit_res))
            continue

        match op:
            case "AND":
                bit_dict[bit_res] = bit_dict[bit1] & bit_dict[bit2]
            case "OR":
                bit_dict[bit_res] = bit_dict[bit1] | bit_dict[bit2]
            case "XOR":
                bit_dict[bit_res] = bit_dict[bit1] ^ bit_dict[bit2]
            case _:
                raise Exception("No known ops found")

    return bit_dict


def compute_number(bit_dict: dict[str, int], letter: str = "z"):
    sub_dict = {k: v for k, v in bit_dict.items() if k[0] == letter}

    res_txt = "".join(
        [str(sub_dict[bit]) for bit in sorted(sub_dict.keys(), reverse=True)]
    )

    return int(res_txt, 2)


def swap(
    instruct_list: list[tuple[str, str, str, str]],
    instruct_to_swap1: tuple[str, str, str, str],
    instruct_to_swap2: tuple[str, str, str, str],
) -> list[tuple[str, str, str, str]]:
    instruct_list.remove(instruct_to_swap1)
    instruct_list.remove(instruct_to_swap2)

    instruct_list += [
        (
            instruct_to_swap1[0],
            instruct_to_swap1[1],
            instruct_to_swap1[2],
            instruct_to_swap2[3],
        ),
        (
            instruct_to_swap2[0],
            instruct_to_swap2[1],
            instruct_to_swap2[2],
            instruct_to_swap1[3],
        ),
    ]

    return instruct_list


# We have to respect 2 criteria to correct this "Ripple-carry adder":
# If output instruct is a z door, operation should be XOR (except the last bit)
# If output instruct is NOT a z door and the inputs are not x, y, operation must be a AND or a OR (not de XOR)


def generate_combinations(instruct_list_init):
    # Identification des listes rule1 et rule2
    rule1_list = [
        instruct
        for instruct in instruct_list_init
        if instruct[3][0] == "z" and instruct[1] != "XOR" and instruct[3] != "z45"
    ]

    rule2_list = [
        instruct
        for instruct in instruct_list_init
        if instruct[3][0] != "z"
        and instruct[0][0] not in ("x", "y")
        and instruct[2][0] not in ("x", "y")
        and instruct[1] == "XOR"
    ]

    print(f"Rule 1 violations: {len(rule1_list)}")
    print(f"Rule 2 violations: {len(rule2_list)}")

    # rule_combinations = list(itertools.product(rule1_list, rule2_list))
    # all_rules_combinations = [
    #     ((a, b), (c, d), (e, f))
    #     for (a, b) in rule_combinations
    #     for (c, d) in rule_combinations
    #     for (e, f) in rule_combinations
    #     if len({a, c, e}) == 3 and len({b, d, f}) == 3
    # ]

    # By inspecting XOR ouput i got this combination:
    winning_combination = (
        (("dsk", "OR", "ptc", "z09"), ("mnm", "XOR", "gqb", "gwh")),
        (("kgk", "AND", "sbs", "z21"), ("kgk", "XOR", "sbs", "rcb")),
        (("x39", "AND", "y39", "z39"), ("wjf", "XOR", "ksf", "jct")),
    )

    z_list = [inst[3] for inst in rule1_list + rule2_list]
    instruct_list_no_rules = [
        inst for inst in instruct_list_init if inst[3] not in z_list
    ]
    instruct_combinations = list(
        itertools.product(
            instruct_list_no_rules,
            instruct_list_no_rules,
        )
    )

    all_combinations = [
        (*winning_combination, (a, b)) for a, b in instruct_combinations if a != b
    ]

    return all_combinations


with open("./2024/day24/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

bit_dict_init = {}

instruction = instruction_list.pop(0)

while instruction != "\n":
    bit_name, bit_nb = re.search(r"([a-z0-9]+): (\d+)", instruction).groups()
    bit_dict_init[bit_name] = int(bit_nb)
    instruction = instruction_list.pop(0)

instruct_list_init = []
while instruction_list:
    instruction = instruction_list.pop(0)
    bit1, op, bit2, bit_res = re.search(
        r"([a-z0-9]+) (XOR|OR|AND) ([a-z0-9]+) -> ([a-z0-9]+)", instruction
    ).groups()
    instruct_list_init.append((bit1, op, bit2, bit_res))

# print(len(instruct_list))
bit_dict = copy.deepcopy(bit_dict_init)
bit_dict = get_operations_results(instruct_list_init, bit_dict)
z = compute_number(bit_dict, "z")


print(f"Part 1: {z}")

all_combinations = generate_combinations(instruct_list_init)

last_swap_combinations_to_test = set()
for swap_combination in tqdm.tqdm(all_combinations):
    bit_dict = copy.deepcopy(bit_dict_init)

    swapped_instruct_list = copy.deepcopy(instruct_list_init)

    all_rules = set()
    for rule1_gate, rule2_gate in swap_combination:
        swapped_instruct_list = swap(swapped_instruct_list, rule1_gate, rule2_gate)

    try:
        bit_dict = get_operations_results(swapped_instruct_list, bit_dict)
    except InfiniteLoopError:
        continue

    z = compute_number(bit_dict, "z")
    x = compute_number(bit_dict, "x")
    y = compute_number(bit_dict, "y")

    # Check if result is correct with current bit initialization
    if bin(x + y) == bin(z):  # Remplacez par la valeur attendue si connue
        print(
            f"Possible solution found : {",".join(sorted([wires[3] for swap_found in swap_combination for wires in swap_found ]))}"
        )
        last_swap_combinations_to_test.add(swap_combination)
        continue
    # else:
    #     print("----")
    #     print(swap_combination)
    #     print(
    #         f"x: {x}, y: {y}, \n x+y: {bin(x+y)}, \n z:   {bin(z)}, \n XOR:    {bin((x+y)^z)}"
    #     )

for swap_combination in last_swap_combinations_to_test:
    good_combination = True
    for i in range(6):
        bit_dict_init_tmp = copy.deepcopy(bit_dict_init)
        # Let's try different combination
        for bit in bit_dict_init_tmp.keys():
            bit_dict_init_tmp[bit] = random.choice([0, 1])

        swapped_instruct_list = copy.deepcopy(instruct_list_init)
        for rule1_gate, rule2_gate in swap_combination:
            swapped_instruct_list = swap(swapped_instruct_list, rule1_gate, rule2_gate)

        bit_dict = get_operations_results(swapped_instruct_list, bit_dict_init_tmp)

        z = compute_number(bit_dict, "z")
        x = compute_number(bit_dict, "x")
        y = compute_number(bit_dict, "y")

        if bin(x + y) != bin(z):
            good_combination = False
            break

    if good_combination:
        print("Good combination")
        print(
            f"Part 2: {",".join(sorted([wires[3] for swap_found in swap_combination for wires in swap_found ]))}"
        )
