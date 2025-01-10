import pytest
import pathlib
from .day16 import solve

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected",
    [("test_input.txt", 71), ("input.txt", 19060)],
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert solve(data, part=1) == expected


@pytest.mark.parametrize("filepath, expected", [("input.txt", 953713095011)])
def test_part2(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert solve(data, part=2) == expected
