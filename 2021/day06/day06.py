with open("./day06/input.txt") as f:
    instruction_list = f.read().splitlines()

NB_DAYS = 256
fish_days = [int(instruction) for instruction in instruction_list[0].split(",")]

fish_state = {i: 0 for i in range(9)}
for fish_time in fish_days:
    fish_state[fish_time] += 1

for day in range(NB_DAYS):
    new_fish_state = {i: 0 for i in range(9)}
    for state in range(9):
        if state == 0:
            new_fish_state[8] = fish_state[0]
            new_fish_state[6] = fish_state[0]
        else:
            new_fish_state[state - 1] += fish_state[state]

    fish_state = new_fish_state
    print(fish_state)
    print(f"After {day + 1} days: {sum(fish_state.values())}")

print(sum(fish_state.values()))
