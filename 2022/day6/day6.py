def solve(instruction_list, part):
    if part == 1:
        BUFFER_SIZE = 4
    else:
        BUFFER_SIZE = 14

    result: int = 0

    for instruction in instruction_list:
        buffer: str = instruction[:BUFFER_SIZE]
        instruction = instruction[BUFFER_SIZE:]

        for position, letter in enumerate(instruction):
            buffer += letter
            buffer = buffer[1:]
            if len(set(buffer)) == BUFFER_SIZE:
                # +1 for 0-position start index,
                # + BUFFER_SIZE because it begins with a BUFFER_SIZE-letter buffer
                result = position + 1 + BUFFER_SIZE
                break
        break

    return result


if __name__ == "__main__":
    with open("./day6/input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
