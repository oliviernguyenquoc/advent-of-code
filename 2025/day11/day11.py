import pathlib
import itertools


def parse_data(instruction_list) -> dict[str, list[str]]:
    connexion_dict = {}

    for instruction in instruction_list:
        if instruction.strip() == "":
            continue

        input_str, output_str = instruction.strip().split(": ")
        connexion_dict[input_str] = output_str.split(" ")

    return connexion_dict


def part1(instruction_list) -> int:
    connection_dict = parse_data(instruction_list)

    # Use a DFS
    START_NODE = "you"
    nb_paths = 0

    queue = [START_NODE]
    while queue:
        node = queue.pop(0)

        if node == "out":
            nb_paths += 1
            continue
        queue += connection_dict[node]

    return nb_paths


def find_paths(
    connection_dict: dict[str, list[str]], start_node: str, stop_node: str, max_path_length: int = 1000
) -> tuple[int, set[str]]:

    paths = [[start_node]]
    end_set = set()

    while paths:
        if any([path[-1] == stop_node for path in paths]):
            paths = [path for path in paths if path[-1] == stop_node]
            return len(paths), set()
        elif len(paths[0]) >= max_path_length:
            end_set = {path[-1] for path in paths}
            return len(paths), end_set            

        paths_tmp = []
        while paths:
            path = paths.pop(0)

            for added_node in connection_dict[path[-1]]:
                paths_tmp.append(path + [added_node])

        paths = paths_tmp.copy()


def reverse_find_paths(
        connection_dict: dict[str, list[str]], start_node: str, stop_node: str, max_path_length: int = 6
) -> tuple[int, set[str]]:
    paths = [[stop_node]]
    while paths:
        if any([path[0] == start_node for path in paths]):
            paths = [path for path in paths if path[0] == start_node]
            return len(paths), set()

        elif len(paths[0]) >= max_path_length:
            end_set = {path[0] for path in paths}
            return len(paths), end_set
            

        paths_tmp = []
        while paths:
            path = paths.pop(0)

            all_roots = [key for key, next_nodes in connection_dict.items() if path[0] in next_nodes]
            for added_node in all_roots:
                paths_tmp.append([added_node] + path)

        paths = paths_tmp.copy()


def part2(instruction_list) -> int:
    connection_dict = parse_data(instruction_list)

    first_paths_len, _ = find_paths(
        connection_dict, start_node="svr", stop_node="fft"
    )
    print(f"First part length: {first_paths_len}")

    i = 1
    begin_set, end_set = set(), set()
    while len(begin_set & end_set) == 0:
        len_path_1, begin_set = find_paths(
            connection_dict, start_node="fft", stop_node="dac", max_path_length = i
        )

        len_path_2, end_set = reverse_find_paths(
            connection_dict, start_node="fft", stop_node="dac", max_path_length = i
        )
        if len(begin_set & end_set) != 0:
            break

        len_path_2, end_set = reverse_find_paths(
            connection_dict, start_node="fft", stop_node="dac", max_path_length = i +1
        )
        i+=1

    i = 1
    begin_set, end_set = set(), set()
    while len(begin_set & end_set) == 0:
        _, begin_set = find_paths(
            connection_dict, start_node="fft", stop_node="dac", max_path_length = i
        )

        _, end_set = reverse_find_paths(
            connection_dict, start_node="fft", stop_node="dac", max_path_length = i
        )
        if len(begin_set & end_set) != 0:
            break

        _, end_set = reverse_find_paths(
            connection_dict, start_node="fft", stop_node="dac", max_path_length = i +1
        )
        i+=1

    lengths = []
    for node in (begin_set & end_set):
        len_1, _ = find_paths(
            connection_dict, start_node="fft", stop_node=node
        )
        len_2, _ = find_paths(
            connection_dict, start_node=node, stop_node="dac"
        )
        lengths.append(len_1 * len_2)

    
    print(f"Second part length: {lengths}")


    end_part_paths_len, _ = find_paths(connection_dict, start_node="dac", stop_node="out")
    print(f"End part length: {end_part_paths_len}")

    return first_paths_len * sum(lengths) * end_part_paths_len


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list)}")

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 2: {part2(instruction_list)}")
    # Too low: 9896858887860 et 98968588878600
