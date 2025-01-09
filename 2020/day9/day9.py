import pathlib


def check_there_is_two_number_sum(a: int, x: list[int]) -> bool:
    """O(nlog(n)) complexity, O(1) space algo Yeah !"""

    x = sorted(x)

    i, j = 0, len(x) - 1

    while i != j:
        if x[i] + x[j] == a:
            return True
        if x[i] + x[j] > a:
            j -= 1
        elif x[i] + x[j] < a:
            i += 1

    return False


def find_continuous_sum(a: int, x: list[int]) -> tuple[int]:
    i, j = 0, 1

    while i != len(x) or j != len(x):
        sum_sub_x = sum(x[i:j])
        if sum_sub_x == a:
            return (i, j)
        elif sum_sub_x < a:
            j += 1
        elif sum_sub_x > a:
            i += 1

    return (0, 0)


def parse_data(nb_list):
    nb_list = [int(nb) for nb in nb_list]
    LEN_CHECK = 25

    # Complexity n * k*log(k) with k=25
    for i in range(len(nb_list) - LEN_CHECK):
        if not check_there_is_two_number_sum(
            nb_list[i + LEN_CHECK], nb_list[i : i + LEN_CHECK]
        ):
            break

    return nb_list, i, LEN_CHECK


def part1(nb_list):
    nb_list, i, LEN_CHECK = parse_data(nb_list)
    return nb_list[i + LEN_CHECK]


def part2(nb_list):
    nb_list, i, LEN_CHECK = parse_data(nb_list)
    a, b = find_continuous_sum(nb_list[i + LEN_CHECK], nb_list)
    return min(nb_list[a:b]) + max(nb_list[a:b])


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
