import networkx
import matplotlib.pyplot as plt

with open("./2024/day23/test_input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

g = networkx.DiGraph()
computer_list = []

for instruction in instruction_list:
    computer1, computer2 = instruction.strip().split("-")
    computer_list += [computer1, computer2]
    g.add_node(computer1)
    g.add_node(computer2)
    g.add_edge(computer1, computer2)

networkx.draw(g, with_labels=True)
plt.show()

cycles = networkx.recursive_simple_cycles(g)
print(cycles)
