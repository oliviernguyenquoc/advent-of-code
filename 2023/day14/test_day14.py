import pytest
import pathlib
from .day14 import part1
from .day14_part2 import part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 136), ("input.txt", 108813)]
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, cycle_length, expected",
    [("test_input.txt", 13, 64), ("input.txt", 10, 104533)],
)
def test_part2(filepath, cycle_length, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data, cycle_length) == expected
