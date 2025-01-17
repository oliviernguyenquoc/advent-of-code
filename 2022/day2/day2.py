import pathlib


def part1(instruction_list):
    guide_dict: dict[str, dict[str, int]] = {
        "A": {
            "X": 3,
            "Y": 6,
            "Z": 0,
        },
        "B": {
            "X": 0,
            "Y": 3,
            "Z": 6,
        },
        "C": {
            "X": 6,
            "Y": 0,
            "Z": 3,
        },
    }
    bonus_shape: dict[str, int] = {"X": 1, "Y": 2, "Z": 3}
    score: int = 0

    for instruction in instruction_list:
        shape_oponent, shape_me = instruction.split(" ")
        score += guide_dict[shape_oponent][shape_me]
        score += bonus_shape[shape_me]

    return score


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
