import pathlib


def part2(instruction_list):
    position_list = [int(instruction) for instruction in instruction_list[0].split(",")]

    sum_fuel_list = []

    # print(position_list)

    for i in range(1, max(position_list)):
        sum_fuel_list.append(
            sum(
                [
                    int(abs(position - i) * (abs(position - i) + 1) / 2)
                    for position in position_list
                ]
            )
        )

    print(sum_fuel_list.index(min(sum_fuel_list)))
    return min(sum_fuel_list)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
