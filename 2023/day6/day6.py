import re
import math
import pathlib

def compute_min_max_time(time: int, record_dist: int) -> tuple[int, int]:
    min_time = math.ceil((time - math.sqrt(time**2 - 4 * record_dist)) / 2)
    max_time = math.floor((time + math.sqrt(time**2 - 4 * record_dist)) / 2)

    # Doing the same distance as the record is not counted as "beat the record"
    if min_time * (time - min_time) == record_dist:
        min_time += 1
    if max_time * (time - max_time) == record_dist:
        max_time -= 1

    return min_time, max_time


def parse_data(instructions):
    times = re.search(r"Time: *([0-9 ]*)", instructions[0]).groups()[0]
    distances = re.search(r"Distance: *([0-9 ]*)", instructions[1]).groups()[0]
    return times, distances


def part1(instructions):
    times, distances = parse_data(instructions)

    times_part1 = [int(nb) for nb in times.split()]
    distances_part1 = [int(nb) for nb in distances.split()]

    nb_ways = []
    for time, record_dist in zip(times_part1, distances_part1):
        min_time, max_time = compute_min_max_time(time, record_dist)
        nb_ways.append(max_time - min_time + 1)

    return math.prod(nb_ways)


def part2(instructions):
    times, distances = parse_data(instructions)

    time_part2 = int("".join(times.split()))
    distance_part2 = int("".join(distances.split()))

    min_time, max_time = compute_min_max_time(time_part2, distance_part2)

    return max_time - min_time + 1


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
