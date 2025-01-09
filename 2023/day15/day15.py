import re
from collections import OrderedDict
import pathlib

def hash(input_str: str) -> int:
    total = 0
    for char in input_str:
        total += ord(char)
        total *= 17
        total = total % 256
    return total


def part1(instruction_list):
    seq = instruction_list[0].strip().split(",")

    total = 0
    for element in seq:
        total += hash(element)

    return total


def part2(instruction_list):
    seq = instruction_list[0].strip().split(",")

    boxes = {i: OrderedDict() for i in range(256)}

    for element in seq:
        nb, op = re.search(r"([a-z]*)([-=1-9]{1,2})", element).groups()
        index = hash(nb)
        if op[0] == "-":
            if nb in boxes[index]:
                boxes[index].pop(nb)

        else:
            focal_length = int(op[1])
            boxes[index][nb] = focal_length

    total_part2 = 0

    for idx, box in boxes.items():
        for i, (_, focal_length) in enumerate(box.items()):
            total_part2 += (idx + 1) * (i + 1) * focal_length

    return total_part2


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
