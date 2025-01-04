import pathlib


def check_report(nuclear_reports: list[int]) -> bool:
    # Check if each number steadly increase / decrease by 1, 2 or 3
    increase_checks: list[bool] = []
    decrease_checks: list[bool] = []

    for i in range(len(nuclear_reports) - 1):
        if 0 < (nuclear_reports[i + 1] - nuclear_reports[i]) <= 3:
            increase_checks.append(True)
        else:
            increase_checks.append(False)

        if -3 <= (nuclear_reports[i + 1] - nuclear_reports[i]) < 0:
            decrease_checks.append(True)
        else:
            decrease_checks.append(False)

    return all(increase_checks) or all(decrease_checks)


def solve(instruction_list, part=1):
    nb_list: list[int] = []
    for instruction in instruction_list:
        nb_list.append([int(nb) for nb in instruction.split()])

    count_reports_part1, count_reports_part2 = 0, 0

    for nuclear_reports in nb_list:
        if check_report(nuclear_reports):
            count_reports_part1 += 1
        else:
            for i in range(len(nuclear_reports)):
                if check_report(nuclear_reports[:i] + nuclear_reports[i + 1 :]):
                    count_reports_part2 += 1
                    break

    if part == 1:
        print(f"Part 1: {count_reports_part1}")
        return count_reports_part1
    else:
        print(f"Part 2: {count_reports_part1 + count_reports_part2}")
        return count_reports_part1 + count_reports_part2


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    solve(instruction_list, part=1)
    solve(instruction_list, part=2)
