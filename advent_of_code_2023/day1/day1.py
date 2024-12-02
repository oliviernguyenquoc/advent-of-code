with open("./day1/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

# Part 1

all_digit_list = []
for instruction in instruction_list:
    digit_tuple: list[str] = []
    for char in instruction:
        if char.isdigit():
            digit_tuple.append(char)
            break

    for char in instruction[::-1]:
        if char.isdigit():
            digit_tuple.append(char)
            break

    all_digit_list.append(int(digit_tuple[0] + digit_tuple[1]))

print(all_digit_list)
print(sum(all_digit_list))
