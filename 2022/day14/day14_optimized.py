from dataclasses import dataclass

# Result for part 1 or part 2
PART_2 = True


Point = tuple[int, int]


@dataclass
class Environment:
    points: dict[Point, str]

    def is_free(self, x: int, y: int):
        return (x, y) not in self.points

    def add_sand(self, new_sand: Point):
        self.points[new_sand] = "o"

    def add_wall(self, wall: Point):
        self.points[wall] = "#"


with open("./day14/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

environment = Environment({})

for instruction in instruction_list:
    wall_instruction_list = instruction.split(" -> ")
    for idx in range(len(wall_instruction_list) - 1):
        x_start_parsed, y_start_parsed = wall_instruction_list[idx].split(",")
        x_end_parsed, y_end_parsed = wall_instruction_list[idx + 1].split(",")

        x_start = min(int(x_start_parsed), int(x_end_parsed))
        x_end = max(int(x_start_parsed), int(x_end_parsed))
        y_start = min(int(y_start_parsed), int(y_end_parsed))
        y_end = max(int(y_start_parsed), int(y_end_parsed))

        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                environment.add_wall((x, y))

Y_FLOOR = max([point[1] for point in environment.points]) + 2
print(f"Floor at {Y_FLOOR}")
print(f"Number of wall block: {len(environment.points)}")

if PART_2:
    for x in range(-1000, 1000):
        environment.add_wall((x, Y_FLOOR))

while True:
    finish_condition = False
    sand_blocked = False

    new_sand = (500, 0)

    while not finish_condition:
        old_x, old_y = new_sand

        for move in [(0, 1), (-1, 1), (1, 1)]:
            if environment.is_free(new_sand[0] + move[0], new_sand[1] + move[1]):
                new_sand = (new_sand[0] + move[0], new_sand[1] + move[1])
                break

        if not PART_2 and new_sand[1] >= Y_FLOOR + 2:
            finish_condition = True
        if PART_2 and new_sand[0] == 500 and new_sand[1] == 0:
            finish_condition = True

        # Sand didn't moved
        if old_x == new_sand[0] and old_y == new_sand[1]:
            break

    # print(f"Number of sand block: {len(environment.points)}")
    environment.add_sand(new_sand)

    if finish_condition:
        break

res = len(
    [point for point, character in environment.points.items() if character == "o"]
)
if not PART_2:
    res -= 1  # Do not count last sand
print(res)
