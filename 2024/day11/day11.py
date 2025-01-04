from collections import Counter
import pathlib


def blink(nb_counter: Counter) -> Counter:
    tmp_counter = Counter()
    for nb, count in nb_counter.items():
        if count == 0:
            continue

        if nb == "0":
            tmp_counter["1"] += nb_counter[nb]
        elif len(nb) % 2 == 0:
            tmp_counter[str(int(nb[: len(nb) // 2]))] += nb_counter[nb]
            tmp_counter[str(int(nb[len(nb) // 2 :]))] += nb_counter[nb]
        else:
            tmp_counter[str(int(nb) * 2024)] += nb_counter[nb]

    return tmp_counter


def solve(instruction_list, part=1):
    if part == 1:
        NB_BLINKS = 25
    else:
        NB_BLINKS = 75

    nb_counter = Counter(instruction_list[0].strip().split(" "))

    len_nb_list = []

    for j in range(NB_BLINKS):
        nb_counter = blink(nb_counter)
        len_nb_list.append(len(nb_counter.keys()))

    print(f"Part {part}: {sum(nb_counter.values())}")
    return sum(nb_counter.values())


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    solve(instruction_list, part=1)
    solve(instruction_list, part=2)
