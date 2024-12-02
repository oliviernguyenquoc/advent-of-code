f = open("./day6/input.txt")

answer_list = "".join(f.readlines()).split("\n\n")

total_question = 0

for group_answer in answer_list:
    individual_anwser_list = "".join(group_answer).split("\n")

    question_set_list = []
    intersection_set = {}

    for i, individual_anwser in enumerate(individual_anwser_list):
        question_set = {question for question in individual_anwser}
        if i == 0:
            intersection_set = question_set
        else:
            intersection_set = intersection_set.intersection(question_set)

    total_question += len(intersection_set)

print(total_question)
f.close()
