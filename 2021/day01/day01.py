with open("./day01/input.txt") as f:
    instruction_list = f.read().splitlines()

number_list = [int(instruction) for instruction in instruction_list]

increase_count = 0
previous_number = number_list[0]

for number in number_list[1:]:
    if number > previous_number:
        increase_count += 1
    previous_number = number

print(increase_count)
