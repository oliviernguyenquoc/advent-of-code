import pytest
import pathlib
from .day6 import solve

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()
    return instruction_list


@pytest.mark.parametrize(
    "data, expected",
    [
        (["bvwbjplbgvbhsrlpgdmjqwftvncz"], 5),
        (["nppdvjthqldpwncqszvftbrmjlhg"], 6),
        (["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"], 10),
        (["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 11),
    ],
)
def test_part1(data, expected):
    assert solve(data, part=1) == expected


@pytest.mark.parametrize("filepath, expected", [("input.txt", 1198)])
def test_part1_loaded(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert solve(data, part=1) == expected


@pytest.mark.parametrize(
    "filepath, expected",
    [("input.txt", 3120)],
)
def test_part2_loaded(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert solve(data, part=2) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (["mjqjpqmgbljsphdztnvjfqwrcgsmlb"], 19),
        (["bvwbjplbgvbhsrlpgdmjqwftvncz"], 23),
        (["nppdvjthqldpwncqszvftbrmjlhg"], 23),
        (["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"], 29),
        (["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 26),
    ],
)
def test_part2(data, expected):
    """Test part 2"""
    assert solve(data, part=2) == expected
