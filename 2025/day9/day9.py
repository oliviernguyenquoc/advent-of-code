import pathlib
import itertools
import collections


def parse_data(instruction_list) -> set[tuple[int, int]]:
    coords = set()
    for instruction in instruction_list:
        x_str, y_str = instruction.strip().split(",")
        coords.add((int(x_str), int(y_str)))

    return coords


def part1(instruction_list) -> int:
    coords = parse_data(instruction_list)

    max_area = 0
    for coord1, coord2 in itertools.combinations(coords, 2):
        area = (abs(coord2[1] - coord1[1]) + 1) * (abs(coord2[0] - coord1[0]) + 1)
        if area > max_area:
            max_area = area

    return max_area


def build_segments(
    coords: set[tuple[int, int]],
) -> collections.defaultdict[(int, list[tuple[int, int]])]:
    lines = collections.defaultdict(list)
    for coord1, coord2 in itertools.combinations(coords, 2):
        if coord1[1] == coord2[1]:
            for x in range(min(coord1[0], coord2[0]), max(coord1[0], coord2[0]) + 1):
                lines[x].append(coord1[1])

    # Sort y point for each x in dict
    for x, y_list in lines.items():
        lines[x] = sorted(y_list)

    # Build segment of what is in the shape
    segments: collections.defaultdict[(int, list[tuple[int, int]])] = (
        collections.defaultdict(list)
    )
    y_start = -1
    for x, y_list in lines.items():
        is_inside, is_on_the_edge = False, False

        for y in y_list:

            # Entering an edge (by a corner)
            if (x, y) in coords and not is_on_the_edge:
                if not is_inside:
                    y_start = y
                is_on_the_edge = True
                continue

            # Leaving an edge (by a corner)
            if (x, y) in coords and is_on_the_edge:
                if is_inside:
                    segments[x].append((y_start, y))
                is_on_the_edge = False
                continue

            # Crossing an edge
            if not is_inside:
                y_start = y
            
            # Leaving the inside by an edge
            if is_inside:
                segments[x].append((y_start, y))

            is_inside = not is_inside


    return segments


# def build_segments(
#     coords: list[tuple[int, int]],
# ) -> collections.defaultdict[(int, list[tuple[int, int]])]:
#     lines = collections.defaultdict(list)
#     for coord1, coord2 in itertools.combinations(coords, 2):
#         if coord1[1] == coord2[1]:
#             for x in range(min(coord1[0], coord2[0]), max(coord1[0], coord2[0]) + 1):
#                 lines[x].append(coord1[1])
#     # Sort y point for each x in dict
#     for x, y_list in lines.items():
#         lines[x] = sorted(y_list)

#     # Build segment of what is in the shape
#     segments: collections.defaultdict[(int, list[tuple[int, int]])] = (
#         collections.defaultdict(list)
#     )
#     for x, y_list in lines.items():
#         segments[x] = list(itertools.batched(y_list, 2))


def is_inside_shape(
    coord1: tuple[int, int],
    coord2: tuple[int, int],
    segments: collections.defaultdict[(int, list[tuple[int, int]])],
) -> bool:

    for x in range(min(coord1[0], coord2[0]), max(coord1[0], coord2[0])):
        for y in range(min(coord1[0], coord2[0]), max(coord1[0], coord2[0])):
            if not any([y_start < y < y_end for (y_start, y_end) in segments[x]]):
                return False

    return True


def part2(instruction_list) -> int:
    coords = parse_data(instruction_list)

    segments = build_segments(coords)

    max_area = 0
    for coord1, coord2 in itertools.combinations(coords, 2):
        area = (abs(coord2[1] - coord1[1]) + 1) * (abs(coord2[0] - coord1[0]) + 1)
        if (coord1 == (9, 5) or coord2 == (9, 5)) and (
            coord1 == (2, 3) or coord2 == (2, 3)
        ):
            print("hey")
        if area > max_area and is_inside_shape(coord1, coord2, segments):
            max_area = area

    return max_area


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
