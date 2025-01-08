import copy
import pathlib


def part1(instruction_list):
    path_tuple_list: list[tuple[str, str]] = []

    for instruction in instruction_list:
        path_tuple_list.append(tuple(instruction.split("-")))

    path_tuple_list += [
        (path_tuple[1], path_tuple[0]) for path_tuple in path_tuple_list
    ]

    all_path_list: list[list[str]] = [
        list(start_tuple)
        for start_tuple in path_tuple_list
        if start_tuple[0] == "start"
    ]
    old_all_path_list: list[list[str]] = []

    while old_all_path_list != all_path_list:
        old_all_path_list = copy.deepcopy(all_path_list)

        for path in all_path_list:
            for path_tuple in path_tuple_list:
                if path[-1] == "end":
                    break
                if (
                    path_tuple[1] != "start"
                    and path_tuple[0] == path[-1]
                    and (path_tuple[1].isupper() or path_tuple[1] not in path)
                    and path + [path_tuple[1]] not in all_path_list
                ):
                    all_path_list.append(copy.deepcopy(path))
                    path.append(path_tuple[1])
            if path[-1] == "end":
                continue

    all_path_list = [path for path in all_path_list if path[-1] == "end"]

    # print(path_tuple_list)
    # print(all_path_list)
    return len(all_path_list)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
