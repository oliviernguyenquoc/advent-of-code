import dataclasses


@dataclasses.dataclass
class Position:
    grid: list[str]
    x1: int
    y1: int
    x2: int
    y2: int

    def move(self, exclude_directions: list[tuple[int, int]] = [(0, 0), (0, 0)]):
        direction1 = self.find_direction(
            self.x1, self.y1, exclude_direction=exclude_directions[0]
        )

        if self.x1 == self.x2 and self.y1 == self.y2:
            exclude_direction = direction1
        else:
            exclude_direction = exclude_directions[1]

        direction2 = self.find_direction(
            self.x2, self.y2, exclude_direction=exclude_direction
        )

        self.x1 += direction1[0]
        self.y1 += direction1[1]
        self.x2 += direction2[0]
        self.y2 += direction2[1]

        return direction1, direction2

    def find_direction(
        self, x: int, y: int, exclude_direction: tuple[int, int] = (0, 0)
    ):
        y_len, x_len = len(self.grid), len(self.grid[0])
        if (
            y + 1 <= y_len - 1
            and self.grid[y][x] in "S|F7"
            and self.grid[y + 1][x] in "|LJ"
            and exclude_direction != (0, 1)
        ):
            return (0, 1)
        elif (
            x + 1 <= x_len - 1
            and self.grid[y][x] in "S-FL"
            and self.grid[y][x + 1] in "-7J"
            and exclude_direction != (1, 0)
        ):
            return (1, 0)
        elif (
            y - 1 >= 0
            and self.grid[y][x] in "S|LJ"
            and self.grid[y - 1][x] in "|F7"
            and exclude_direction != (0, -1)
        ):
            return (0, -1)
        elif (
            x - 1 >= 0
            and self.grid[y][x] in "S-7J"
            and self.grid[y][x - 1] in "-LF"
            and exclude_direction != (-1, 0)
        ):
            return (-1, 0)

        raise Exception("Ohoh")

    def is_same_positions(self) -> bool:
        return (self.x1 == self.x2) and (self.y1 == self.y2)


def find_start(instruction_list: list[str]) -> tuple[int, int]:
    for j, instruction in enumerate(instruction_list):
        for i, char in enumerate(instruction):
            if char == "S":
                return (i, j)


with open("./2023/day10/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

instruction_list = [instruction.strip() for instruction in instruction_list]

start_x, start_y = find_start(instruction_list)
position = Position(
    grid=instruction_list, x1=start_x, y1=start_y, x2=start_x, y2=start_y
)

nb_moves = 1
all_positions = {(start_x, start_y)}
old_direction1, old_direction2 = position.move()
all_positions.update([(position.x1, position.y1), (position.x2, position.y2)])

while not position.is_same_positions():
    old_direction1, old_direction2 = position.move(
        exclude_directions=[
            (-old_direction1[0], -old_direction1[1]),
            (-old_direction2[0], -old_direction2[1]),
        ]
    )
    all_positions.update([(position.x1, position.y1), (position.x2, position.y2)])
    nb_moves += 1

if position.x1 == 0 and position.y1 == 0:
    nb_moves = nb_moves // 2

print(f"Part 1: {nb_moves}")

grid = instruction_list

enable_in = [False] * len(grid[0])
memory_7L = [False] * len(grid[0])
memory_FJ = [False] * len(grid[0])

count_in = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (x, y) in all_positions:
            match grid[y][x]:
                case "-":
                    enable_in[x] = not enable_in[x]
                case "7":
                    memory_7L[x] = True
                case "L":
                    if memory_7L[x]:
                        memory_7L[x] = False
                        enable_in[x] = not enable_in[x]
                    elif memory_FJ[x]:
                        memory_FJ[x] = False
                case "F":
                    memory_FJ[x] = True
                case "J":
                    if memory_FJ[x]:
                        memory_FJ[x] = False
                        enable_in[x] = not enable_in[x]
                    elif memory_7L[x]:
                        memory_7L[x] = False

                # Because in my case, it should be a 7
                case "S":
                    memory_7L[x] = True
        elif enable_in[x]:
            count_in += 1

print(f"Part 2: {count_in}")


# # Tried flood-fill (NOT WORKING)
# y_len, x_len = len(position.grid), len(position.grid[0])

# position_to_explore = set((0, i) for i in range(y_len) if (0, i) not in all_positions)
# position_to_explore.update(
#     set((x_len - 1, i) for i in range(y_len) if (x_len - 1, i)  not in all_positions)
# )
# position_to_explore.update(
#     set((i, 0) for i in range(x_len) if (i, 0) not in all_positions)
# )
# position_to_explore.update(
#     set((i, y_len - 1) for i in range(x_len) if (i, y_len - 1) not in all_positions)
# )

# possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# all_positions.update(position_to_explore)
# while position_to_explore:
#     pos = position_to_explore.pop()
#     for move in possible_moves:
#         if (
#             0 <= pos[0] + move[0] < x_len
#             and 0 <= pos[1] + move[1] < y_len
#             and (pos[0] + move[0], pos[1] + move[1]) not in all_positions
#         ):
#             position_to_explore.add((pos[0] + move[0], pos[1] + move[1]))
#             all_positions.add((pos[0] + move[0], pos[1] + move[1]))

# print(set((i,j) for i in range(x_len) for j in range(y_len)).difference(all_positions))
# print(f"Part 2: {(x_len * y_len) - len(all_positions)}")
