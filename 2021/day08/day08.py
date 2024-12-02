with open("./day08/input.txt") as f:
    instruction_list = f.read().splitlines()

output_value_list = [
    instruction.split(" | ")[1]
    for instruction in instruction_list
]
output_value_list = [
    output_value.split()
    for output_value in output_value_list
]

# digits_dict = {2: 1, 3: 7, 4: 4, 7: 8}
count_digits = {2: 0, 3: 0, 4: 0, 7: 0}

for output_value in output_value_list:
    for letters in output_value:
        if len(letters) in count_digits:
            count_digits[len(letters)] += 1

print(sum(count_digits.values()))
