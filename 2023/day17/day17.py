import networkx as nx

with open("./2023/day17/test_input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

grid = [instruction.strip() for instruction in instruction_list]

len_y = len(grid)
len_x = len(grid[0])

G = nx.DiGraph()

DIRECTIONS = {(0, 1), (-1, 0), (0, -1), (1, 0)}
for x in range(len_x):
    for y in range(len_y):
        G.add_node((x, y))
        for direction in DIRECTIONS:
            new_x, new_y = x + direction[0], y + direction[1]
            if (0 <= new_x < len_x) and (0 <= new_y < len_y):
                G.add_edge(
                    (x, y),
                    (new_x, new_y),
                    weight=int(grid[new_y][new_x]),
                )

shortest_paths = nx.shortest_simple_paths(
    G, source=(0, 0), target=(len_x - 1, len_y - 1), weight="weight"
)
for k, path in enumerate(shortest_paths):
    print(k)
    i = 0
    found_wrong_path = False
    while i < len(path) - 4 and not found_wrong_path:
        if any(
            path[i][j] == path[i + 1][j] == path[i + 2][j] == path[i + 3][j]
            for j in range(2)
        ):
            found_wrong_path = True
        i += 1
    if not found_wrong_path:
        break


# # Find the length of the shortest path considering weights
# shortest_path_length = nx.shortest_path_length(
#     G, source=(0, 0), target=(len_x - 1, len_y - 1), weight="weight"
# )

print("Shortest path:", path[i - 1])
# print("Shortest path length:", shortest_path_length)
