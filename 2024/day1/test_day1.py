import pytest
import pathlib
from .day1 import part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 11), ("input.txt", 1258579)]
)
def test_part1_example1(filepath, expected):
    """Test part 1 on example input."""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 31), ("input.txt", 23981443)]
)
def test_part2_example1(filepath, expected):
    """Test part 2 on example input."""
    data = load_input(filepath)
    assert part2(data) == expected
