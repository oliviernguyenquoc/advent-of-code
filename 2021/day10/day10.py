import pathlib


def part1(instruction_list):
    illegal_char = []
    points_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
    char_dict = {")": "(", "]": "[", ">": "<", "}": "{"}

    for instruction in instruction_list:
        char_list = []
        for char in instruction:
            if char in char_dict.values():
                char_list.append(char)
            elif char in char_dict:
                if char_list[-1] != char_dict[char]:
                    illegal_char.append(char)
                    break
                else:
                    char_list = char_list[:-1]

    print(illegal_char)
    print([points_dict[char] for char in illegal_char])
    return sum([points_dict[char] for char in illegal_char])


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
