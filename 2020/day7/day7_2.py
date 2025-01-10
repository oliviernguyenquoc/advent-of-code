from .day7_common import get_bag_dict
import pathlib


def get_nb_bag(bag_type: str, bag_dict: dict):
    total = 0

    if not isinstance(bag_dict[bag_type], list):
        return 1
    else:
        for nb_subbag, subbag_type in bag_dict[bag_type]:
            nb_total_bag = get_nb_bag(subbag_type, bag_dict)
            total += int(nb_subbag) * nb_total_bag

        total += 1

    return total


def part2(instruction_list):
    bag_dict = get_bag_dict(instruction_list)
    return get_nb_bag("shiny gold", bag_dict) - 1


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 2: {part2(instruction_list)}")
