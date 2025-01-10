import pytest
import pathlib
from .day4 import part1
from .day4_2 import part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 2), ("input.txt", 235)]
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 2), ("input.txt", 194)]
)
def test_part2(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data) == expected
