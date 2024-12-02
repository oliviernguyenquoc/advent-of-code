import re
from dataclasses import dataclass

with open("./day22/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

DIRECTION_LIST: list[str] = ["R", "D", "L", "U"]
MOVE_DICT: dict[str, tuple[int, int]] = {
    "R": (1, 0),
    "D": (0, 1),
    "L": (-1, 0),
    "U": (0, -1),
}

path: str = instruction_list[-1]

path_list = re.split(r"(\d+)", path)
map_temp = instruction_list[:-2]
WIDTH = max([len(row) for row in map_temp])
HIGHT = len(map_temp)


@dataclass
class Cursor:
    i: int
    j: int
    direction: str
    map: list[str]

    def turn_right(self):
        direction_idx = DIRECTION_LIST.index(self.direction)
        self.direction = DIRECTION_LIST[(direction_idx + 1) % len(DIRECTION_LIST)]

    def turn_left(self):
        direction_idx = DIRECTION_LIST.index(self.direction)
        self.direction = DIRECTION_LIST[(direction_idx - 1) % len(DIRECTION_LIST)]

    def move(
        self, nb_steps: int, part: int = 1, test_exemple: bool = False
    ) -> tuple[int, int]:
        for _ in range(nb_steps):
            move_x, move_y = MOVE_DICT[self.direction]

            if part == 1:
                x, y, direction = self._get_next_coordinates(move_x, move_y)
            else:
                if test_exemple:
                    x, y, direction = self._get_next_coordinates_part_2_test(
                        move_x, move_y
                    )
                else:
                    x, y, direction = self._get_next_coordinates_part_2(move_x, move_y)

            if x == 10 and y == 11:
                print("h")

            if self.map[y][x] == "#":
                continue
            else:
                self.i = x
                self.j = y
                self.direction = direction

    def _get_next_coordinates(self, move_x: int, move_y: int) -> tuple[int, int, str]:
        if (
            self.j + move_y >= HIGHT
            or self.j + move_y < 0
            or self.i + move_x >= WIDTH
            or self.i + move_x < 0
            or self.map[self.j + move_y][self.i + move_x] == " "
        ):
            while self.map[(self.j + move_y) % HIGHT][
                (self.i + move_x) % WIDTH
            ] not in ["#", "."]:
                added_move_x, added_move_y = MOVE_DICT[self.direction]
                move_x += added_move_x
                move_y += added_move_y

        return (self.i + move_x) % WIDTH, (self.j + move_y) % HIGHT, self.direction

    def _get_next_coordinates_part_2_test(
        self, move_x: int, move_y: int
    ) -> tuple[int, int, str]:
        teleport_dict = {}
        for i in range(4):
            teleport_dict.update({(12, i, "R"): (15, 11 - i, "L")})
            teleport_dict.update({(16, 11 - i, "R"): (11, i, "L")})

            teleport_dict.update({(7, i, "L"): (4 + i, 4, "D")})
            teleport_dict.update({(4 + i, 3, "U"): (8, i, "R")})

            teleport_dict.update({(8 + i, -1, "U"): (3 - i, 4, "D")})
            teleport_dict.update({(3 - i, 3, "U"): (8 + i, 0, "D")})

            teleport_dict.update({(-1, 4 + i, "L"): (15 - i, 11, "U")})
            teleport_dict.update({(15 - i, 12, "D"): (0, 4 + i, "R")})

            teleport_dict.update({(4 + i, 8, "D"): (8, 11 - i, "R")})
            teleport_dict.update({(7, 11 - i, "L"): (4 + i, 7, "U")})

            teleport_dict.update({(12 + i, 7, "U"): (11, 7 - i, "L")})
            teleport_dict.update({(12, 7 - i, "R"): (12 + i, 8, "D")})

            teleport_dict.update({(8 + i, 12, "D"): (3 - i, 7, "U")})
            teleport_dict.update({(3 - i, 8, "D"): (8 + i, 11, "U")})

        if (self.i + move_x, self.j + move_y, self.direction) in teleport_dict:
            x, y, direction = teleport_dict[
                (self.i + move_x, self.j + move_y, self.direction)
            ]
        else:
            x = self.i + move_x
            y = self.j + move_y
            direction = self.direction

        return x, y, direction

    def _get_next_coordinates_part_2(
        self, move_x: int, move_y: int
    ) -> tuple[int, int, str]:
        teleport_dict = {}
        for i in range(50):
            teleport_dict.update({(50 + i, -1, "U"): (0, 150 + i, "R")})
            teleport_dict.update({(-1, 150 + i, "L"): (50 + i, 0, "D")})

            teleport_dict.update({(49, i, "L"): (0, 149 - i, "R")})
            teleport_dict.update({(-1, 149 - i, "L"): (50, i, "R")})

            teleport_dict.update({(150, i, "R"): (99, 149 - i, "L")})
            teleport_dict.update({(100, 149 - i, "R"): (149, i, "L")})

            teleport_dict.update({(100 + i, -1, "U"): (i, 199, "U")})
            teleport_dict.update({(i, 200, "D"): (100 + i, 0, "D")})

            teleport_dict.update({(100 + i, 50, "D"): (99, 50 + i, "L")})
            teleport_dict.update({(100, 50 + i, "R"): (100 + i, 49, "U")})

            teleport_dict.update({(49, 50 + i, "L"): (i, 100, "D")})
            teleport_dict.update({(i, 99, "U"): (50, 50 + i, "R")})

            teleport_dict.update({(50, 150 + i, "R"): (50 + i, 149, "U")})
            teleport_dict.update({(50 + i, 150, "D"): (49, 150 + i, "L")})

        if (self.i + move_x, self.j + move_y, self.direction) in teleport_dict:
            x, y, direction = teleport_dict[
                (self.i + move_x, self.j + move_y, self.direction)
            ]
        else:
            x = self.i + move_x
            y = self.j + move_y
            direction = self.direction

        return x, y, direction


# Add missing spaces
map_temp = [row + (" " * (WIDTH - len(row))) for row in map_temp]


# PART 1
cursor = Cursor(map_temp[0].index("."), 0, "R", map=map_temp)

for instruction in path_list:
    if instruction.isnumeric():
        cursor.move(nb_steps=int(instruction), part=1)
    elif instruction == "R":
        cursor.turn_right()
    elif instruction == "L":
        cursor.turn_left()

print(
    f"Result part 1: {1000 * (cursor.j + 1) + 4 * (cursor.i + 1) + DIRECTION_LIST.index(cursor.direction)}"
)


# PART 2
cursor = Cursor(map_temp[0].index("."), 0, "R", map=map_temp)

for instruction in path_list:
    # print(instruction)

    if instruction.isnumeric():
        cursor.move(nb_steps=int(instruction), part=2, test_exemple=False)
    elif instruction == "R":
        cursor.turn_right()
    elif instruction == "L":
        cursor.turn_left()
    print(cursor.i, cursor.j, cursor.direction)

print(
    f"Result part 2: {1000 * (cursor.j + 1) + 4 * (cursor.i + 1) + DIRECTION_LIST.index(cursor.direction)}"
)
