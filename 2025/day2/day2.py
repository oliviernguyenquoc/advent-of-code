import pathlib


def _parse_data(data: str) -> list[tuple[str, str]]:
    intervals: list[tuple[str, str]] = []

    for instruction in data.split(","):
        min_range_str, max_range_str = instruction.split("-")
        intervals.append((min_range_str.strip(), max_range_str.strip()))

    return intervals


def get_invalid_ids(
    intervals: list[tuple[str, str]], repetition_len: int = 2
) -> set[int]:
    invalid_ids = set()

    for min_interval, max_interval in intervals:
        if len(max_interval) < repetition_len:
            continue

        # Ensure the number of digits is a multiple of repetition_len
        # Round up to the next power of 10 that satisfies this condition
        if len(min_interval) % repetition_len != 0:
            min_interval = str(
                10 ** (((len(min_interval) // repetition_len + 1) * repetition_len) - 1)
            )

        # Round down to the previous power of 10 that satisfies this condition
        if len(max_interval) % repetition_len != 0:
            max_interval = str(
                10 ** ((len(max_interval) // repetition_len) * repetition_len) - 1
            )

        if int(min_interval) > int(max_interval):
            continue

        min_first_half_digits = int(min_interval[: len(min_interval) // repetition_len])
        max_first_half_digits = int(max_interval[: len(max_interval) // repetition_len])

        for digits in range(min_first_half_digits, max_first_half_digits + 1):
            invalid_id_condidate = int(repetition_len * str(digits))
            if int(min_interval) <= invalid_id_condidate <= int(max_interval):
                invalid_ids.add(invalid_id_condidate)

    return invalid_ids

"""
def part1(instruction_list) -> int:
    intervals = _parse_data(instruction_list[0])

    invalid_ids = get_invalid_ids(intervals)

    return sum(invalid_ids)
"""

def part1(instruction_list) -> int:
    intervals = _parse_data(instruction_list[0])

    invalid_ids = set()
    for min_interval, max_interval in intervals:
        # We ensure that the number of digits is even
        if len(min_interval) % 2 == 1:
            min_interval = str(10 ** (len(min_interval)))

        if len(max_interval) % 2 == 1:
            max_interval = str(10 ** (len(max_interval) - 1) - 1)

        if int(min_interval) > int(max_interval):
            continue

        min_first_half_digits = int(min_interval[: len(min_interval) // 2])
        max_first_half_digits = int(max_interval[: len(max_interval) // 2])

        for digits in range(min_first_half_digits, max_first_half_digits + 1):
            invalid_id_condidate = int(str(digits) + str(digits))
            if int(min_interval) <= invalid_id_condidate <= int(max_interval):
                invalid_ids.add(invalid_id_condidate)

    return sum(invalid_ids)


def part2(instruction_list) -> int:
    intervals = _parse_data(instruction_list[0])
    invalid_ids = set()

    max_int = max(intervals, key=lambda tpl: tpl[1])[1]

    for repetition_len in range(2, len(max_int)+1):
        invalid_ids |= get_invalid_ids(intervals, repetition_len=repetition_len)

    return sum(invalid_ids)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
    # 50850548984 too low
