import pathlib

DIGIT_SET = {
    0: {"a", "b", "c", "e", "f", "g"},
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"},
}


def _test_intersection(
    digit: int, str_to_test: str, local_digit_dict: dict[int, set[int]]
) -> bool:
    return all(
        [
            len(DIGIT_SET[digit].intersection(DIGIT_SET[i]))
            == len(set(str_to_test).intersection(local_digit_dict[i]))
            for i in DIGIT_SET
            if i in local_digit_dict
        ]
    )


def get_corespondance(input_value_list: str) -> dict[int, set[str]]:
    local_digit_dict = {}

    for group_str in input_value_list:
        match len(group_str):
            case 2:
                local_digit_dict[1] = set(group_str)
            case 3:
                local_digit_dict[7] = set(group_str)
            case 4:
                local_digit_dict[4] = set(group_str)
            case 7:
                local_digit_dict[8] = set(group_str)

    while len(local_digit_dict) != 10:
        for group_str in input_value_list:
            match len(group_str):
                case 5:
                    # Could be 2 or 3 or 5
                    if _test_intersection(2, group_str, local_digit_dict):
                        local_digit_dict[2] = set(group_str)
                    elif _test_intersection(3, group_str, local_digit_dict):
                        local_digit_dict[3] = set(group_str)
                    elif _test_intersection(5, group_str, local_digit_dict):
                        local_digit_dict[5] = set(group_str)
                case 6:
                    # Could be 0 or 6 or 9
                    if _test_intersection(0, group_str, local_digit_dict):
                        local_digit_dict[0] = set(group_str)
                    elif _test_intersection(6, group_str, local_digit_dict):
                        local_digit_dict[6] = set(group_str)
                    elif _test_intersection(9, group_str, local_digit_dict):
                        local_digit_dict[9] = set(group_str)

    return local_digit_dict


def get_numbers(
    correspondance_dict: dict[str, set[str]], output_value_list: list[str]
) -> int:
    res_list = []
    for value in output_value_list:
        for number, letters_set in correspondance_dict.items():
            if set(value) == letters_set:
                res_list.append(number)

    return int("".join(str(i) for i in res_list))


def part2(instruction_list):
    output_value_list = [
        instruction.split(" | ")[1] for instruction in instruction_list
    ]
    output_value_list = [output_value.split() for output_value in output_value_list]

    input_value_list = [instruction.split(" | ")[0] for instruction in instruction_list]
    input_value_list = [input_value.split() for input_value in input_value_list]

    res_list = []

    for i in range(len(input_value_list)):
        correspondance_dict = get_corespondance(
            input_value_list[i] + output_value_list[i]
        )
        number = get_numbers(correspondance_dict, output_value_list[i])
        res_list.append(number)

    return sum(res_list)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
