import re


def get_bag_dict(instruction_list: list) -> dict:

    bag_dict = {}

    for instruction in instruction_list:
        no_bag_regex = re.compile("([a-z ]*) bags contain no other bags?")
        bag_regex = re.compile(r"([0-9]{0,2}) ?([a-z ]*) bags?")

        # Contain no other bags
        if no_bag_regex.match(instruction):
            interpreted_instruction = [no_bag_regex.match(instruction).group(1)]
            bag_dict[interpreted_instruction[0]] = None
        else:
            bag_match = bag_regex.match(instruction)
            origin_bag = bag_match.group(2)
            bag_dict[origin_bag] = []

            for j, bag_match in enumerate(bag_regex.finditer(instruction)):
                if j != 0:
                    bag_dict[origin_bag].append(
                        (bag_match.group(1), bag_match.group(2))
                    )

    return bag_dict
