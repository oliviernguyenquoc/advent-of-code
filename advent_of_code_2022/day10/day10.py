with open("./day10/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

cycle: int = 0
next_cycle_add_x: int = 0
X: int = 1
res: list[int] = []
instruction_idx: int = 0
wait_cycle: int = -1
line: str = "#"

print(f"Number of instructions: {len(instruction_list)}")

while instruction_idx < len(instruction_list):
    cycle += 1

    if (cycle + 20) % 40 == 0:
        res.append(X * cycle)
    if cycle % 40 == 0:
        print(line)
        line = ""

    if wait_cycle >= 0:
        command = ""
    else:
        instruction: str = instruction_list[instruction_idx]
        command = instruction[:4]

    if command == "addx":
        next_cycle_add_x = int(instruction[5:])
        wait_cycle = 1
    elif command == "noop":
        instruction_idx += 1

    if wait_cycle == 0:
        X += next_cycle_add_x
        instruction_idx += 1
        wait_cycle = -1
    else:
        wait_cycle -= 1

    line = line + ("#" if X - 1 <= cycle % 40 <= X + 1 else " ")


print(res)
print(sum(res))

# assert res == [420, 1140, 1800, 2940, 2880, 3960]
