import pytest
import pathlib
from .day19 import part1
from .day19_2 import part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected",
    [("test_input.txt", 6), ("input.txt", 315)],
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, expected",
    [("test_input.txt", 16), ("input.txt", 625108891232249)],
)
def test_part2(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data) == expected
