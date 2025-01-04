import networkx as nx
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt

with open("./day15/input.txt") as f:
    instruction_list = f.read().splitlines()

for instruction in instruction_list:
    grid: List[List[int]] = [
        [int(number_str) for number_str in instruction_line]
        for instruction_line in instruction_list
    ]

edges: List[Tuple[int, int, Dict[str, int]]] = []

width: int = len(grid[0])
height: int = len(grid)
nb_points: int = width * height

for i in range(width):
    for j in range(height):
        point_name: int = j * height + i
        if i + 1 < width:
            edges.append((point_name, point_name + 1, {"weight": grid[j][i + 1]}))
        if j + 1 < height:
            edges.append((point_name, (j + 1) * height + i, {"weight": grid[j + 1][i]}))

# edges = list(set(edges))
# print(edges)
G = nx.DiGraph()
G.add_nodes_from([(i, {"pos": (i % width, i // height)}) for i in range(nb_points)])
G.add_edges_from(edges)

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

print((width, height, nb_points))
print((grid[0][0], grid[width - 1][height - 1]))

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
