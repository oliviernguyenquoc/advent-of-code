import networkx
import pathlib


def parse_data(instruction_list):
    walls = set()
    start, end = (-1, -1), (-1, -1)

    for y, line in enumerate(instruction_list):
        for x, char in enumerate(line.strip()):
            match char:
                case "#":
                    walls.add((x, y))
                case "S":
                    start = (x, y)
                case "E":
                    end = (x, y)

    X_LEN, Y_LEN = len(instruction_list[0].strip()), len(instruction_list)
    return walls, start, end, X_LEN, Y_LEN


def find_shortest_path(
    walls: list[tuple[int, int]],
    start: tuple[int, int],
    end: tuple[int, int],
    x_len: int,
    y_len: int,
) -> int:
    X_LEN, Y_LEN = x_len, y_len
    DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

    g = networkx.Graph()

    for x in range(X_LEN):
        for y in range(Y_LEN):
            if (x, y) in walls:
                continue
            g.add_node((x, y))
            for direction in DIRECTIONS:
                new_point = (x + direction[0], y + direction[1])
                if (
                    1 <= new_point[0] < X_LEN - 1
                    and 1 <= new_point[1] < Y_LEN - 1
                    and new_point not in walls
                ):
                    g.add_edge((x, y), new_point)

    shortest_path = networkx.shortest_path(g, start, end)

    return shortest_path


def find_base_shortest_path(
    walls: list[tuple[int, int]],
    start: tuple[int, int],
    end: tuple[int, int],
    x_len: int,
    y_len: int,
) -> int:
    shortest_path_base = list(find_shortest_path(walls, start, end, x_len, y_len))

    base_score = len(shortest_path_base) - 1
    print(f"Base score is: {base_score}")
    return shortest_path_base


def manathan_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def part1(instruction_list, is_test=False):
    if is_test:
        TIME_THRESHOLD = 10
    else:
        TIME_THRESHOLD = 100

    walls, start, end, x_len, y_len = parse_data(instruction_list)
    shortest_path_base = find_base_shortest_path(walls, start, end, x_len, y_len)

    all_scores = []
    for i, point1 in enumerate(shortest_path_base):
        for j, point2 in enumerate(shortest_path_base):
            if i < j and manathan_distance(point1, point2) == 2:
                shortcut_length = (j - i) - manathan_distance(point1, point2)
                all_scores.append(shortcut_length)

    return len([score for score in all_scores if score >= TIME_THRESHOLD])


def part2(instruction_list, is_test=False):
    if is_test:
        TIME_THRESHOLD = 60
    else:
        TIME_THRESHOLD = 100

    walls, start, end, x_len, y_len = parse_data(instruction_list)
    shortest_path_base = find_base_shortest_path(walls, start, end, x_len, y_len)

    all_scores = []
    for i, point in enumerate(shortest_path_base):
        for j, point2 in enumerate(shortest_path_base):
            if i < j and 2 <= manathan_distance(point, point2) <= 20:
                shortcut_length = (j - i) - manathan_distance(point, point2)
                all_scores.append(shortcut_length)

    return len([score for score in all_scores if score >= TIME_THRESHOLD])


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
