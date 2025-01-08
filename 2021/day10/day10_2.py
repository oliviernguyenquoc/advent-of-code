import pathlib
import statistics


def part2(instruction_list):
    illegal_char = []
    POINTS_DICT = {")": 1, "]": 2, "}": 3, ">": 4}

    CHAR_DICT = {")": "(", "]": "[", ">": "<", "}": "{"}
    reverse_char_dict = {reverse_char: char for char, reverse_char in CHAR_DICT.items()}

    remaining_list = []

    for instruction in instruction_list:
        is_illegal_line: bool = False
        char_list = []
        for char in instruction:
            if char in CHAR_DICT.values():
                char_list.append(char)
            elif char in CHAR_DICT:
                if char_list[-1] != CHAR_DICT[char]:
                    illegal_char.append(char)
                    is_illegal_line = True
                    break
                else:
                    char_list = char_list[:-1]

        if not is_illegal_line:
            remaining_list.append([reverse_char_dict[char] for char in char_list[::-1]])

    score_list = []

    for remain_str in remaining_list:
        score = 0
        for char in remain_str:
            score *= 5
            score += POINTS_DICT[char]

        score_list.append(score)

    return statistics.median(score_list)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
