import pathlib


def part1(instruction_list):
    answer_list = "".join(instruction_list).split("\n\n")

    total_question = 0

    for group_answer in answer_list:
        individual_anwser_list = "".join(group_answer).split("\n")

        # print(individual_anwser_list)
        question_set = {
            question
            for individual_anwser in individual_anwser_list
            for question in individual_anwser
        }
        total_question += len(question_set)

    return total_question


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
