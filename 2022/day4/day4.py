import pathlib


def part1(instruction_list):
    result = 0

    for instruction in instruction_list:
        # print(instruction)
        (pair1_str, pair2_str) = instruction.split(",")
        tuple1 = pair1_str.split("-")
        tuple2 = pair2_str.split("-")

        # Cast str to int
        tuple1 = (int(tuple1[0]), int(tuple1[1]))
        tuple2 = (int(tuple2[0]), int(tuple2[1]))

        if (tuple1[0] <= tuple2[0] and tuple1[1] >= tuple2[1]) or (
            tuple1[0] >= tuple2[0] and tuple1[1] <= tuple2[1]
        ):
            result += 1

    return result


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
