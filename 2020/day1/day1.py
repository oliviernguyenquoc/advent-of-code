import pathlib


def part1(arr):
    # Can't x > 1010 to fullfill a*x = 2020 with a > 1
    arr = [int(nb) for nb in arr]

    print(len(arr))
    # print(arr)

    for i in arr:
        for j in arr:
            if i + j == 2020 and i != j:
                break
        if i + j == 2020 and i != j:
            break

    print((i, j))
    return i * j


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
