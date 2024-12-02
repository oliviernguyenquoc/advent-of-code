from typing import List, Dict
import tqdm

NB_STEP = 10

with open("./day14/input.txt") as f:
    instruction_list = f.read().splitlines()

polymere_template = instruction_list[0]

receipes: Dict[str, str] = {}

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

    # print(polymere_template)

count_dict: Dict[str, int] = {}

for letter in polymere_template:
    if letter not in count_dict:
        count_dict[letter] = 1
    else:
        count_dict[letter] += 1

print(count_dict)


# print(polymere_template)


min_letter = min(count_dict.items(), key=lambda x: x[1])
max_letter = max(count_dict.items(), key=lambda x: x[1])

print(max_letter[1] - min_letter[1])
