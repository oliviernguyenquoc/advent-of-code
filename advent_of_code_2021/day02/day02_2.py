with open('./day02/input.txt') as f:
    instruction_list = f.read().splitlines() 

horizontal_position = 0
depth_position = 0
aim = 0

for instruction in instruction_list:
    move, intensity = instruction.split()
    match move:
        case 'forward':
            horizontal_position += int(intensity)
            depth_position += aim * int(intensity)
        case "down":
            aim += int(intensity)
        case "up":
            aim -= int(intensity)

print(horizontal_position * depth_position)