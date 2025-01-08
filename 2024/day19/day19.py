import pathlib


def is_stripes_possible(stripes_to_find: str, towel_stock: set[str]) -> bool:
    if stripes_to_find == "":
        return True
    for towel in towel_stock:
        if stripes_to_find[: len(towel)] == towel:
            if is_stripes_possible(stripes_to_find[len(towel) :], towel_stock):
                return True

    return False


def part1(instruction_list):
    towel_stock = set(instruction_list.pop(0).strip().split(", "))

    # Skip empty line
    instruction_list.pop(0)

    total = 0
    for instruction in instruction_list:
        stripes_to_find = instruction.strip()

        if is_stripes_possible(stripes_to_find, towel_stock):
            total += 1

    return total


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
