import pathlib


def part1(instruction_list) -> int:
    total = 0

    for nbs_str in instruction_list:
        nbs_str = nbs_str.strip()
        first_nb_list: list[int] = [int(i) for i in nbs_str[: len(nbs_str) - 1]]
        max_first_int: int = max(first_nb_list)
        idx_max_first_int: int = first_nb_list.index(max_first_int)
        max_second_int: int = max(
            [int(i) for i in nbs_str[idx_max_first_int + 1 : len(nbs_str)]]
        )

        total += int(str(max_first_int) + str(max_second_int))

    return total


def part2(instruction_list) -> int:
    total = 0
    NB_DIGITS = 12

    for nbs_str in instruction_list:
        nbs_str = nbs_str.strip()
        idx_list = NB_DIGITS * [-1]

        for nb in range(0, NB_DIGITS):
            n_digit_list: list[int] = [
                int(i)
                for i in nbs_str[idx_list[nb] + 1 : len(nbs_str) - (NB_DIGITS - nb - 1)]
            ]
            max_n_digit: int = max(n_digit_list)
            idx_max_n_int: int = n_digit_list.index(max_n_digit) + idx_list[nb] + 1
            idx_list = idx_list[:nb] + (NB_DIGITS - nb) * [idx_max_n_int]

        final_int = int("".join([nbs_str[digit_idx] for digit_idx in idx_list]))
        total += final_int

    return total


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
