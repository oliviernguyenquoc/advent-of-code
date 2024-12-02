NB_STACKS = 9

stack: list[list[str]] = [[] for i in range(NB_STACKS)]
with open("./day5/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

for instruction in instruction_list:
    if (
        not instruction.startswith("move")
        and not instruction.startswith(" 1   2   3")
        and instruction != ""
    ):
        for i in range(0, NB_STACKS * 4, 4):
            if instruction[i : i + 3] == "   ":
                continue
            if instruction[i] == "[":
                stack[i // 4].append(instruction[i + 1])
    elif instruction.startswith(" 1   2   3"):
        stack = [row[::-1] for row in stack]
    elif instruction.startswith("move"):
        _, nb_move, _, stack_begin_position, _, stack_end_position = instruction.split(
            " "
        )

        # cast to int
        nb_move = int(nb_move)
        stack_begin_position = int(stack_begin_position)
        stack_end_position = int(stack_end_position)

        items_to_move = stack[stack_begin_position - 1][-nb_move:]
        stack[stack_begin_position - 1] = stack[stack_begin_position - 1][:-nb_move]
        stack[stack_end_position - 1] += items_to_move

print("".join([row[-1] for row in stack]))
