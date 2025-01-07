import pytest
import pathlib
from .day11 import solve

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 374), ("input.txt", 9543156)]
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert solve(data, part=1) == expected


@pytest.mark.parametrize(
    "filepath, multiplier, expected",
    [
        ("test_input.txt", 5, 1030),
        ("test_input.txt", 50, 8410),
        ("input.txt", 500000, 625243292686),
    ],
)
def test_part2(filepath, multiplier, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert solve(data, part=2, multiplier=multiplier) == expected
