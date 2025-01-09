from dataclasses import dataclass

# Result for part 1 or part 2
PART_2 = True


@dataclass
class Point:
    x: int
    y: int
    type: str | None = None

    def __eq__(self, other) -> bool:
        return (self.x == other.x) and (self.y == other.y)

    def move(self, x: int, y: int):
        self.x = x
        self.y = y


@dataclass
class Environment:
    walls: dict[int, list[Point]]
    sands: list[Point]
    top_sands: dict[int, list[Point]]

    def is_free(self, x: int, y: int):
        return (x not in self.walls or Point(x, y) not in self.walls[x]) and (
            x not in self.top_sands or Point(x, y) not in self.top_sands[x]
        )

    def add_sand(self, new_sand: Point):
        if new_sand.x not in self.top_sands:
            self.top_sands[new_sand.x] = [new_sand]
        else:
            self.top_sands[new_sand.x].append(new_sand)

    def add_wall(self, wall: Point):
        if wall.x not in self.walls:
            self.walls[wall.x] = [wall]
        else:
            self.walls[wall.x].append(wall)


with open("./day14/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

environment = Environment({}, [], {})

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
                environment.add_wall(Point(x, y, type="#"))

Y_FLOOR = (
    max([point.y for point_list in environment.walls.values() for point in point_list])
    + 2
)
print(f"Floor at {Y_FLOOR}")
print(f"Number of wall block: {len(environment.walls)}")

if PART_2:
    for x in range(-1000, 1000):
        environment.add_wall(Point(x, Y_FLOOR, type="#"))

while True:
    finish_condition = False
    sand_blocked = False

    new_sand = Point(x=500, y=0, type="o")

    while not finish_condition:
        old_x, old_y = new_sand.x, new_sand.y

        for move in [
            (new_sand.x, new_sand.y + 1),
            (new_sand.x - 1, new_sand.y + 1),
            (new_sand.x + 1, new_sand.y + 1),
        ]:
            if environment.is_free(*move):
                # print(move, new_sand)
                new_sand.move(*move)
                break

        if not PART_2 and new_sand.y >= Y_FLOOR + 2:
            finish_condition = True
        if PART_2 and new_sand.x == 500 and new_sand.y == 0:
            finish_condition = True

        # Sand didn't moved
        if old_x == new_sand.x and old_y == new_sand.y:
            break

    print(new_sand)
    # print(f"Number of wall block: {len(environment.walls)}")
    # print(environment.sands)
    # print(environment.top_sands)
    print(f"Number of sand block: {len(environment.sands)}")
    print(f"Number of top sand block: {len(environment.top_sands)}")

    environment.sands.append(new_sand)
    environment.add_sand(new_sand)

    if finish_condition:
        break

res = len(environment.sands)
if not PART_2:
    res -= 1  # Do not count last sand
print(res)
