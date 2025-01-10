import pytest
import pathlib
from .day5 import part1
from .day5_2 import part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()
    return instruction_list


@pytest.mark.parametrize("filepath, expected", [("input.txt", 880)])
def test_part1_loaded(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (["FBFBBFFRLR"], 357),
        (["BFFFBBFRRR"], 567),
        (["FFFBBBFRRR"], 119),
        (["BBFFBBFRLL"], 820),
    ],
)
def test_part1(data, expected):
    """Test part 1"""
    assert part1(data) == expected


@pytest.mark.parametrize("filepath, expected", [("input.txt", 731)])
def test_part2_loaded(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data) == expected
