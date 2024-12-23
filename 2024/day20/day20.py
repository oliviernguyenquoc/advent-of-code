import networkx

with open("./2024/day20/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

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


def find_shortest_path(
    walls: list[tuple[int, int]], start: tuple[int, int], end: tuple[int, int]
) -> int:
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


shortest_path_base = list(find_shortest_path(walls, start, end))

base_score = len(shortest_path_base) - 1
print(f"Base score is: {base_score}")


def manathan_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


all_scores = []
for i, point1 in enumerate(shortest_path_base):
    for j, point2 in enumerate(shortest_path_base):
        if i < j and manathan_distance(point1, point2) == 2:
            shortcut_length = (j - i) - manathan_distance(point1, point2)
            all_scores.append(shortcut_length)

print(f"Part1: {len([score for score in all_scores if score >= 100])}")

all_scores = []
for i, point in enumerate(shortest_path_base):
    for j, point2 in enumerate(shortest_path_base):
        if i < j and 2 <= manathan_distance(point, point2) <= 20:
            shortcut_length = (j - i) - manathan_distance(point, point2)
            all_scores.append(shortcut_length)

print(f"Part2: {len([score for score in all_scores if score >= 100])}")
