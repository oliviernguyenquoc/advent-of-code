import pytest
import pathlib
from .day15 import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 26), ("input.txt", 4502208)]
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, expected",
    [("test_input.txt", 56000011), ("input.txt", 13784551204480)],
)
def test_part2(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data) == expected
