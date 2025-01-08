import math
import itertools
from collections import defaultdict
import pathlib


def mix(nb1: int, nb2: int) -> int:
    return nb1 ^ nb2


def prune(secret_nb: int) -> int:
    return secret_nb % 16777216


def hash(secret_nb: int) -> int:
    secret_nb = mix(secret_nb * 64, secret_nb)
    secret_nb = prune(secret_nb)

    secret_nb = mix(math.floor(secret_nb / 32), secret_nb)
    secret_nb = prune(secret_nb)

    secret_nb = mix(secret_nb * 2048, secret_nb)
    secret_nb = prune(secret_nb)

    return secret_nb


def solve(instruction_list, part=1):
    all_secret_nb_seq = []
    res_part1 = []
    for instruction in instruction_list:
        nb = int(instruction.strip())
        buyer_sn = [nb]
        for _ in range(2000):
            nb = hash(nb)
            buyer_sn.append(nb)

        res_part1.append(nb)
        all_secret_nb_seq.append(buyer_sn)

    if part == 1:
        return sum(res_part1)

    all_diffs = []
    for secret_nb_seq in all_secret_nb_seq:
        all_diffs.append(
            [0]
            + [
                int(str(nb2)[-1]) - int(str(nb1)[-1])
                for nb1, nb2 in itertools.pairwise(secret_nb_seq)
            ]
        )

    four_seq_mem = defaultdict(int)
    for secret_nb_seq, diff_seq in zip(all_secret_nb_seq, all_diffs):
        tmp_mem = {}
        for i in range(len(diff_seq) - 3):
            searched_seq = (
                diff_seq[i],
                diff_seq[i + 1],
                diff_seq[i + 2],
                diff_seq[i + 3],
            )
            if searched_seq not in tmp_mem:
                four_seq_mem[searched_seq] += int(str(secret_nb_seq[i + 3])[-1])
                tmp_mem[searched_seq] = True

    return max(four_seq_mem.values())


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
