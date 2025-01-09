import pathlib

def horizontal_comparison(figure: list[str], y: int) -> bool:
    len_y = len(figure)
    if y <= len_y // 2:
        if figure[:y] == figure[y : 2 * y][::-1]:
            return True
    else:
        if figure[2 * y - len_y : y] == figure[y:][::-1]:
            return True

    return False


def vertical_comparison(figure: list[str], x: int) -> bool:
    len_x = len(figure[0])
    part1 = []
    part2 = []

    for y in range(len(figure)):
        if x <= len_x // 2:
            part1.append(figure[y][:x])
            part2.append(figure[y][x : 2 * x][::-1])
        else:
            part1.append(figure[y][2 * x - len_x : x])
            part2.append(figure[y][x:][::-1])

    return part1 == part2


def horizontal_comparison_with_smudge(figure: list[str], y: int) -> bool:
    len_y = len(figure)
    if y <= len_y // 2:
        if sum([figure[:y][i] != figure[y : 2 * y][::-1][i] for i in range(y)]) == 1:
            return (
                sum(
                    [
                        i != j
                        for line1, line2 in zip(figure[:y], figure[y : 2 * y][::-1])
                        for i, j in zip(line1, line2)
                    ]
                )
                == 1
            )
    else:
        if (
            sum(
                [
                    figure[2 * y - len_y : y][i] != figure[y:][::-1][i]
                    for i in range(len_y - y)
                ]
            )
            == 1
        ):
            return (
                sum(
                    [
                        i != j
                        for line1, line2 in zip(
                            figure[2 * y - len_y : y], figure[y:][::-1]
                        )
                        for i, j in zip(line1, line2)
                    ]
                )
                == 1
            )


def vertical_comparison_with_smudge(figure: list[str], x: int) -> bool:
    len_x = len(figure[0])
    part1 = []
    part2 = []

    nb_diff = 0
    for y in range(len(figure)):
        if x <= len_x // 2:
            tmp1 = figure[y][:x]
            tmp2 = figure[y][x : 2 * x][::-1]
            if tmp1 != tmp2:
                nb_diff += 1
            part1.append(tmp1)
            part2.append(tmp2)
        else:
            tmp1 = figure[y][2 * x - len_x : x]
            tmp2 = figure[y][x:][::-1]
            if tmp1 != tmp2:
                nb_diff += 1
            part1.append(tmp1)
            part2.append(tmp2)

        if nb_diff > 1:
            return False

    if nb_diff != 1:
        return False
    else:
        return (
            sum(
                [
                    i != j
                    for line1, line2 in zip(part1, part2)
                    for i, j in zip(line1, line2)
                ]
            )
            == 1
        )


def parse_data(instruction_list):
    figures = []
    tmp = []
    for instruction in instruction_list:
        if instruction == "\n":
            figures.append(tmp)
            tmp = []
        else:
            tmp.append(instruction.strip())
    figures.append(tmp)

    return figures


def part1(instruction_list):
    figures = parse_data(instruction_list)

    horizontal_symetries, vertical_symetries = 0, 0

    for i, figure in enumerate(figures):
        len_y = len(figure)
        for y in range(1, len_y):
            if horizontal_comparison(figure, y):
                horizontal_symetries += 100 * y

        for x in range(1, len(figure[0])):
            if vertical_comparison(figure, x):
                vertical_symetries += x

    return horizontal_symetries + vertical_symetries


def part2(instruction_list):
    figures = parse_data(instruction_list)

    horizontal_symetries, vertical_symetries = 0, 0
    horizontal_symetries_smuge, vertical_symetries_smuge = 0, 0

    for i, figure in enumerate(figures):
        len_y = len(figure)
        for y in range(1, len_y):
            if horizontal_comparison(figure, y):
                horizontal_symetries += 100 * y

            elif horizontal_comparison_with_smudge(figure, y):
                horizontal_symetries_smuge += 100 * y

        for x in range(1, len(figure[0])):
            if vertical_comparison(figure, x):
                vertical_symetries += x

            elif vertical_comparison_with_smudge(figure, x):
                vertical_symetries_smuge += x

    return horizontal_symetries_smuge + vertical_symetries_smuge


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
