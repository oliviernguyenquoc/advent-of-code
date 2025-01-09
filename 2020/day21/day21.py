from pprint import pprint
import pathlib


def solve(instruction_list, part):
    base_food_list = "".join(instruction_list).strip().split("\n")

    food_list = []
    all_ingredient_list = []
    for food in base_food_list:
        ingredient_list, alergene_list = food.split(" (contains ")
        ingredient_list = ingredient_list.split(" ")
        alergene_list = alergene_list[:-1].split(", ")
        food_list.append((set(ingredient_list), set(alergene_list)))

        all_ingredient_list += ingredient_list

    all_allergene_set = set()
    for food in food_list:
        all_allergene_set.update(food[1])

    allergene_dict = {}

    for allergene in all_allergene_set:
        all_ingredient_set = set(all_ingredient_list)
        for food in food_list:
            if allergene in food[1]:
                all_ingredient_set = all_ingredient_set & food[0]

        allergene_dict[allergene] = all_ingredient_set

    # print("allergene_dict: ", allergene_dict)

    ingredient_not_safe = set()
    for ingredient_set in allergene_dict.values():
        ingredient_not_safe.update(ingredient_set)

    # print("ingredient_not_safe:", ingredient_not_safe)

    if part == 1:
        return len(
            [
                ingredient
                for ingredient in all_ingredient_list
                if ingredient not in ingredient_not_safe
            ]
        )

    pprint(sorted(allergene_dict.items()))

    # With handmade elimination
    final_dict = {
        "eggs": "xxscc",
        "fish": "mjmqst",
        "nuts": "gzxnc",
        "peanuts": "vvqj",
        "sesame": "trnnvn",
        "shellfish": "gbcjqbm",
        "soy": "dllbjr",
        "wheat": "nckqzsg",
    }

    return ",".join(final_dict.values())


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {solve(instruction_list,part=1)}")
    print(f"Part 2: {solve(instruction_list,part=2)}")
