from dataclasses import dataclass
import pathlib


@dataclass
class Point:
    x: int
    y: int

    def move(self, x, y):
        self.x += x
        self.y += y


@dataclass
class Knot(Point):
    def follow(self, head: Point):
        diff_x = head.x - self.x
        diff_y = head.y - self.y
        move_x, move_y = (0, 0)

        match (diff_x, diff_y):
            case (-2, -1) | (-1, -2) | (-2, -2):
                move_x, move_y = (-1, -1)
            case (-2, 1) | (-1, 2) | (-2, 2):
                move_x, move_y = (-1, 1)
            case (1, -2) | (2, -1) | (2, -2):
                move_x, move_y = (1, -1)
            case (1, 2) | (2, 1) | (2, 2):
                move_x, move_y = (1, 1)
            case (2, 0):
                move_x = 1
            case (-2, 0):
                move_x = -1
            case (0, -2):
                move_y = -1
            case (0, 2):
                move_y = 1

        self.x += move_x
        self.y += move_y


def solve(instruction_list, part):
    if part == 1:
        NB_KNOTS = 1
    else:
        NB_KNOTS = 9

    # start_point = Point(0, 0)
    head = Point(0, 0)
    rope_list: list[Point] = [head] + [Knot(0, 0) for _ in range(NB_KNOTS)]
    point_set: set[tuple[int, int]] = {(0, 0)}

    for instruction in instruction_list:
        direction, number_steps = instruction.split(" ")
        number_steps = int(number_steps)

        for _ in range(number_steps):
            match direction:
                case "U":
                    head.move(0, 1)
                case "D":
                    head.move(0, -1)
                case "R":
                    head.move(1, 0)
                case "L":
                    head.move(-1, 0)

            for i in range(1, NB_KNOTS + 1):
                knot = rope_list[i]
                knot.follow(rope_list[i - 1])

            tail = rope_list[NB_KNOTS]
            point_set.add((tail.x, tail.y))

    return len(point_set)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
