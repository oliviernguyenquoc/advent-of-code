import pathlib


def part2(arr):
    # Can't x > 1010 to fullfill a*x = 2020 with a > 1
    arr = [int(nb) for nb in arr]

    print(len(arr))

    for i in arr:
        for j in arr:
            for k in arr:
                if i + j + k == 2020 and i != j and j != k:
                    break
            if i + j + k == 2020 and i != j and j != k:
                break
        if i + j + k == 2020 and i != j and j != k:
            break

    print((i, j, k))
    return i * j * k


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
