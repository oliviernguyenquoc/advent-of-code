with open("./2023/day16/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

grid = [instruction.strip() for instruction in instruction_list]

len_x = len(grid[0])
len_y = len(grid)


# x, y, direction(x, y)
def nb_tiles_energized(
    start_x: int, start_y: int, start_direction_x: int, start_direction_y: int
) -> int:
    seen = set()
    queue = [(start_x, start_y, start_direction_x, start_direction_y)]

    while queue:
        x, y, direction_x, direction_y = queue.pop(0)

        if (
            0 <= x + direction_x < len_x
            and 0 <= y + direction_y < len_y
            and (x, y, direction_x, direction_y) not in seen
        ):
            letter = grid[y + direction_y][x + direction_x]

            if (direction_x == 1 and letter == "/") or (
                direction_x == -1 and letter == "\\"
            ):
                queue.append((x + direction_x, y + direction_y, 0, -1))
            elif (direction_x == 1 and letter == "\\") or (
                direction_x == -1 and letter == "/"
            ):
                queue.append((x + direction_x, y + direction_y, 0, 1))
            elif (direction_y == 1 and letter == "\\") or (
                direction_y == -1 and letter == "/"
            ):
                queue.append((x + direction_x, y + direction_y, 1, 0))
            elif (direction_y == 1 and letter == "/") or (
                direction_y == -1 and letter == "\\"
            ):
                queue.append((x + direction_x, y + direction_y, -1, 0))
            elif direction_x in (1, -1) and letter == "|":
                queue += [
                    (x + direction_x, y + direction_y, 0, -1),
                    (x + direction_x, y + direction_y, 0, 1),
                ]
            elif direction_y in (1, -1) and letter == "-":
                queue += [
                    (x + direction_x, y + direction_y, -1, 0),
                    (x + direction_x, y + direction_y, 1, 0),
                ]
            else:
                queue.append(
                    (x + direction_x, y + direction_y, direction_x, direction_y)
                )

        seen.add((x, y, direction_x, direction_y))

    return len({(x, y) for x, y, _, _ in seen}) - 1


print(f"Part 1: {nb_tiles_energized(-1, 0, 1, 0)}")

results = {}
for x in range(len_x):
    results[(x, -1, 0, 1)] = nb_tiles_energized(x, -1, 0, 1)
    results[(x, len_y, 0, -1)] = nb_tiles_energized(x, len_y, 0, -1)


for y in range(len_y):
    results[(-1, y, 1, 0)] = nb_tiles_energized(-1, y, 1, 0)
    results[(len_x, y, -1, 0)] = nb_tiles_energized(len_x, y, -1, 0)

# print(results)
print(f"Part 2: {max(results.values())}")
