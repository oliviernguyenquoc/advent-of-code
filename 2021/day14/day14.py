import tqdm
import pathlib


def part1(instruction_list):
    NB_STEP = 10

    polymere_template = instruction_list[0]

    receipes: dict[str, str] = {}

    for instruction in instruction_list[2:]:
        duo_letter, insertion_letter = instruction.split(" -> ")
        receipes[duo_letter] = insertion_letter

    for step in tqdm.tqdm(range(NB_STEP)):
        new_polymere: str = ""
        for i in range(len(polymere_template) - 1):
            new_polymere += (
                polymere_template[i]
                + receipes[polymere_template[i] + polymere_template[i + 1]]
            )
        new_polymere += polymere_template[i + 1]
        polymere_template = new_polymere

    count_dict: dict[str, int] = {}

    for letter in polymere_template:
        if letter not in count_dict:
            count_dict[letter] = 1
        else:
            count_dict[letter] += 1

    print(count_dict)

    min_letter = min(count_dict.items(), key=lambda x: x[1])
    max_letter = max(count_dict.items(), key=lambda x: x[1])

    return max_letter[1] - min_letter[1]


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
