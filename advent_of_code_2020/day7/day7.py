from day7_common import get_bag_dict

f = open("./day7/input.txt")

instruction_list = f.readlines()

bag_dict = get_bag_dict(instruction_list)

total_bags = 0


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

print(total)

f.close()
