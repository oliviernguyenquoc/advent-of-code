import pytest
import pathlib
from .day3 import part1, check_if_adjacent
from .day3_part2 import part2

PUZZLE_DIR = pathlib.Path(__file__).parent


def load_input(path):
    with open(PUZZLE_DIR / path, encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    return instruction_list


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 4361), ("input.txt", 538046)]
)
def test_part1(filepath, expected):
    """Test part 1"""
    data = load_input(filepath)
    assert part1(data) == expected


@pytest.mark.parametrize(
    "filepath, expected", [("test_input.txt", 467835), ("input.txt", 81709807)]
)
def test_part2(filepath, expected):
    """Test part 2"""
    data = load_input(filepath)
    assert part2(data) == expected


@pytest.fixture
def test1():
    return ["x..", ".12", "..."]


@pytest.fixture
def test2():
    return [".x.", ".12", "..."]


@pytest.fixture
def test3():
    return ["..x", ".12", "..."]


@pytest.fixture
def test4():
    return ["...", "x12", "..."]


@pytest.fixture
def test5():
    return ["...", "12x", "..."]


@pytest.fixture
def test6():
    return ["...", ".12", "x.."]


@pytest.fixture
def test7():
    return ["...", ".12", ".x."]


@pytest.fixture
def test8():
    return ["...", ".12", "..x"]


@pytest.fixture
def test9():
    return ["...", ".12", "..."]


@pytest.fixture
def test10():
    return ["...", "..x", ".12"]


def test_check_if_adjacent_test1(test1):
    assert check_if_adjacent(test1, 1, 1, 2) is True


def test_check_if_adjacent_test2(test2):
    assert check_if_adjacent(test2, 1, 1, 2) is True


def test_check_if_adjacent_test3(test3):
    assert check_if_adjacent(test3, 1, 1, 2) is True


def test_check_if_adjacent_test4(test4):
    assert check_if_adjacent(test4, 1, 1, 2) is True


def test_check_if_adjacent_test5(test5):
    assert check_if_adjacent(test5, 1, 0, 1) is True


def test_check_if_adjacent_test6(test6):
    assert check_if_adjacent(test6, 1, 1, 2) is True


def test_check_if_adjacent_test7(test7):
    assert check_if_adjacent(test7, 1, 1, 2) is True


def test_check_if_adjacent_test8(test8):
    assert check_if_adjacent(test8, 1, 1, 2) is True


def test_check_if_adjacent_test9(test9):
    assert check_if_adjacent(test9, 1, 1, 2) is False


def test_check_if_adjacent_test10(test10):
    assert check_if_adjacent(test10, 2, 1, 2) is True
