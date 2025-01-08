import pytest
import pathlib
from .day05 import part1

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 5), ("input.txt", 4745)]
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize(
    "filepath, expected",
    [("test_input.txt", 12), ("input.txt", 18442)],
)
def test_part2(filepath, expected):
    """Test part 2"""
    # data = load_input(filepath)
    # assert part2(data) == expected
