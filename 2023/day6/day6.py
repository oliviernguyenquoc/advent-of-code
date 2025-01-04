import re
import math


def compute_min_max_time(time: int, record_dist: int) -> tuple[int, int]:
    min_time = math.ceil((time - math.sqrt(time**2 - 4 * record_dist)) / 2)
    max_time = math.floor((time + math.sqrt(time**2 - 4 * record_dist)) / 2)

    # Doing the same distance as the record is not counted as "beat the record"
    if min_time * (time - min_time) == record_dist:
        min_time += 1
    if max_time * (time - max_time) == record_dist:
        max_time -= 1

    return min_time, max_time


with open("./day6/input.txt", encoding="utf-8") as f:
    instructions: list[str] = f.readlines()

times = re.search(r"Time: *([0-9 ]*)", instructions[0]).groups()[0]
times_part1 = [int(nb) for nb in times.split()]
time_part2 = int("".join(times.split()))

distances = re.search(r"Distance: *([0-9 ]*)", instructions[1]).groups()[0]
distances_part1 = [int(nb) for nb in distances.split()]
distance_part2 = int("".join(distances.split()))

nb_ways = []
for time, record_dist in zip(times_part1, distances_part1):
    min_time, max_time = compute_min_max_time(time, record_dist)
    nb_ways.append(max_time - min_time + 1)

print(f"Part 1: {math.prod(nb_ways)}")

min_time, max_time = compute_min_max_time(time_part2, distance_part2)
print(f"Part 2: {max_time - min_time + 1}")
