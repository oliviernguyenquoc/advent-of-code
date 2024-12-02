f = open("./day6/input.txt")

answer_list = "".join(f.readlines()).split("\n\n")

total_question = 0

for group_answer in answer_list:
    individual_anwser_list = "".join(group_answer).split("\n")

    print(individual_anwser_list)
    question_set = {
        question
        for individual_anwser in individual_anwser_list
        for question in individual_anwser
    }
    total_question += len(question_set)

print(total_question)
f.close()
