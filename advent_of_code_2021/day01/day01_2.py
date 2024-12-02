with open("./day01/input.txt") as f:
    instruction_list = f.read().splitlines()

number_list = [int(instruction) for instruction in instruction_list]

increase_count = 0

for i in range(1, len(number_list[1:-1])):
    if sum(number_list[i : i + 3]) > sum(number_list[i - 1 : i + 2]):
        increase_count += 1

print(increase_count)
