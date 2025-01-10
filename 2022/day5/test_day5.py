import pytest
import pathlib
from .day5 import part1
from .day5_part2 import part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, is_test, expected",
    [("test_input.txt", True, "CMZ"), ("input.txt", False, "RFFFWBPNS")],
)
def test_part1(filepath, is_test, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data, is_test=is_test) == expected


@pytest.mark.parametrize(
    "filepath, is_test, expected",
    [("test_input.txt", True, "MCD"), ("input.txt", False, "CQQBBJFCS")],
)
def test_part2(filepath, is_test, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data, is_test=is_test) == expected
