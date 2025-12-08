import pathlib


def _parse_date(instruction_list) -> tuple[list[tuple[int, int]], list[int]]:
    ranges: list[tuple[int, int]] = []
    ingredient_list: list[int] = []

    for instruction in instruction_list:
        if instruction == "\n":
            continue
        elif "-" in instruction:
            min_id_str, max_id_str = instruction.strip().split("-")
            ranges.append((int(min_id_str), int(max_id_str)))
        else:
            ingredient_list.append(int(instruction.strip()))

    return ranges, ingredient_list


def part1(instruction_list) -> int:
    ranges, ingredient_list = _parse_date(instruction_list)

    nb_fresh_ingredient = 0
    for ingredient in ingredient_list:
        if any([min_id <= ingredient <= max_id for min_id, max_id in ranges]):
            nb_fresh_ingredient += 1

    return nb_fresh_ingredient


def part2(instruction_list) -> int:
    ranges, _ = _parse_date(instruction_list)
    ranges.sort()

    merged_ranges: list[tuple[int, int]] = [ranges[0]]

    for min_id, max_id in ranges[1:]:
        previous_min, previous_max = merged_ranges.pop()
        if previous_min <= min_id <= previous_max:
            merged_ranges.append((previous_min, max(previous_max, max_id)))
        else:
            merged_ranges.append((previous_min, previous_max))
            merged_ranges.append((min_id, max_id))

    return sum([max_id - min_id + 1 for min_id, max_id in merged_ranges])


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
