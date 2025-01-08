import tqdm
import pathlib


def part2(instruction_list):
    NB_STEP = 40

    polymere_template = instruction_list[0]

    receipes: dict[str, str] = {}

    for instruction in instruction_list[2:]:
        duo_letter, insertion_letter = instruction.split(" -> ")
        receipes[duo_letter] = insertion_letter

    two_step_receipes = {}
    for duo_letter, insertion_letter in receipes.items():
        two_step_receipes[duo_letter] = (
            duo_letter[0]
            + receipes[duo_letter[0] + insertion_letter]
            + insertion_letter
            + receipes[insertion_letter + duo_letter[1]]
        )

    # print(two_step_receipes)

    four_step_receipes = {}
    for duo_letter, insertion_letters in two_step_receipes.items():
        four_step_receipes[duo_letter] = (
            two_step_receipes[insertion_letters[:2]]
            + two_step_receipes[insertion_letters[1:3]]
            + two_step_receipes[insertion_letters[2:4]]
            + two_step_receipes[insertion_letters[3] + duo_letter[1]]
        )

    height_step_receipes = {}
    for duo_letter, insertion_letters in four_step_receipes.items():
        insertion_letter_for_height: str = ""
        for i in range(15):
            insertion_letter_for_height += four_step_receipes[
                insertion_letters[i : i + 2]
            ]

        insertion_letter_for_height += four_step_receipes[
            insertion_letters[15] + duo_letter[1]
        ]
        height_step_receipes[duo_letter] = insertion_letter_for_height

    for step in tqdm.tqdm(range(NB_STEP // 8)):
        new_polymere: str = ""
        for i in range(len(polymere_template) - 1):
            new_polymere += height_step_receipes[polymere_template[i : i + 2]]
        new_polymere += polymere_template[i + 1]
        polymere_template = new_polymere

    # print(polymere_template)

    count_dict: dict[str, int] = {}

    for letter in polymere_template:
        if letter not in count_dict:
            count_dict[letter] = 1
        else:
            count_dict[letter] += 1

    print(count_dict)

    # print(polymere_template)

    min_letter = min(count_dict.items(), key=lambda x: x[1])
    max_letter = max(count_dict.items(), key=lambda x: x[1])

    return max_letter[1] - min_letter[1]


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
