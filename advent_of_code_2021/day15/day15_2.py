import networkx as nx
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt

with open("./day15/test_input.txt") as f:
    instruction_list = f.read().splitlines()

GRID_MULTIPLIER = 5

for instruction in instruction_list:
    grid: List[List[int]] = [
        [int(number_str) for number_str in instruction_line]
        for instruction_line in instruction_list
    ]

edges: List[Tuple[int, int, Dict[str, int]]] = []

width: int = len(grid[0])
height: int = len(grid)
nb_points: int = width * height * 25

for i in range(width):
    for j in range(height):
        for width_multiplier in range(5):
            for height_multiplier in range(5):
                point_name: int = (
                    (GRID_MULTIPLIER * width * height_multiplier + GRID_MULTIPLIER * j)
                    * width
                    + (width_multiplier * width)
                    + i
                )
                # print((i, j, width_multiplier, height_multiplier))
                if (width_multiplier * width) + i < 5 * width:
                    weight: int = (
                        grid[j][(i + 1) % width] + height_multiplier + width_multiplier
                    )
                    while weight > 9:
                        weight -= 9
                    edges.append((point_name, point_name + 1, {"weight": weight}))
                if (width * height_multiplier + j) < 5 * height:
                    weight: int = (
                        grid[(j + 1) % height][i] + height_multiplier + width_multiplier
                    )
                    while weight > 9:
                        weight -= 9
                    edges.append(
                        (
                            point_name,
                            (
                                GRID_MULTIPLIER * width * height_multiplier
                                + GRID_MULTIPLIER * (j + 1)
                            )
                            * width
                            + (width_multiplier * width)
                            + i,
                            {"weight": weight},
                        )
                    )

# edges = list(set(edges))
# print(edges)
G = nx.DiGraph()
# print([(i, {"pos": (i % (width * 5), i // (height * 5))}) for i in range(nb_points)])
G.add_nodes_from(
    [(i, {"pos": (i % (width * 5), i // (height * 5))}) for i in range(nb_points)]
)
G.add_edges_from(edges)

# pos = nx.get_node_attributes(G, "pos")
# nx.draw(G, pos)
# labels = nx.get_edge_attributes(G, "weight")
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# plt.show()

print((width, height, nb_points))
print((grid[0][0], grid[width - 1][height - 1]))

# nx.draw(G, with_labels=True, font_weight="bold", node_color="orange")
# plt.show()

# This will give us the shortest path
shortest_path = nx.shortest_path(G, source=0, target=nb_points - 1, weight="weight")

# This will give us the length of the shortest path
length = nx.shortest_path_length(G, source=0, target=nb_points - 1, weight="weight")

shortest_path_weights = [
    G.get_edge_data(shortest_path[i], shortest_path[i + 1])["weight"]
    for i in range(len(shortest_path) - 1)
]

print(f"Shortest path from begin to end: {shortest_path}")
print(f"Shortest path weights from begin to end: {shortest_path_weights}")
print(f"Length of the shortest path: {length}")


def draw_graph(G, shortest_path):
    pos = nx.get_node_attributes(G, "pos")
    nx.draw(G, pos)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    path_edges = zip(shortest_path, shortest_path[1:])
    path_edges = set(path_edges)
    nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color="r")
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="r", width=10)
    plt.show()
