import statistics

with open("./day07/input.txt") as f:
    instruction_list = f.read().splitlines()

position_list = [int(instruction) for instruction in instruction_list[0].split(',')]

median_position = int(statistics.median(position_list))

sum_fuel = sum([abs(position - median_position) for position in position_list])

print(sum_fuel)