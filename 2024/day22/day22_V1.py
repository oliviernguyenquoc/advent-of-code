import math
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


def part1(instruction_list):
    res = []
    for instruction in instruction_list:
        nb = int(instruction.strip())
        for _ in range(2000):
            nb = hash(nb)

        res.append(nb)

    return sum(res)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
