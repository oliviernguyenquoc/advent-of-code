with open("./day6/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()
# instruction_list = ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

BUFFER_SIZE = 14  # 4
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

print(result)
