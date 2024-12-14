import re
import dataclasses
import time

with open("./2024/day14/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

@dataclasses.dataclass
class Robot:
    p_x: int
    p_y: int
    v_x: int
    v_y: int

    def move(self):
        self.p_x = (self.p_x + self.v_x) % TILE_WIDE
        self.p_y = (self.p_y + self.v_y) % TILE_TALL

    def witch_quadrant(self) -> int:
        quadrant_x = TILE_WIDE // 2
        quadrant_y = TILE_TALL // 2

        if (0 <= self.p_x < quadrant_x) and (0 <= self.p_y < quadrant_y):
            return 1
        elif (TILE_WIDE - quadrant_x <= self.p_x < TILE_WIDE) and (
            0 <= self.p_y < quadrant_y
        ):
            return 2
        elif (0 <= self.p_x < quadrant_x) and (
            TILE_TALL - quadrant_y <= self.p_y < TILE_TALL
        ):
            return 3
        elif (TILE_WIDE - quadrant_x <= self.p_x < TILE_WIDE) and (
            TILE_TALL - quadrant_y <= self.p_y < TILE_TALL
        ):
            return 4
        else:
            return 0


robot_list = []

for instruction in instruction_list:
    p_str, v_str = re.search(r"p=([0-9,-]*) v=([0-9,-]*)", instruction.strip()).groups()
    p_x, p_y = p_str.split(",")
    v_x, v_y = v_str.split(",")

    robot_list.append(Robot(p_x=int(p_x), p_y=int(p_y), v_x=int(v_x), v_y=int(v_y)))

TILE_WIDE, TILE_TALL = 101, 103
NB_CYCLES = 100000

for i in range(NB_CYCLES):
    robot_positions = ["." * TILE_WIDE] * TILE_TALL
    for robot in robot_list:
        robot.move()
        robot_positions[robot.p_y] = robot_positions[robot.p_y][:robot.p_x] + "#" + robot_positions[robot.p_y][robot.p_x+1:]
        if "############################" in robot_positions[robot.p_y]:
            print(f"------ {i} -----")
            print("\n".join(robot_positions))
            break
    
    if "############################" in robot_positions[robot.p_y]:
        break

    if i+1 == 100:
        robot_count = {i: 0 for i in range(5)}
        for robot in robot_list:
            robot_count[robot.witch_quadrant()] += 1

        print(robot_count)
        print(f"Part 1: {robot_count[1] * robot_count[2] * robot_count[3] * robot_count[4]}")

print(f"Part 2: {i+1}")