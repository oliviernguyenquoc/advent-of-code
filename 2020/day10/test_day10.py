import pytest
import pathlib
from .day10 import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return [int(i.strip()) for i in instruction_list]


@pytest.mark.parametrize(
    "filepath, expected",
    [("test_input.txt", 35), ("larger_test_input.txt", 220), ("input.txt", 2343)],
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, expected",
    [
        ("test_input.txt", 8),
        ("larger_test_input.txt", 19208),
        ("input.txt", 31581162962944),
    ],
)
def test_part2(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data) == expected
