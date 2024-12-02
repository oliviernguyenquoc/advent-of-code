import statistics

with open("./day10/input.txt") as f:
    instruction_list = f.read().splitlines()

illegal_char = []
points_dict = {")": 1, "]": 2, "}": 3, ">": 4}

char_dict = {")": "(", "]": "[", ">": "<", "}": "{"}
reverse_char_dict = {reverse_char: char for char, reverse_char in char_dict.items()}

remaining_list= []

for instruction in instruction_list:
    is_illegal_line: bool = False
    char_list = []
    for char in instruction:
        if char in char_dict.values():
            char_list.append(char)
        elif char in char_dict:
            if char_list[-1] != char_dict[char]:
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
        score += points_dict[char]
    
    score_list.append(score)

print(statistics.median(score_list))
