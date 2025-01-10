import pytest
import pathlib
from .day2_1 import part1
from .day2_2 import part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 2), ("input.txt", 680)]
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 1), ("input.txt", 710)]
)
def test_part2(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data) == expected