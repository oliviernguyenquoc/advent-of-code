import pytest
import pathlib
from .day10 import solve

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 8), ("input.txt", 6907)]
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert solve(data, part=1) == expected


@pytest.mark.parametrize(
    "filepath, start, expected",
    [
        ("test_input2.txt", "F", 4),
        ("test_input3.txt", "F", 8),
        ("test_input4.txt", "7", 10),
        ("input.txt", "7", 541),
    ],
)
def test_part2(filepath, start, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert solve(data, part=2, start=start) == expected
