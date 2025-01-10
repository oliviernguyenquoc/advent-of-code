import pytest
import pathlib
from .day18 import part1
from .day18_2 import part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize("filepath, expected, is_test", [("input.txt", 4940631886147)])
def test_part1(filepath, expected, is_test):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, expected, is_test", [("input.txt", 283582817678281)]
)
def test_part2(filepath, expected, is_test):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data, is_test) == expected
