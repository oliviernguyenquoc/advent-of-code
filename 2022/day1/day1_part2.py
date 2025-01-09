import pathlib


def part2(instruction_list):
    max_weight_list: list[int] = [0, 0, 0]
    current_elf_weight: int = 0

    for instruction in instruction_list:
        if instruction != "":
            current_elf_weight += int(instruction)
        else:
            if max_weight_list[0] < current_elf_weight:
                max_weight_list[0] = current_elf_weight
                max_weight_list.sort()
            current_elf_weight = 0

    return sum(max_weight_list)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
