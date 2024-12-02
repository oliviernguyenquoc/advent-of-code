import math
from typing import Dict

f = open("./day16/input.txt")

instruction_list = f.readlines()


bloc_list = "".join(instruction_list).split("\n\n")
rules_list = [rule.split(":") for rule in bloc_list[0].split("\n")]
rule_dict = {rule[0]: rule[1] for rule in rules_list}


def mkrule(rule):
    rule1, rule2 = [rule for rule in rule.split(" or ")]
    min1, max1 = [int(i) for i in rule1.split("-")]
    min2, max2 = [int(i) for i in rule2.split("-")]

    def func(x):
        return (min1 <= x <= max1) or (min2 <= x <= max2)

    return func


rule_dict = {name: mkrule(rule) for name, rule in rule_dict.items()}
my_ticket_list = [int(ticket) for ticket in bloc_list[1].split("\n")[1].split(",")]

nearby_ticket_list = [
    ticket.split(",") for ticket in bloc_list[2].split("\n") if "nearby" not in ticket
]
nearby_ticket_list = [
    [int(ticket) for ticket in ticket_list] for ticket_list in nearby_ticket_list
]

sum_res = 0
discard_list = []

for ticket_list in nearby_ticket_list:
    is_ticket_list_valid = True

    for ticket in ticket_list:
        if not any(func(ticket) for _, func in rule_dict.items()):
            sum_res += ticket
            is_ticket_list_valid = False

    if not is_ticket_list_valid:
        discard_list.append(ticket_list)

nearby_ticket_list = [
    ticket_list for ticket_list in nearby_ticket_list if ticket_list not in discard_list
]

rule_name_dict = {rule: [] for rule in rule_dict}


for rule, func in rule_dict.items():
    for i in range(len(nearby_ticket_list[0])):
        if all(func(ticket_list[i]) for ticket_list in nearby_ticket_list):
            rule_name_dict[rule].append(i)


def deduce_rule_list(rule_name_dict: Dict[str, int]) -> Dict[str, int]:
    to_delete = []
    all_done = False
    while not all_done:
        all_done = True

        for rule, check_rule_list in rule_name_dict.items():
            if len(check_rule_list) == 1 and check_rule_list[0] not in to_delete:
                to_delete.append(check_rule_list[0])

        for rule, check_rule_list in rule_name_dict.items():
            new_list = list(set(check_rule_list) - set(to_delete))
            if len(new_list) < len(check_rule_list) and len(check_rule_list) > 1:
                rule_name_dict[rule] = new_list
                all_done = False

    rule_name_dict = {
        rule: check_rule_list[0] for rule, check_rule_list in rule_name_dict.items()
    }
    return rule_name_dict


rule_name_dict = deduce_rule_list(rule_name_dict)
print(len(nearby_ticket_list))
print(sum_res)
print(rule_name_dict)
departure_id_list = [id for rule, id in rule_name_dict.items() if "departure" in rule]
print(math.prod([my_ticket_list[i] for i in departure_id_list]))

f.close()