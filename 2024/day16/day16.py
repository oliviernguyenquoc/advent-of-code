from collections import defaultdict
from enum import IntEnum
import heapq
import pathlib


class Direction(IntEnum):
    WEST = 0
    NORTH = 1
    EST = 2
    SOUTH = 3


def solve(instruction_list, part=1):
    DIRECTIONS = [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1),
    ]

    # (move_foward, turn_left_or_right)
    MOVEMENTS = ((1, 0), (0, 1), (0, -1))

    walls = set()
    start, end = (0, 0), (0, 0)

    grid = [instruction.strip() for instruction in instruction_list]

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            match char:
                case "#":
                    walls.add((x, y))
                case "S":
                    start = (x, y, Direction.EST)
                case "E":
                    end = (x, y)

    # Ignore surrounding walls
    distances = {
        (x, y, direction): float("inf")
        for y in range(1, len(grid) - 1)
        for x in range(1, len(grid[0]) - 1)
        for direction in Direction
    }

    prev = defaultdict(set)

    # Initialization
    distances[start] = 0
    pqueue = [(0, *start)]
    visited = set()

    # Dijkstra
    while pqueue:
        current_cost, x, y, direction = heapq.heappop(pqueue)
        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))
        for movement in MOVEMENTS:
            next_position = (
                x + (movement[0] * DIRECTIONS[direction.value][0]),
                y + (movement[0] * DIRECTIONS[direction.value][1]),
                Direction((direction.value + movement[1]) % 4),
            )

            if (
                next_position[0],
                next_position[1],
            ) in walls or next_position not in distances:
                continue

            if movement[0] == 0:
                cost = 1000
            else:
                cost = 1

            new_cost = current_cost + cost
            if distances[next_position] >= new_cost:
                distances[next_position] = new_cost
                prev[next_position].add((x, y, direction))
                heapq.heappush(pqueue, (new_cost, *next_position))

    if part == 1:
        return min(distances[(*end, Direction.NORTH)], distances[(*end, Direction.EST)])

    paths = [[(*end, Direction.NORTH)]]

    while any([path[-1] != start for path in paths]):
        path = paths.pop(0)
        if path[-1] != start:
            for new_path in prev[path[-1]]:
                paths.append(path + [new_path])
        else:
            paths.append(path)

    all_coordinates = set()
    for path in paths:
        all_coordinates |= set((coord[0], coord[1]) for coord in path)

    return len(all_coordinates)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
