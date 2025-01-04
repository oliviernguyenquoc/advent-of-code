from typing import List, Set

with open("./day04/input.txt") as f:
    instruction_list = f.read().splitlines()


def generate_lists_from_scoreboard(instruction_list) -> List[List[Set[str]]]:
    card_list = []
    new_card: List[Set[str]] = [set() for i in range(5)]

    for idx_instruction, instruction in enumerate(instruction_list):
        if instruction == "":
            new_card += [
                set(inst.split())
                for inst in instruction_list[idx_instruction - 5 : idx_instruction]
            ]
            card_list.append(new_card)
            new_card = [set() for i in range(5)]
        else:
            for position, number in enumerate(instruction.split()):
                new_card[position].add(number)

    new_card += [set(inst.split()) for inst in instruction_list[-5:]]
    card_list.append(new_card)

    return card_list


card_list = generate_lists_from_scoreboard(instruction_list[2:])

stop: bool = False

card_to_delete: List[int] = []
bingo_numbers: List[str] = instruction_list[0].split(",")

for bingo_idx, actual_nb in enumerate(bingo_numbers):
    for card_idx, card in enumerate(card_list):
        if card_idx in card_to_delete:
            continue
        for nb_set_idx, nb_set in enumerate(card):
            if len(nb_set - set(bingo_numbers[: bingo_idx + 1])) == 0:
                stop = True
                break
        if stop:
            card_to_delete.append(card_idx)
            stop = False
            if len(card_to_delete) == len(card_list):
                break
            else:
                continue
    if len(card_to_delete) == len(card_list):
        break

card_idx = card_to_delete[-1]
losing_card = card_list[card_idx]
losing_card = [card - set(bingo_numbers[: bingo_idx + 1]) for card in losing_card]

sum_nb = sum([int(nb_str) for nb_set in losing_card for nb_str in nb_set])

print(sum_nb // 2)
print(f"Number N°{bingo_idx}: {int(bingo_numbers[bingo_idx])}")
print(sum_nb * int(bingo_numbers[bingo_idx]) // 2)
