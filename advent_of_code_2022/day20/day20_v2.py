from dataclasses import dataclass

# PART 1: NB_MIX = 1 & NB_MULTIPLIER = 1
# PART 1: NB_MIX = 10 & NB_MULTIPLIER = 811589153
NB_MIX = 10  # 1
NB_MULTIPLIER = 811589153  # 1

test_input = [1, 2, -3, 3, -2, 0, 4]

with open("./day20/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

initial_list = [int(instruction) for instruction in instruction_list]
# initial_list = test_input


@dataclass
class FileNumber:
    number: int
    initial_idx: int
    current_idx: int


number_list = [
    FileNumber(number * NB_MULTIPLIER, idx, idx)
    for idx, number in enumerate(initial_list)
]

LEN_LIST = len(number_list)

print(f"List is length: {LEN_LIST}")

for mix_idx in range(NB_MIX):
    print(f"Mix {mix_idx + 1} / 10")
    for number in number_list:
        number_idx = number.current_idx
        new_number_idx = number_idx + number.number

        if new_number_idx <= 0 or LEN_LIST <= new_number_idx:
            new_number_idx = new_number_idx % (LEN_LIST - 1)

        if new_number_idx <= number_idx:
            for temp_number in number_list:
                if new_number_idx <= temp_number.current_idx < number_idx:
                    temp_number.current_idx += 1
        else:
            for temp_number in number_list:
                if number_idx + 1 <= temp_number.current_idx <= new_number_idx:
                    temp_number.current_idx -= 1

        number.current_idx = new_number_idx

current_list = [0] * LEN_LIST

for number in number_list:
    current_list[number.current_idx] = number.number

print(current_list)

zero_index = current_list.index(0)
first_nb = current_list[(1000 + zero_index) % LEN_LIST]
second_nb = current_list[(2000 + zero_index) % LEN_LIST]
third_nb = current_list[(3000 + zero_index) % LEN_LIST]
print(first_nb + second_nb + third_nb)
