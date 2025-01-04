import pytest
import pathlib
from .day17 import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected",
    [
        ("test_input_2.txt", "0,1,2"),
        ("test_input_3.txt", "4,2,5,6,7,7,7,7,3,1,0"),
        ("test_input.txt", "4,6,3,5,6,3,5,2,1,0"),
        ("input.txt", "2,1,0,1,7,2,5,0,3"),
    ],
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, expected",
    [("test_input_part2.txt", 117440), ("input.txt", 267265166222235)],
)
def test_part2(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data) == expected
