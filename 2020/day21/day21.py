from pprint import pprint

f = open("./day21/input.txt")

base_food_list = "".join(f.readlines()).split("\n")

food_list = []
all_ingredient_list = []
for food in base_food_list:
    ingredient_list, alergene_list = food.split(" (contains ")
    ingredient_list = ingredient_list.split(" ")
    alergene_list = alergene_list[:-1].split(", ")
    food_list.append((set(ingredient_list), set(alergene_list)))

    all_ingredient_list += ingredient_list

len_dict = -1

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


print("allergene_dict: ", allergene_dict)

ingredient_not_safe = set()
for ingredient_set in allergene_dict.values():
    ingredient_not_safe.update(ingredient_set)

print("ingredient_not_safe:", ingredient_not_safe)

print("Part 1:",
    len(
        [
            ingredient
            for ingredient in all_ingredient_list
            if ingredient not in ingredient_not_safe
        ]
    )
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

print(f"Part 2: {','.join(final_dict.values())}")

f.close()