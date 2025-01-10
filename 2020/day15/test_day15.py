import pytest
import pathlib
from .day15 import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.read().strip().split(",")

    return [int(i) for i in instruction_list]


@pytest.mark.parametrize("filepath, expected", [("input.txt", 1085)])
def test_part1_loade(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        ([0, 3, 6], 436),
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836),
    ],
)
def test_part1(data, expected):
    """Test part 1"""
    assert part1(data) == expected


@pytest.mark.parametrize("filepath, expected", [("input.txt", 10652)])
def test_part2_loade(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        ([0, 3, 6], 175594),
        ([1, 3, 2], 2578),
        ([1, 2, 3], 261214),
        ([2, 3, 1], 6895259),
        ([3, 2, 1], 18),
        ([3, 1, 2], 362),
    ],
)
def test_part2(data, expected):
    """Test part 2"""
    assert part2(data) == expected
