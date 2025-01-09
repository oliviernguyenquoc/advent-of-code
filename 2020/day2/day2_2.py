import pathlib


def part2(instruction_list):
    total_true_password = 0

    for arr in instruction_list:
        min_letter, max_letter = map(int, arr[0].split("-"))
        letter = arr[1][0]
        password = arr[2]
        print((min_letter, max_letter, letter, password))
        if (password[min_letter - 1] == letter) != (password[max_letter - 1] == letter):
            total_true_password += 1
            print("true")

    return total_true_password


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
