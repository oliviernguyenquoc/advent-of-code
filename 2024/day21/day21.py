import networkx
import itertools
import copy
import re
import pathlib


def build_graph(keyboard) -> networkx.DiGraph:
    g = networkx.DiGraph()

    DIRECTIONS_DICT = {(-1, 0): "<", (0, -1): "^", (1, 0): ">", (0, 1): "v"}
    X_LEN, Y_LEN = len(keyboard[0]), len(keyboard)

    for y, line in enumerate(keyboard):
        for x, key in enumerate(line):
            g.add_node(key)
            for direction, instruction in DIRECTIONS_DICT.items():
                if 0 <= x + direction[0] < X_LEN and 0 <= y + direction[1] < Y_LEN:
                    g.add_edge(
                        keyboard[y][x],
                        keyboard[y + direction[1]][x + direction[0]],
                        instruction=instruction,
                    )
    g.remove_node("B")

    # networkx.draw(g, with_labels=True)
    # plt.show()

    return g


def get_sequences_on_keypad(
    g: networkx.DiGraph, node_from: str, node_to: str
) -> list[str]:
    shortest_paths = networkx.all_shortest_paths(g, node_from, node_to)

    res = []
    for path in shortest_paths:
        pathGraph = networkx.path_graph(path)  # does not pass edges attributes

        instructions = ""
        for ea in pathGraph.edges():
            instructions += g.edges[ea[0], ea[1]]["instruction"]
        res.append(instructions)
    return res


def generate_keypad_dict():
    numeric_keypad = ["789", "456", "123", "B0A"]
    numeric_keypad_graph = build_graph(numeric_keypad)

    directional_keypad = ["B^A", "<v>"]
    directional_keypad_graph = build_graph(directional_keypad)

    state_numeric_dict = {}

    for a, b in itertools.permutations("A0123456789", 2):  # pragma: allowlist secret
        state_numeric_dict[(a, b)] = [
            seq + "A" for seq in get_sequences_on_keypad(numeric_keypad_graph, a, b)
        ]

    state_directional_dict = {}
    for a, b in itertools.permutations("^A<v>", 2):
        state_directional_dict[(a, b)] = [
            seq + "A" for seq in get_sequences_on_keypad(directional_keypad_graph, a, b)
        ]

    for a in "^A<v>":
        state_directional_dict[(a, a)] = ["A"]

    return state_numeric_dict, state_directional_dict


def combine_possibilities(groups: list[list[str]]) -> list[str]:
    """
    Input: pairwise iteration with every possbilities by pairs
    Output: All combinaition possible
    """
    output_list = [""]

    while groups:
        possilities = groups.pop(0)
        tmp_list = copy.deepcopy(output_list)
        output_list = []
        for new_chars in possilities:
            for chars in tmp_list:
                output_list.append(chars + new_chars)

        # if len(output_list) > 1000:
        #     min_string = min(output_list, key=len)
        #     output_list = [min_string]

    return output_list


def solve(instruction_list, part=1):
    state_numeric_dict, state_directional_dict = generate_keypad_dict()

    if part == 1:
        NB_DIRECTIONAL_KEYPAD = 1
    else:
        NB_DIRECTIONAL_KEYPAD = 25

    res_dict = {}
    for instruction in instruction_list:
        output_str = ""
        for key1, key2 in itertools.pairwise("A" + instruction.strip()):
            all_directional_path = []
            all_numeric_path = state_numeric_dict[(key1, key2)]
            for path in all_numeric_path:
                all_directional_path.append(
                    [
                        state_directional_dict[(key3, key4)]
                        for key3, key4 in itertools.pairwise("A" + path)
                    ]
                )
            tmp_list = []
            for possibility in all_directional_path:
                tmp_list += combine_possibilities(possibility)

            for i in range(NB_DIRECTIONAL_KEYPAD):
                print(f"Iteration: {i}")
                print(f"Length: {len(tmp_list)}")
                all_directional_path = copy.deepcopy(tmp_list)
                all_directional_path2 = []
                for path in all_directional_path:
                    all_directional_path2.append(
                        [
                            state_directional_dict[(key5, key6)]
                            for key5, key6 in itertools.pairwise("A" + path)
                        ]
                    )
                tmp_list = []
                for possibility in all_directional_path2:
                    tmp_list += combine_possibilities(possibility)

                min_string = min(tmp_list, key=len)
                tmp_list = [min_string]
            output_str += min_string

        res_dict[instruction.strip()] = len(output_str)

    total = 0
    for code, len_output in res_dict.items():
        nb = re.search(r"(\d+)[A-Z]*", code).groups()[0]
        total += int(nb) * len_output
    print(f"Part {part}: {total}")
    return total


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    solve(instruction_list, part=1)
    solve(instruction_list, part=2)
