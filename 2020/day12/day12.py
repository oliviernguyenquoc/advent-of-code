import pathlib


class BoatPart1:
    def __init__(self):
        self.direction = "E"
        self.x = 0
        self.y = 0

    def move(self, command: str, n: int):
        cardinal = ["S", "W", "N", "E"]
        if command == "F":
            self._foward(n)
        elif command == "E":
            self.x += n
        elif command == "W":
            self.x -= n
        elif command == "N":
            self.y += n
        elif command == "S":
            self.y -= n
        elif command == "R":
            self.direction = cardinal[
                (cardinal.index(self.direction) + (n // 90) % 360) % 4
            ]
        elif command == "L":
            self.direction = cardinal[
                (cardinal.index(self.direction) - (n // 90) % 360) % 4
            ]

    def _foward(self, n: int):
        if self.direction == "E":
            self.x += n
        elif self.direction == "W":
            self.x -= n
        elif self.direction == "N":
            self.y += n
        elif self.direction == "S":
            self.y -= n


class BoatPart2:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1

    def move(self, command: str, n: int):
        if command == "F":
            self._foward(n)
        elif command == "E":
            self.waypoint_x += n
        elif command == "W":
            self.waypoint_x -= n
        elif command == "N":
            self.waypoint_y += n
        elif command == "S":
            self.waypoint_y -= n
        elif command in ["R", "L"]:
            if command == "L":
                n = -n

            if n % 360 == 90:
                tmp_x = self.waypoint_x
                self.waypoint_x = self.waypoint_y
                self.waypoint_y = -tmp_x
            elif n % 360 == 180:
                self.waypoint_x = -self.waypoint_x
                self.waypoint_y = -self.waypoint_y
            elif n % 360 == 270:
                tmp_x = self.waypoint_x
                self.waypoint_x = -self.waypoint_y
                self.waypoint_y = tmp_x

    def _foward(self, n: int):
        self.x += n * self.waypoint_x
        self.y += n * self.waypoint_y


def part1(instruction_list):
    boat = BoatPart1()

    for instruction in instruction_list:
        command = instruction[0]
        n = int(instruction[1:])
        boat.move(command, n)

    return abs(boat.x) + abs(boat.y)


def part2(instruction_list):
    boat = BoatPart2()

    for instruction in instruction_list:
        command = instruction[0]
        n = int(instruction[1:])
        boat.move(command, n)

    return abs(boat.x) + abs(boat.y)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
