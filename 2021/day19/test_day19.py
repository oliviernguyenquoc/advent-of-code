import pytest
import pathlib
from .day19 import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected, is_test",
    [("test_input.txt", 79, True), ("input.txt", 1234, False)],
)
def test_part1(filepath, expected, is_test):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data, is_test) == expected


@pytest.mark.parametrize(
    "filepath, expected, is_test",
    [("test_input.txt", 456, True), ("input.txt", 7890, False)],
)
def test_part2(filepath, expected, is_test):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data, is_test) == expected
