import pathlib
import math
import itertools
import collections

BoxCoord = tuple[int, int, int]


def parse_data(instruction_list: list[str]) -> list[BoxCoord]:
    boxes = []
    for instruction in instruction_list:
        x_str, y_str, z_str = instruction.strip().split(",")
        boxes.append((int(x_str), int(y_str), int(z_str)))

    return boxes


def distance_boxes(coord1: tuple[int, int], coord2: tuple[int, int]) -> float:
    return math.sqrt(
        (coord2[0] - coord1[0]) ** 2
        + (coord2[1] - coord1[1]) ** 2
        + (coord2[2] - coord1[2]) ** 2
    )


def make_connexions(
    instruction_list: list[str], nb_connexions: int = 1000000000
) -> tuple[dict[BoxCoord], BoxCoord, BoxCoord]:
    boxes = parse_data(instruction_list)
    distances = [
        (coord1, coord2, distance_boxes(coord1, coord2))
        for (coord1, coord2) in itertools.combinations(boxes, 2)
    ]
    distances.sort(key=lambda x: x[2])

    groups, group_index = {}, {}
    for group_nb, box in enumerate(boxes):
        groups[group_nb] = {box}
        group_index[box] = group_nb

    nb_connection = 0
    while nb_connection < nb_connexions and len(groups) > 1:
        box1, box2, _ = distances.pop(0)
        if group_index[box1] != group_index[box2]:
            new_group_idx = min(group_index[box1], group_index[box2])
            new_group = groups[group_index[box1]] | groups[group_index[box2]]
            groups[new_group_idx] = new_group
            del groups[max(group_index[box1], group_index[box2])]

            # Update index
            for box in new_group:
                group_index[box] = new_group_idx

        nb_connection += 1

    return group_index, box1, box2


def part1(instruction_list, test=True) -> int:
    if test:
        NB_SHORTEST_CONNEXIONS = 10
    else:
        NB_SHORTEST_CONNEXIONS = 1000

    group_index, _, _ = make_connexions(instruction_list, NB_SHORTEST_CONNEXIONS)

    counter = collections.Counter(group_index.values())

    return math.prod([nb for _, nb in counter.most_common(3)])


def part2(instruction_list) -> int:
    _, box1, box2 = make_connexions(instruction_list)

    return box1[0] * box2[0]


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent
    filename = "input.txt"

    with open(PUZZLE_DIR / filename, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list, test = (filename == "test_input.txt"))}")
    print(f"Part 2: {part2(instruction_list)}")
