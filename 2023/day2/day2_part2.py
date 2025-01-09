import re
from collections import defaultdict
import math
import pathlib


def part2(instructions):
    sum_power = 0

    for instruction in instructions:
        idx, record = re.search(r"Game ([0-9]*)\: (.*)", instruction).groups()
        ball_dict = defaultdict(int)

        for pick in record.split(";"):
            for ball in pick.split(","):
                nb_balls, color = re.search(r" ?([0-9]*) (.*)", ball).groups()
                ball_dict[color] = max(ball_dict[color], int(nb_balls))

        power = math.prod([ball for ball in ball_dict.values()])
        sum_power += power

    return sum_power


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 2: {part2(instruction_list)}")
