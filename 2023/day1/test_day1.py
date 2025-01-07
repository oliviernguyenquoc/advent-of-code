import pytest
import pathlib
from .day1 import part1
from .day1_part2 import part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 2024), ("input.txt", 57270694330992)]
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, expected",
    [
        ("test_input.txt", "aaa,aoc,bbb,ccc,eee,ooo,z24,z99"),
        ("input.txt", "gwh,jct,rcb,wbw,wgb,z09,z21,z39"),
    ],
)
def test_part2(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data) == expected
