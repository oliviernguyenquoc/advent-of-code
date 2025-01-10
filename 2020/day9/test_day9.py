import pytest
import pathlib
from .day9 import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, is_test, expected",
    [("test_input.txt", True, 127), ("input.txt", False, 3199139634)],
)
def test_part1(filepath, is_test, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data, is_test) == expected


@pytest.mark.parametrize(
    "filepath, is_test, expected",
    [("test_input.txt", True, 62), ("input.txt", False, 438559930)],
)
def test_part2(filepath, is_test, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data, is_test) == expected
