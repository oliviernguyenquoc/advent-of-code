import itertools
from collections import defaultdict


def get_strength(hand: str) -> int:
    letter_dict = defaultdict(int)
    for letter in hand:
        letter_dict[letter] += 1

    nb_pairs = 0
    have_triple = False
    for value in letter_dict.values():
        match value:
            case 5:
                return 5
            case 4:
                return 4
            case 3:
                have_triple = True
            case 2:
                nb_pairs += 1
            case _:
                continue

    if have_triple and nb_pairs == 1:
        return 3
    elif have_triple and nb_pairs == 0:
        return 2
    elif nb_pairs == 2:
        return 1
    elif nb_pairs == 1:
        return 0
    else:
        return -1


def get_card_strength(letter: str) -> int:
    match letter:
        case "A":
            return 14
        case "K":
            return 13
        case "Q":
            return 12
        case "J":
            return 0
        case "T":
            return 10
        case _:
            return int(letter)


def is_better(hand1: str, hand2: str) -> bool:
    if "J" in hand1:
        strength_1 = -10
        for i in "AKQT98765432":
            strength_1 = max(get_strength(hand1.replace("J", i)), strength_1)
    else:
        strength_1 = get_strength(hand1)

    if "J" in hand2:
        strength_2 = -10
        for i in "AKQT98765432":
            strength_2 = max(get_strength(hand2.replace("J", i)), strength_2)
    else:
        strength_2 = get_strength(hand2)

    if strength_1 != strength_2:
        return strength_1 > strength_2

    i = 0
    while i < len(hand1):
        if hand1[i] != hand2[i]:
            return get_card_strength(hand1[i]) > get_card_strength(hand2[i])
        else:
            i += 1

    raise Exception("Ohoh")


def part2(instructions):
    hands = []
    bid_dict = {}

    for instruction in instructions:
        hand, bid = instruction.split()
        hands.append(hand)
        bid_dict[hand] = int(bid)

    point_dict: dict[str, int] = {hand: 0 for hand in hands}

    for hand1, hand2 in itertools.combinations(hands, 2):
        if is_better(hand1, hand2):
            # print(f"{hand1} > {hand2}")
            point_dict[hand1] += 1
        else:
            # print(f"{hand1} < {hand2}")
            point_dict[hand2] += 1

    total = 0
    i = 1

    for hand, value in sorted(point_dict.items(), key=lambda x: x[1]):
        total += bid_dict[hand] * i
        i += 1

    return total


if __name__ == "__main__":
    with open("./day7/input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
