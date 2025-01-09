from day7_common import get_bag_dict
import pathlib


def get_nb_gold_bag(bag_type, bag_dict):
    if bag_type == "shiny gold":
        return 1
    elif bag_dict[bag_type]:
        total = 0
        for _, bag_type in bag_dict[bag_type]:
            total += get_nb_gold_bag(bag_type, bag_dict)
        return total > 0
    else:
        return 0


def part1(instruction_list):
    bag_dict = get_bag_dict(instruction_list)

    total = 0
    total_bag_list = []
    for bag, bag_list in bag_dict.items():
        if bag_list:
            contain_gold_bag_bool = False
            for nb_bag, bag_type in bag_list:
                test_bag = get_nb_gold_bag(bag_type, bag_dict)
                if test_bag:
                    contain_gold_bag_bool = True

            if contain_gold_bag_bool:
                total_bag_list.append(bag)
                total += 1

    return total


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
