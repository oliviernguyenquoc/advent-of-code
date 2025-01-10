import pathlib


def part1(instruction_list, is_test):
    if is_test:
        NB_STACKS = 3
    else:
        NB_STACKS = 9

    stack: list[list[str]] = [[] for i in range(NB_STACKS)]

    for instruction in instruction_list:
        if (
            not instruction.startswith("move")
            and not instruction.startswith(" 1   2   3")
            and instruction != ""
        ):
            for i in range(0, len(instruction), 4):
                if instruction[i : i + 3] == "   ":
                    continue
                if instruction[i] == "[":
                    stack[i // 4].append(instruction[i + 1])
        elif instruction.startswith(" 1   2   3"):
            stack = [row[::-1] for row in stack]
        elif instruction.startswith("move"):
            _, nb_move, _, stack_begin_position, _, stack_end_position = (
                instruction.split(" ")
            )

            # cast to int
            nb_move = int(nb_move)
            stack_begin_position = int(stack_begin_position)
            stack_end_position = int(stack_end_position)

            for i in range(nb_move):
                item_to_move = stack[stack_begin_position - 1].pop()
                stack[stack_end_position - 1].append(item_to_move)

    return "".join([row[-1] for row in stack])


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list, is_test=True)}")
