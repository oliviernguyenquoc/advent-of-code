import pathlib


def part1(instruction_list):
    max_weight: int = 0
    current_elf_weight: int = 0
    for instruction in instruction_list:
        if instruction != "":
            current_elf_weight += int(instruction)
        else:
            if max_weight < current_elf_weight:
                max_weight = current_elf_weight
            current_elf_weight = 0

    return max_weight


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
