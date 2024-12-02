with open("./day2/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

guide_dict: dict[str, dict[str, str]] = {
    "A": {
        "X": "C",  # Rock
        "Y": "A",  # Paper
        "Z": "B",  # Scissors
    },
    "B": {
        "X": "A",
        "Y": "B",
        "Z": "C",
    },
    "C": {
        "X": "B",
        "Y": "C",
        "Z": "A",
    },
}
bonus_shape: dict[str, int] = {"A": 1, "B": 2, "C": 3}
bonus_win: dict[str, int] = {"X": 0, "Y": 3, "Z": 6}
score: int = 0

for instruction in instruction_list:
    shape_oponent, shape_me = instruction.split(" ")
    score += bonus_shape[guide_dict[shape_oponent][shape_me]]
    score += bonus_win[shape_me]

print(score)
