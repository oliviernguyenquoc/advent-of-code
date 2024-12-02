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


f = open("./day12/input.txt")

instruction_list = f.readlines()

boat1 = BoatPart1()
boat2 = BoatPart2()

for instruction in instruction_list:
    command = instruction[0]
    n = int(instruction[1:])
    boat1.move(command, n)
    boat2.move(command, n)

print(f"Answer to part 1: {abs(boat1.x) + abs(boat1.y)}")
print(f"Answer to part 2: {abs(boat2.x) + abs(boat2.y)}")

f.close()
