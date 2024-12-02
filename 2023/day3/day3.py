import pytest

with open("./day3/input.txt", encoding="utf-8") as f:
    instructions: list[str] = f.readlines()

instructions = [instruction.strip() for instruction in instructions]


def check_if_adjacent(instructions: list[str], row_number: int, i: int, j: int) -> bool:
    # Check left side
    if i > 0:
        if instructions[row_number][i - 1] != ".":
            return True
        if row_number > 0 and instructions[row_number - 1][i - 1] != ".":
            return True
        if (
            row_number < len(instructions) - 1
            and instructions[row_number + 1][i - 1] != "."
        ):
            return True

    # Check right side
    if j < len(instructions[row_number]) - 1:
        if instructions[row_number][j + 1] != ".":
            return True
        if row_number > 0 and instructions[row_number - 1][j + 1] != ".":
            return True
        if (
            row_number < len(instructions) - 1
            and instructions[row_number + 1][j + 1] != "."
        ):
            return True

    # Check above
    if row_number > 0 and any(
        [instructions[row_number - 1][k] != "." for k in range(i, j + 1)]
    ):
        return True

    # Check bellow
    if row_number < len(instructions) - 1 and any(
        [instructions[row_number + 1][k] != "." for k in range(i, j + 1)]
    ):
        return True

    return False


all_adjacent_numbers: list[int] = []

for row_number, instruction in enumerate(instructions):
    begin, end = 0, 0
    while end < len(instruction) or begin != end:
        # Case we detect a number
        if end < len(instruction) and instruction[end].isdigit():
            end += 1

        # End of a number
        elif begin != end or end == len(instruction):
            is_adjacent = check_if_adjacent(instructions, row_number, begin, end - 1)
            if is_adjacent and instruction[begin:end].isdigit():
                all_adjacent_numbers.append(int(instruction[begin:end]))
            begin = end

        #  No number
        else:
            begin += 1
            end += 1

# print(all_adjacent_numbers)
print(sum(all_adjacent_numbers))


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
