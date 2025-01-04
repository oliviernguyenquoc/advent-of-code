import pytest
import pathlib
from .day12 import solve

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected",
    [
        ("test_input.txt", 140),
        ("test_input_2.txt", 772),
        ("test_input_3.txt", 1930),
        ("input.txt", 1396562),
    ],
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert solve(data, part=1) == expected


@pytest.mark.parametrize(
    "filepath, expected",
    [
        ("test_input.txt", 80),
        ("test_input_2.txt", 436),
        ("test_input_4.txt", 236),
        ("test_input_5.txt", 368),
        ("test_input_3.txt", 1206),
        ("input.txt", 844132),
    ],
)
def test_part2(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert solve(data, part=2) == expected
