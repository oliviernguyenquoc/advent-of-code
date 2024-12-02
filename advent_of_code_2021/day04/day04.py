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

bingo_numbers = instruction_list[0].split(",")

for bingo_idx, actual_nb in enumerate(bingo_numbers):
    for card_idx, card in enumerate(card_list):
        for nb_set_idx, nb_set in enumerate(card):
            if len(nb_set - set(bingo_numbers[: bingo_idx + 1])) == 0:
                stop = True
                break
        if stop:
            break
    if stop:
        break

winning_card = card_list[card_idx]
winning_card = [card - set(bingo_numbers[: bingo_idx + 1]) for card in winning_card]

print(card_idx, nb_set_idx)
print(winning_card)
print(card_list[card_idx][nb_set_idx])

sum = sum([int(nb_str) for nb_set in winning_card for nb_str in nb_set])

print(sum // 2)
print(int(bingo_numbers[bingo_idx]))
print(sum * int(bingo_numbers[bingo_idx]) // 2)
