import re
from collections import defaultdict


def part1(instructions):
    idx_ok: set[int] = set()
    idx_ko: set[int] = set()

    for instruction in instructions:
        idx, record = re.search(r"Game ([0-9]*)\: (.*)", instruction).groups()

        for pick in record.split(";"):
            ball_dict = defaultdict(int)
            for ball in pick.split(","):
                nb_balls, color = re.search(r" ?([0-9]*) (.*)", ball).groups()
                ball_dict[color] = int(nb_balls)

            # Check whether the pick is possible or not
            if (
                ball_dict["red"] > 12
                or ball_dict["green"] > 13
                or ball_dict["blue"] > 14
            ):
                idx_ko.add(int(idx))
                break

        if int(idx) not in idx_ko:
            idx_ok.add(int(idx))

    return sum(idx_ok)


if __name__ == "__main__":
    with open("./day2/input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
