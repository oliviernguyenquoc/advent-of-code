import pathlib

def solve(instruction_list, part):
    total_part1, total_part2 = 0, 0
    for instruction in instruction_list:
        derivation = [[int(k) for k in instruction.strip().split()]]
        i = 0
        while any([nb != 0 for nb in derivation[i]]):
            derivation.append(
                [x - derivation[i][k - 1] for k, x in enumerate(derivation[i])][1:]
            )
            i += 1

        # Part 1
        tmp = 0
        for i in range(len(derivation) - 1, -1, -1):
            tmp += derivation[i][-1]
        total_part1 += tmp

        # Part 2
        tmp = 0
        for i in range(len(derivation) - 1, -1, -1):
            tmp = derivation[i][0] - tmp

        total_part2 += tmp

    if part == 1:
        return total_part1
    else:
        return total_part2


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()
    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
