with open("./day1/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

# Part 2

DIGITS_IN_LETTER = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

REVERSE_DIGIT = {
    digit_str[::-1]: digit for digit_str, digit in DIGITS_IN_LETTER.items()
}


def extract_digit(characters: str, digit_dict: dict[str, int]) -> int:
    i = 0

    while i < len(characters):
        # Check if real digit
        if characters[i].isdigit():
            return int(characters[i])

        # Check if digit in letters
        for digit_str, digit in digit_dict.items():
            if i + len(digit_str) <= len(characters):
                sub_characters = characters[i : i + len(digit_str)]
                if sub_characters == digit_str:
                    return digit
        i += 1

    raise Exception("Weird")


all_digit_list = []
for instruction in instruction_list:
    first_digit = extract_digit(instruction, DIGITS_IN_LETTER)
    second_digit = extract_digit(instruction[::-1], REVERSE_DIGIT)

    all_digit_list.append(int(str(first_digit) + str(second_digit)))

print(sum(all_digit_list))
