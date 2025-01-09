import pathlib


def solve(instruction_list, part):
    if part == 1:
        NB_DAYS = 80
    else:
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
        # print(fish_state)
        # print(f"After {day + 1} days: {sum(fish_state.values())}")

    return sum(fish_state.values())


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
