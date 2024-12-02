from day7_common import get_bag_dict

f = open("./day7/input.txt")

instruction_list = f.readlines()

bag_dict = get_bag_dict(instruction_list)


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


print(get_nb_bag("shiny gold", bag_dict) - 1)


f.close()
