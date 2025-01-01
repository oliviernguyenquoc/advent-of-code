from collections import defaultdict
import copy

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
    ring_list += [[comp1, comp2] for comp2 in comp_list]


while not all(
    [comp_seq[-1] == comp_seq[0] or len(comp_seq) > 3 for comp_seq in ring_list]
):
    print(len(ring_list))
    comp_seq = ring_list.pop(0)
    if comp_seq[-1] != comp_seq[0]:
        if len(comp_seq) == 3:
            for comp in connexions[comp_seq[-1]]:
                if comp == comp_seq[0]:
                    ring_list.append(comp_seq + [comp])
        else:
            for comp in connexions[comp_seq[-1]]:
                ring_list.append(comp_seq + [comp])
    else:
        ring_list.append(comp_seq)

all_comp_t = {k for k in connexions.keys()}  #  if k[0] == "t"

ring_list = [
    comp_seq
    for comp_seq in ring_list
    if comp_seq[0] == comp_seq[-1] and len(comp_seq) == 4
]
ring_list = set(
    frozenset(comp_seq)
    for comp_seq in ring_list
    if set(comp_seq).intersection(all_comp_t)
)

print(f"Part 1: {len(ring_list)}")

fully_connected_neighbours_found = True

while ring_list:
    fully_connected_neighbours_found = False
    tmp = copy.deepcopy(ring_list)
    print(len(ring_list))
    new_ring_list = []
    for seq in ring_list:
        for computer in seq:
            for neigboor in connexions[computer]:
                if (
                    neigboor not in seq
                    and connexions[neigboor].intersection(seq) == seq
                ):
                    tmp = set(seq)
                    tmp.add(neigboor)
                    new_ring_list.append(tmp)

    if not new_ring_list:
        ring_list = set(frozenset(comp_seq) for comp_seq in tmp)
        break

    ring_list = set(frozenset(comp_seq) for comp_seq in new_ring_list)

print(f"Part 2: {",".join(sorted([seq for seq in ring_list][0]))}")
print(ring_list)
