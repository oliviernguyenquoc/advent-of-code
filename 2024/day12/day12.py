import itertools
import pathlib


def get_stats_from_letter(
    letter: str, x: int, y: int, visited: set[tuple[int, int]] = set()
) -> tuple[int, int, set[tuple[int, int]]]:
    DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

    for direction in DIRECTIONS:
        visited.add((x, y))
        if (
            0 <= x + direction[0] < len(grid[0])
            and 0 <= y + direction[1] < len(grid)
            and grid[y + direction[1]][x + direction[0]] == letter
        ):
            if (x + direction[0], y + direction[1]) not in visited:
                tmp_visited = get_stats_from_letter(
                    letter,
                    x + direction[0],
                    y + direction[1],
                    visited=visited,
                )
                visited.update(tmp_visited)

    return visited


def get_perimeter(visited: set[tuple[int, int]]) -> int:
    total = len(visited) * 4
    for (x1, y1), (x2, y2) in itertools.combinations(visited, 2):
        if (abs(x2 - x1) == 1 and abs(y2 - y1) == 0) or (
            abs(x2 - x1) == 0 and abs(y2 - y1) == 1
        ):
            total -= 2

    return total


def get_nb_sides(perimeter: int, visited: set[tuple[int, int]]) -> int:
    total = perimeter
    for (x1, y1), (x2, y2) in itertools.combinations(visited, 2):
        if abs(x2 - x1) == 1 and abs(y2 - y1) == 0:
            if (x1, y1 + 1) not in visited and (x2, y2 + 1) not in visited:
                total -= 1
            if (x1, y1 - 1) not in visited and (x2, y2 - 1) not in visited:
                total -= 1

        if abs(x2 - x1) == 0 and abs(y2 - y1) == 1:
            if (x1 + 1, y1) not in visited and (x2 + 1, y2) not in visited:
                total -= 1
            if (x1 - 1, y1) not in visited and (x2 - 1, y2) not in visited:
                total -= 1

    return total


def solve(instruction_list, part=1):
    global grid

    grid = [instruction.strip() for instruction in instruction_list]

    visited = set()
    total = 0

    for y, line in enumerate(grid):
        for x, letter in enumerate(line):
            surface = 0
            if (x, y) not in visited:
                tmp_visited = get_stats_from_letter(letter, x, y, visited=set())
                visited.update(tmp_visited)

                surface = len(tmp_visited)
                perimeter = get_perimeter(tmp_visited)
                nb_sides = get_nb_sides(perimeter, tmp_visited)

                if part == 1:
                    total += surface * perimeter
                else:
                    total += surface * nb_sides

    print(f"Part {part}: {total}")
    return total


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    solve(instruction_list, part=1)
    solve(instruction_list, part=2)
