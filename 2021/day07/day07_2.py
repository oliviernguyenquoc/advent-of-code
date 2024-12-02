with open("./day07/input.txt") as f:
    instruction_list = f.read().splitlines()

position_list = [int(instruction) for instruction in instruction_list[0].split(",")]

sum_fuel_list = []

print(position_list)

for i in range(1, max(position_list)):
    sum_fuel_list.append(
        sum(
            [
                int(abs(position - i) * (abs(position - i) + 1) / 2)
                for position in position_list
            ]
        )
    )

print(sum_fuel_list.index(min(sum_fuel_list)))
print(min(sum_fuel_list))

