from collections import defaultdict

with open("./2024/day23/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

connexions = defaultdict(set)

for instruction in instruction_list:
    computer1, computer2 = instruction.strip().split("-")
    connexions[computer1].add(computer2)
    connexions[computer2].add(computer1)

ring_list = []
for comp1, comp_list in connexions.items():
    # if comp1[0] == "t":
    ring_list += [{comp1, comp2} for comp2 in comp_list]

tiple_ring = []
for comp_seq in ring_list:
    for neighbor in connexions[list(comp_seq)[0]]:
        if connexions[neighbor].intersection(comp_seq) == comp_seq:
            tiple_ring.append(comp_seq | {neighbor})

all_comp_t = {k for k in connexions.keys() if k[0] == "t"}  #

ring_list_t = set(
    frozenset(comp_seq)
    for comp_seq in tiple_ring
    if set(comp_seq).intersection(all_comp_t)
)

print(f"Part 1: {len(ring_list_t)}")


max_seq_length_found = (3, "")

ring_dict = {min(seq): seq for seq in tiple_ring}

for element in ring_dict.keys():
    # Just need to check 1 computer
    # (to see if its neighbors are connected with other computer of the ring)
    for neigboor in connexions[element]:
        seq = ring_dict[element]
        connected_neighbor_found = False
        if neigboor not in seq and connexions[neigboor].intersection(seq) == seq:
            seq |= {neigboor}
            connected_neighbor_found = True

        if connected_neighbor_found:
            ring_dict[element] = seq
            if len(seq) > max_seq_length_found[0]:
                max_seq_length_found = (len(seq), element)

print(f"Part 2: {",".join(sorted(ring_dict[max_seq_length_found[1]]))}")
