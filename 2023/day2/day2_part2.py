import re
from collections import defaultdict
import math

with open("./day2/input.txt", encoding="utf-8") as f:
    instructions: list[str] = f.readlines()

idx_ok: set[int] = set()
idx_ko: set[int] = set()

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

print(sum_power)
