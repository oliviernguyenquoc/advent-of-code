def check_if_adjacent(instructions: list[str], row_number: int, i: int, j: int) -> bool:
    # Check left side
    if i > 0:
        if instructions[row_number][i - 1] != ".":
            return True
        if row_number > 0 and instructions[row_number - 1][i - 1] != ".":
            return True
        if (
            row_number < len(instructions) - 1
            and instructions[row_number + 1][i - 1] != "."
        ):
            return True

    # Check right side
    if j < len(instructions[row_number]) - 1:
        if instructions[row_number][j + 1] != ".":
            return True
        if row_number > 0 and instructions[row_number - 1][j + 1] != ".":
            return True
        if (
            row_number < len(instructions) - 1
            and instructions[row_number + 1][j + 1] != "."
        ):
            return True

    # Check above
    if row_number > 0 and any(
        [instructions[row_number - 1][k] != "." for k in range(i, j + 1)]
    ):
        return True

    # Check bellow
    if row_number < len(instructions) - 1 and any(
        [instructions[row_number + 1][k] != "." for k in range(i, j + 1)]
    ):
        return True

    return False


def part1(instructions: list[str]) -> int:
    instructions = [instruction.strip() for instruction in instructions]

    all_adjacent_numbers: list[int] = []

    for row_number, instruction in enumerate(instructions):
        begin, end = 0, 0
        while end < len(instruction) or begin != end:
            # Case we detect a number
            if end < len(instruction) and instruction[end].isdigit():
                end += 1

            # End of a number
            elif begin != end or end == len(instruction):
                is_adjacent = check_if_adjacent(
                    instructions, row_number, begin, end - 1
                )
                if is_adjacent and instruction[begin:end].isdigit():
                    all_adjacent_numbers.append(int(instruction[begin:end]))
                begin = end

            #  No number
            else:
                begin += 1
                end += 1

    return sum(all_adjacent_numbers)


if __name__ == "__main__":
    with open("./day3/input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()
    print(f"Part 1: {part1(instruction_list)}")
