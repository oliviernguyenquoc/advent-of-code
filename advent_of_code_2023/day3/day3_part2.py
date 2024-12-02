from collections import defaultdict
import math

with open("./day3/input.txt", encoding="utf-8") as f:
    instructions: list[str] = f.readlines()

instructions = [instruction.strip() for instruction in instructions]


def check_if_adjacent(
    instructions: list[str], row_number: int, i: int, j: int
) -> tuple[bool, int, int]:
    """
    Check if adjacent to a char (other than ".") and return its position
    """
    # Check left side
    if i > 0:
        if instructions[row_number][i - 1] != ".":
            return True, row_number, i - 1
        if row_number > 0 and instructions[row_number - 1][i - 1] != ".":
            return True, row_number - 1, i - 1
        if (
            row_number < len(instructions) - 1
            and instructions[row_number + 1][i - 1] != "."
        ):
            return True, row_number + 1, i - 1

    # Check right side
    if j < len(instructions[row_number]) - 1:
        if instructions[row_number][j + 1] != ".":
            return True, row_number, j + 1
        if row_number > 0 and instructions[row_number - 1][j + 1] != ".":
            return True, row_number - 1, j + 1
        if (
            row_number < len(instructions) - 1
            and instructions[row_number + 1][j + 1] != "."
        ):
            return True, row_number + 1, j + 1

    # Check above
    if row_number > 0 and any(
        [instructions[row_number - 1][k] != "." for k in range(i, j + 1)]
    ):
        for k in range(i, j + 1):
            if instructions[row_number - 1][k] != ".":
                return True, row_number - 1, k

    # Check bellow
    if row_number < len(instructions) - 1 and any(
        [instructions[row_number + 1][k] != "." for k in range(i, j + 1)]
    ):
        for k in range(i, j + 1):
            if instructions[row_number + 1][k] != ".":
                return True, row_number + 1, k

    return False, 0, 0


all_adjacent_numbers_dict: dict[tuple[int, int], list[int]] = defaultdict(list)

for row_number, instruction in enumerate(instructions):
    begin, end = 0, 0
    while end < len(instruction) or begin != end:
        # Case we detect a number
        if end < len(instruction) and instruction[end].isdigit():
            end += 1

        # End of a number
        elif begin != end or end == len(instruction):
            is_adjacent, x, y = check_if_adjacent(
                instructions, row_number, begin, end - 1
            )
            if (
                is_adjacent
                and instruction[begin:end].isdigit()
                and instructions[x][y] == "*"
            ):
                all_adjacent_numbers_dict[(x, y)].append(int(instruction[begin:end]))
            begin = end

        #  No number
        else:
            begin += 1
            end += 1

# print(all_adjacent_numbers_dict)
print(
    sum(
        [
            math.prod(couple_list)
            for couple_list in all_adjacent_numbers_dict.values()
            if len(couple_list) == 2
        ]
    )
)
