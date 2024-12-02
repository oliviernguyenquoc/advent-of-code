from typing import List


def game(
    starter_list: List[int],
    stop: int = 2020,
) -> int:

    turn_dict = {starter: i+1 for i, starter in enumerate(starter_list)}
    last_number = starter_list[-1]

    for turn in range(len(starter_list) + 1, stop + 1):
        if last_number not in turn_dict:
            turn_dict[last_number] = turn - 1
            last_number = 0
        else:
            tmp = (turn - 1) - turn_dict[last_number]
            turn_dict[last_number] = turn - 1
            last_number = tmp

    return last_number


eg0 = [0, 3, 6]
print(game(eg0))
assert game([1, 3, 2], stop=2020) == 1
print("Test 1 passed")
assert game([2, 1, 3], stop=2020) == 10
print("Test 2 passed")
assert game([1, 2, 3], stop=2020) == 27
print("Test 3 passed")
assert game([2, 3, 1], stop=2020) == 78
print("Test 4 passed")
assert game([3, 2, 1], stop=2020) == 438
print("Test 5 passed")
assert game([3, 1, 2], stop=2020) == 1836
print("Test 6 passed")

print(f"Part 1: {game([1, 20, 11, 6, 12, 0])}")

assert game([0, 3, 6], stop=30000000) == 175594
print("Test 1 passed")
assert game([1, 3, 2], stop=30000000) == 2578
print("Test 2 passed")
assert game([1, 2, 3], stop=30000000) == 261214
print("Test 3 passed")
assert game([2, 3, 1], stop=30000000) == 6895259
print("Test 4 passed")
assert game([3, 2, 1], stop=30000000) == 18
print("Test 5 passed")
assert game([3, 1, 2], stop=30000000) == 362
print("Test 6 passed")


print(f"Part 1: {game([1, 20, 11, 6, 12, 0], stop=30000000)}")
