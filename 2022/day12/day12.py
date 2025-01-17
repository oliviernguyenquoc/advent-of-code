import copy
import string
from dataclasses import dataclass


@dataclass
class Node:
    x: int
    y: int
    letter: str
    score: int


def get_start(grid: list[list[str]]) -> Node:
    start = Node(0, 0, "a", 0)

    for idx_y, line in enumerate(grid):
        if "S" in line:
            for idx_x, letter in enumerate(line):
                if letter == "S":
                    start = Node(idx_x, idx_y, "a", 0)
                    break

    return start


def get_all_start(grid: list[list[str]]) -> list[Node]:
    start = []

    for idx_y, line in enumerate(grid):
        if "S" in line or "a" in line:
            for idx_x, letter in enumerate(line):
                if letter in ["S", "a"]:
                    start.append(Node(idx_x, idx_y, "a", 0))

    return start


def check_available_neighbours(grid: list[list[str]], node: Node) -> list[Node]:
    ALPHABET: str = string.ascii_lowercase

    node_available: list[Node] = []

    MOVES = [
        (node.x - 1, node.y),
        (node.x + 1, node.y),
        (node.x, node.y - 1),
        (node.x, node.y + 1),
    ]

    CURRENT_LETTER = grid[node.y][node.x]

    if CURRENT_LETTER != "S":
        CURRENT_LETTER_IDX = ALPHABET.index(CURRENT_LETTER)
    else:
        CURRENT_LETTER_IDX = 0

    possible_letters = ALPHABET[: CURRENT_LETTER_IDX + 2]

    if CURRENT_LETTER in ("y", "z"):
        possible_letters += "E"

    for next_x, next_y in MOVES:
        if (
            0 <= next_x < len(grid[0])
            and 0 <= next_y < len(grid)
            and grid[next_y][next_x] in possible_letters
        ):
            node_available.append(
                Node(next_x, next_y, grid[next_y][next_x], node.score + 1)
            )

    return node_available


def solve(instruction_list, part):
    grid: list[list[str]] = [list(line) for line in instruction_list]

    if part == 1:
        all_start_nodes = [get_start(grid)]
    else:
        all_start_nodes = get_all_start(grid)

    all_end_nodes: list[Node] = []

    for start_node in all_start_nodes:
        end = Node(0, 0, "E", 0)

        visited: set[tuple[int, int]] = {(start_node.x, start_node.y)}
        queue: list[Node] = [start_node]

        while queue:
            node = queue.pop(0)

            if node.letter == "E":
                end = node

                break

            node_available_list = check_available_neighbours(grid, node)

            for next_node in node_available_list:
                if (next_node.x, next_node.y) not in visited:
                    queue.append(next_node)
                    visited.add((next_node.x, next_node.y))

        # print(start_node)
        all_end_nodes.append(copy.copy(end))

    # Get minimum of path length
    min_score = 1000000
    for node in all_end_nodes:
        if node.score != 0 and node.score < min_score:
            min_score = node.score

    return min_score


if __name__ == "__main__":
    with open("./2022/day12/test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
