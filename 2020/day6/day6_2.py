import pathlib


def part2(instruction_list):
    answer_list = "".join(instruction_list).split("\n\n")

    total_question = 0

    for group_answer in answer_list:
        individual_anwser_list = "".join(group_answer).split("\n")

        intersection_set = {}

        for i, individual_anwser in enumerate(individual_anwser_list):
            question_set = {question for question in individual_anwser}
            if i == 0:
                intersection_set = question_set
            else:
                intersection_set = intersection_set.intersection(question_set)

        total_question += len(intersection_set)

    return total_question + 1


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 2: {part2(instruction_list)}")
