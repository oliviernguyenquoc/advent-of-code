import pathlib


def generate_set(x1: int, y1: int, x2: int, y2: int) -> set[tuple[int, int]]:
    if x1 == x2 or y1 == y2:
        res = {
            (x, y)
            for x in range(min(x1, x2), max(x1, x2) + 1)
            for y in range(min(y1, y2), max(y1, y2) + 1)
        }
    else:
        res = set()
    return res


def generate_set_with_diag(x1: int, y1: int, x2: int, y2: int) -> set[tuple[int, int]]:
    if x1 == x2 or y1 == y2:
        res = {
            (x, y)
            for x in range(min(x1, x2), max(x1, x2) + 1)
            for y in range(min(y1, y2), max(y1, y2) + 1)
        }
    elif abs(x1 - x2) == abs(y1 - y2):
        # This side : \
        res = {
            (x, y)
            for x in range(min(x1, x2), max(x1, x2) + 1)
            for y in range(min(y1, y2), max(y1, y2) + 1)
            if abs(x + y) == abs(x1 + y1)
        }

        # This side : /
        res.update(
            {
                (x, y)
                for x in range(min(x1, x2), max(x1, x2) + 1)
                for y in range(min(y1, y2), max(y1, y2) + 1)
                if y - x == y1 - x1
            }
        )
    else:
        res = set()
    return res


# xxo (3,1)
# xox (2,2)
# oxx (1,3)


# Test function
def test_generate_set():
    print(generate_set(1, 2, 3, 2) == {(1, 2), (2, 2), (3, 2)})
    print(generate_set(2, 4, 2, 6) == {(2, 4), (2, 5), (2, 6)})
    print(generate_set(3, 2, 1, 2) == {(1, 2), (2, 2), (3, 2)})
    print(generate_set(2, 6, 2, 4) == {(2, 4), (2, 5), (2, 6)})


# Test function
def test_generate_set_with_diag():
    # Horizontal / vertical
    print(generate_set(1, 2, 3, 2) == {(1, 2), (2, 2), (3, 2)})
    print(generate_set(2, 4, 2, 6) == {(2, 4), (2, 5), (2, 6)})
    print(generate_set(3, 2, 1, 2) == {(1, 2), (2, 2), (3, 2)})
    print(generate_set(2, 6, 2, 4) == {(2, 4), (2, 5), (2, 6)})

    # Diags
    print(generate_set_with_diag(1, 3, 3, 5) == {(1, 3), (2, 4), (3, 5)})
    print(generate_set_with_diag(3, 1, 1, 3) == {(1, 3), (2, 2), (3, 1)})
    print(generate_set_with_diag(1, 1, 3, 3) == {(1, 1), (2, 2), (3, 3)})
    print(generate_set_with_diag(9, 7, 7, 9) == {(9, 7), (8, 8), (7, 9)})
    print(generate_set_with_diag(3, 3, 1, 1) == {(1, 1), (2, 2), (3, 3)})
    print(generate_set_with_diag(7, 9, 9, 7) == {(9, 7), (8, 8), (7, 9)})
    print(generate_set_with_diag(6, 4, 2, 0))
    print(
        generate_set_with_diag(6, 4, 2, 0) == {(6, 4), (5, 3), (4, 2), (3, 1), (2, 0)}
    )


# test_generate_set_with_diag()
# exit(0)


def part1(instruction_list):
    max_x, max_y = 0, 0
    grid: dict[tuple[int, int], int] = {}

    for instruction in instruction_list:
        coordinates_str = [
            coordinates.split(",") for coordinates in instruction.split(" -> ")
        ]
        (x1, y1), (x2, y2) = [(int(x), int(y)) for x, y in coordinates_str]
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)

        # line_set = generate_set(x1, y1, x2, y2) # PART 1
        line_set = generate_set_with_diag(x1, y1, x2, y2)

        for x, y in line_set:
            if (x, y) in grid:
                grid[(x, y)] += 1
            else:
                grid[(x, y)] = 1

    count_overlap = 0

    for (x, y), nb_lines in grid.items():
        if nb_lines > 1:
            count_overlap += 1

    print(f"Grid: {max_x+1}x{max_y+1} ({(max_x+1)*(max_y+1)} points)")
    return count_overlap


# TODO: Find part2
if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
