from __future__ import annotations

import math
import re
from dataclasses import dataclass

PART_1: bool = False  # True
NB_ROUND: int = 10000  # 20

with open("./day11/input.txt", encoding="utf-8") as f:
    instructions: str = f.read()

values = re.findall(
    r"""Monkey ([0-9]*):\n  Starting items: ([0-9 ,]*)
  Operation: new = old (.) (.*)\n  Test: divisible by ([0-9]*)
    If true: throw to monkey ([0-9]*)
    If false: throw to monkey ([0-9]*)""",
    instructions,
)


@dataclass
class Item:
    worry_level: int


@dataclass
class Monkey:
    id: int
    item_list: list[Item]
    operation: str
    operation_number: str
    test_number: int
    monkey_test_true_int: int
    monkey_test_false_int: int
    monkey_test_true: Monkey | None = None
    monkey_test_false: Monkey | None = None

    def load_test_monkeys(self, true_monkey: "Monkey", false_monkey: "Monkey"):
        self.monkey_test_true = true_monkey
        self.monkey_test_false = false_monkey

    def round(self):
        for item in self.item_list:
            # Inspect item
            match self.operation:
                case "-":
                    if self.operation_number.isnumeric():
                        item.worry_level -= int(self.operation_number)
                    else:
                        item.worry_level -= item.worry_level
                case "+":
                    if self.operation_number.isnumeric():
                        item.worry_level += int(self.operation_number)
                    else:
                        item.worry_level += item.worry_level
                case "*":
                    if self.operation_number.isnumeric():
                        item.worry_level *= int(self.operation_number)
                    else:
                        item.worry_level *= item.worry_level

            # Level of stress decrease
            if PART_1:
                item.worry_level = math.floor(item.worry_level / 3)
            else:
                item.worry_level = item.worry_level % GCD

            # Test item
            if item.worry_level % self.test_number == 0:
                self.monkey_test_true.item_list.append(item)
            else:
                self.monkey_test_false.item_list.append(item)

        self.item_list = []


monkey_list: list[Monkey] = []

for value in values:
    monkey_list.append(
        Monkey(
            id=int(value[0]),
            item_list=[Item(int(item)) for item in value[1].split(", ")],
            operation=value[2],
            operation_number=value[3],
            test_number=int(value[4]),
            monkey_test_true_int=int(value[5]),
            monkey_test_false_int=int(value[6]),
        )
    )

print(len(monkey_list))
GCD = 1

for monkey in monkey_list:
    monkey.load_test_monkeys(
        true_monkey=monkey_list[monkey.monkey_test_true_int],
        false_monkey=monkey_list[monkey.monkey_test_false_int],
    )
    GCD *= monkey.test_number

monkey_dict: dict[int, int] = {i: 0 for i in range(len(monkey_list))}

for round_number in range(NB_ROUND):
    print(f"Round {round_number}")
    for monkey_idx, monkey in enumerate(monkey_list):
        monkey_dict[monkey_idx] += len(monkey.item_list)
        monkey.round()

print(monkey_dict)

higher_items_inspections = sorted(list(monkey_dict.values()))[-2:]
monkey_business = higher_items_inspections[0] * higher_items_inspections[1]
print(monkey_business)
