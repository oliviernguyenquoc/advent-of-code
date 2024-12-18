import networkx

with open("./2024/day18/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

incoming_bytes = []

for i, instruction in enumerate(instruction_list):
    x_str, y_str = instruction.strip().split(",")
    incoming_bytes.append((int(x_str), int(y_str)))


def find_shortest_path_length(incoming_bytes: list[tuple[int, int]]) -> int:
    X_LEN, Y_LEN = 71, 71
    DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

    g = networkx.Graph()

    for x in range(X_LEN):
        for y in range(Y_LEN):
            if (x, y) in incoming_bytes:
                continue
            g.add_node((x, y))
            for direction in DIRECTIONS:
                new_point = (x + direction[0], y + direction[1])
                if (
                    0 <= new_point[0] < X_LEN
                    and 0 <= new_point[1] < Y_LEN
                    and new_point not in incoming_bytes
                ):
                    g.add_edge((x, y), new_point)

    shortest_path = networkx.shortest_path(g, (0, 0), (X_LEN - 1, Y_LEN - 1))

    return len(shortest_path)


NB_BYTES = 12
print(f"Part 1: {find_shortest_path_length(incoming_bytes[:NB_BYTES]) - 1}")

max_bytes = len(incoming_bytes)
min_bytes = NB_BYTES + 1

while min_bytes != max_bytes:
    nb_bytes = min_bytes + (max_bytes - min_bytes) // 2
    print(f"Searching in [{min_bytes}, {max_bytes}]. Let's try: {nb_bytes}")
    try:
        path_length = find_shortest_path_length(incoming_bytes[:nb_bytes]) - 1
        min_bytes = nb_bytes + 1
    except networkx.exception.NetworkXNoPath as err:
        print(err)
        max_bytes = nb_bytes


print(
    f"First byte to make the exit blocked is the number {min_bytes}: {incoming_bytes[nb_bytes]}"
)
print(f"Part 2: {incoming_bytes[nb_bytes][0]},{incoming_bytes[nb_bytes][1]}")
