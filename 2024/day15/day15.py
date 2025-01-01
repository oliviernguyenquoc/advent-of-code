from collections import defaultdict

with open("./2024/day15/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

y = 0
walls_x, walls_y = defaultdict(list), defaultdict(list)
global boxes
boxes = set()
robot = (0, 0)

while instruction_list[y] != "\n":
    for x, char in enumerate(instruction_list[y].strip()):
        match char:
            case "#":
                walls_x[x].append(y)
                walls_y[y].append(x)
            case "O":
                boxes.add((x, y))
            case "@":
                robot = (x, y)
    y += 1


[walls_x[x].sort() for x in walls_x.keys()]
[walls_y[y].sort() for y in walls_y.keys()]

moves = "".join([instruction.strip() for instruction in instruction_list[y + 1 :]])


def move_robot(
    robot: tuple[int, int], direction: tuple[int, int], walls: list[int], axis: int
) -> tuple[int, int]:
    wall_selection = walls[robot[(axis + 1) % 2]]
    next_position = (robot[0] + direction[0], robot[1] + direction[1])

    # Face a wall
    if robot[axis] + direction[axis] in wall_selection:
        return robot

    # Free to move
    if next_position not in boxes:
        return next_position

    if direction[axis] < 0:
        first_wall = max([pos for pos in wall_selection if pos < robot[axis]])
    else:
        first_wall = min([pos for pos in wall_selection if pos > robot[axis]])

    for pos in range(robot[axis] + sum(direction), first_wall, sum(direction)):
        if axis == 0:
            new_position = (pos, robot[1])
        else:
            new_position = (robot[0], pos)

        if new_position not in boxes:
            boxes.add(new_position)
            boxes.remove(next_position)
            return next_position

    return robot


for move in moves:
    match move:
        case "<":
            direction = (-1, 0)
            robot = move_robot(robot, direction, walls_y, 0)

        case ">":
            direction = (1, 0)
            robot = move_robot(robot, direction, walls_y, 0)

        case "^":
            direction = (0, -1)
            robot = move_robot(robot, direction, walls_x, 1)

        case "v":
            direction = (0, 1)
            robot = move_robot(robot, direction, walls_x, 1)

total = 0
for x, y in boxes:
    total += x + 100 * y

print(f"Part1: {total}")
