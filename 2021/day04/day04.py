import pathlib


def generate_lists_from_scoreboard(instruction_list) -> list[list[set[str]]]:
    card_list = []
    new_card: list[set[str]] = [set() for i in range(5)]

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


def part1(instruction_list):
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

    total_sum = sum([int(nb_str) for nb_set in winning_card for nb_str in nb_set])

    print(total_sum // 2)
    print(int(bingo_numbers[bingo_idx]))
    return total_sum * int(bingo_numbers[bingo_idx]) // 2


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
