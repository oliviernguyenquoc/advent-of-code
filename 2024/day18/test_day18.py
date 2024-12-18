import pytest
from day18 import find_shortest_path_length

def test_find_shortest_path_length():
    with open("./2024/day18/input.txt", encoding="utf-8") as f:
        instruction_list = f.readlines()

    incoming_bytes = []

    for i, instruction in enumerate(instruction_list):
        x_str, y_str = instruction.strip().split(",")
        incoming_bytes.append((int(x_str), int(y_str)))

    NB_BYTES = 12
    assert find_shortest_path_length(incoming_bytes[:NB_BYTES]) - 1 == 318
