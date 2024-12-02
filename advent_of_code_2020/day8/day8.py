f = open("./day8/input.txt")

instruction_list = f.readlines()
done_list = [False] * len(instruction_list)

i = 0
acc = 0

instruction_list = [tuple(instruction.split()) for instruction in instruction_list]

while not done_list[i]:
    done_list[i] = True
    instruction, nb = instruction_list[i][0], int(instruction_list[i][1])
    if instruction == "acc":
        acc += nb
        i += 1
    elif instruction == "jmp":
        i += nb
    elif instruction == "nop":
        i += 1

print(acc)

f.close()
