import pytest
import pathlib
from .day22 import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 6032), ("input.txt", 123046)]
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, is_test, expected",
    [("test_input.txt", True, 5031), ("input.txt", False, 195032)],
)
def test_part2(filepath, is_test, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data, is_test) == expected
