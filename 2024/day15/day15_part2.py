from collections import defaultdict

with open("./2024/day15/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

walls_x, walls_y = defaultdict(list), defaultdict(list)
global boxes
boxes = set()
robot = (0, 0)
y = 0

while instruction_list[y] != "\n":
    for x, char in enumerate(instruction_list[y].strip()):
        match char:
            case "#":
                walls_x[2 * x].append(y)
                walls_x[2 * x + 1].append(y)
                walls_y[y] += [2 * x, 2 * x + 1]
            case "O":
                boxes.add((2 * x, y))
            case "@":
                robot = (2 * x, y)
    y += 1

global complement_boxes
# In order to use "]" coordinates
complement_boxes = set((x + 1, y) for x, y in boxes)

[walls_x[x].sort() for x in walls_x.keys()]
[walls_y[y].sort() for y in walls_y.keys()]

len_x, len_y = max(walls_x), max(walls_y)

moves = "".join([instruction.strip() for instruction in instruction_list[y + 1 :]])


def move_robot(
    robot: tuple[int, int], direction: tuple[int, int], walls: list[int], axis: int
) -> tuple[int, int]:
    wall_selection = walls[robot[(axis + 1) % 2]]

    # Face a wall
    if robot[axis] + direction[axis] in wall_selection:
        return robot

    next_position = (robot[0] + direction[0], robot[1] + direction[1])

    # Free to move
    if next_position not in boxes and next_position not in complement_boxes:
        return next_position

    # Horizontal move
    if axis == 0:
        return handle_horizontal_move(robot, direction, walls)

    # Vertical move
    else:
        return handle_vertical_move(robot, direction, walls)


def handle_horizontal_move(
    robot: tuple[int, int], direction: tuple[int, int], walls: list[int]
) -> tuple[int, int]:
    next_position = (robot[0] + direction[0], robot[1])
    if direction[0] < 0:
        first_wall = max([pos for pos in walls[robot[1]] if pos < robot[0]])
    else:
        first_wall = min([pos for pos in walls[robot[1]] if pos > robot[0]])

    for pos in range(robot[0] + sum(direction), first_wall, sum(direction)):
        new_position = (pos, robot[1])

        if new_position not in boxes and new_position not in complement_boxes:
            if direction[0] == -1:
                for i in range(robot[0] - 1, pos, -2):
                    boxes.remove((i - 1, robot[1]))
                    boxes.add((i - 2, robot[1]))
                    complement_boxes.remove((i, robot[1]))
                    complement_boxes.add((i - 1, robot[1]))
            elif direction[0] == 1:
                for i in range(robot[0] + 1, pos, 2):
                    boxes.remove((i, robot[1]))
                    boxes.add((i + 1, robot[1]))
                    complement_boxes.remove((i + 1, robot[1]))
                    complement_boxes.add((i + 2, robot[1]))
            return next_position

    return robot


def handle_vertical_move(
    robot: tuple[int, int], direction: tuple[int, int], walls: list[int]
) -> tuple[int, int]:
    next_position = (robot[0], robot[1] + direction[1])

    all_boxes_concidered = []
    all_complement_boxes_concidered = []

    if next_position in boxes:
        all_boxes_concidered += [{(robot[0], robot[1] + direction[1])}]
        all_complement_boxes_concidered += [{(robot[0] + 1, robot[1] + direction[1])}]
    # new_position in complement_boxes
    else:
        all_boxes_concidered += [{(robot[0] - 1, robot[1] + direction[1])}]
        all_complement_boxes_concidered += [{(robot[0], robot[1] + direction[1])}]

    next_level_boxes = {
        (x, y + direction[1])
        for x, y in all_boxes_concidered[-1] | all_complement_boxes_concidered[-1]
        if (x, y + direction[1]) in boxes
    }
    next_complement_boxes = {
        (x, y + direction[1])
        for x, y in all_boxes_concidered[-1] | all_complement_boxes_concidered[-1]
        if (x, y + direction[1]) in complement_boxes
    }

    while next_level_boxes or next_complement_boxes:
        next_level_boxes = {
            (x, y + direction[1])
            for x, y in all_boxes_concidered[-1] | all_complement_boxes_concidered[-1]
            if (x, y + direction[1]) in boxes
        }
        next_complement_boxes = {
            (x, y + direction[1])
            for x, y in all_boxes_concidered[-1] | all_complement_boxes_concidered[-1]
            if (x, y + direction[1]) in complement_boxes
        }
        if next_level_boxes:
            for x, y in next_level_boxes:
                next_complement_boxes.add((x + 1, y))
        if next_complement_boxes:
            for x, y in next_complement_boxes:
                next_level_boxes.add((x - 1, y))

        if next_level_boxes:
            all_boxes_concidered.append(next_level_boxes)
        if next_complement_boxes:
            all_complement_boxes_concidered.append(next_complement_boxes)

    if any(
        [
            y + direction[1] in walls[x]
            for x, y in set.union(*all_boxes_concidered)
            | set.union(*all_complement_boxes_concidered)
        ]
    ):
        return robot

    for x, y in set.union(*all_boxes_concidered):
        boxes.remove((x, y))

    for x, y in set.union(*all_boxes_concidered):
        boxes.add((x, y + direction[1]))

    for x, y in set.union(*all_complement_boxes_concidered):
        complement_boxes.remove((x, y))

    for x, y in set.union(*all_complement_boxes_concidered):
        complement_boxes.add((x, y + direction[1]))

    return next_position


def print_grid(walls_y, len_x, len_y, robot):
    for y in range(len_y + 1):
        line = ""
        for x in range(len_x + 1):
            if x in walls_y[y]:
                line += "#"
            elif (x, y) in boxes:
                line += "["
            elif (x, y) in complement_boxes:
                line += "]"
            elif (x, y) == robot:
                line += "@"
            else:
                line += "."
        print(line)


for move in moves:
    # print("-----------------")
    # print_grid(walls_y, len_x, len_y, robot)
    # print(move)

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

print("-----------------")
print_grid(walls_y, len_x, len_y, robot)

total = 0
for x, y in boxes:
    total += x + 100 * y

print(f"Part2: {total}")
