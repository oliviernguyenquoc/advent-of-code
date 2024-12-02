""" NOT WORKING AS NUMBER ARE NOT UNIQUE IN GIVEN INPUT """

test_input = [1, 2, -3, 3, -2, 0, 4]

with open("./day20/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

initial_list = [int(instruction) for instruction in instruction_list]
# initial_list = test_input

LEN_LIST = len(initial_list)

current_list = initial_list.copy()
print(current_list)

for number in initial_list:
    number_idx = current_list.index(number)
    new_number_idx = number_idx + number

    if new_number_idx <= 0 or LEN_LIST <= new_number_idx:
        new_number_idx = new_number_idx % (LEN_LIST - 1)

    if new_number_idx <= number_idx:
        current_list = (
            current_list[:new_number_idx]
            + [number]
            + current_list[new_number_idx:number_idx]
            + current_list[number_idx + 1 :]
        )
    else:
        current_list = (
            current_list[:number_idx]
            + current_list[number_idx + 1 : new_number_idx + 1]
            + [number]
            + current_list[new_number_idx + 1 :]
        )

print(current_list)
zero_index = current_list.index(0)
first_nb = current_list[(1000 + zero_index) % LEN_LIST]
second_nb = current_list[(2000 + zero_index) % LEN_LIST]
third_nb = current_list[(3000 + zero_index) % LEN_LIST]
print(first_nb + second_nb + third_nb)
