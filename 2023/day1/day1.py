import pathlib

def part1(instruction_list):
    all_digit_list = []
    for instruction in instruction_list:
        digit_tuple: list[str] = []
        for char in instruction:
            if char.isdigit():
                digit_tuple.append(char)
                break

        for char in instruction[::-1]:
            if char.isdigit():
                digit_tuple.append(char)
                break

        all_digit_list.append(int(digit_tuple[0] + digit_tuple[1]))

    return sum(all_digit_list)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
