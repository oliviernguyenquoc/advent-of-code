def get_stats_from_letter(
    letter: str, x: int, y: int, visited: set[tuple[int, int]] = set()
) -> tuple[int, int, set[tuple[int, int]]]:
    DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

    surface, perimeter = 1, 0

    for direction in DIRECTIONS:
        visited.add((x, y))
        if (
            0 <= x + direction[0] < len(grid[0])
            and 0 <= y + direction[1] < len(grid)
            and grid[y + direction[1]][x + direction[0]] == letter
        ):
            if (x + direction[0], y + direction[1]) not in visited:
                tmp_surface, tmp_perimeter, tmp_visited = get_stats_from_letter(
                    letter,
                    x + direction[0],
                    y + direction[1],
                    visited=visited,
                )
                surface += tmp_surface
                perimeter += tmp_perimeter
                visited.update(tmp_visited)
        else:
            perimeter += 1

    return surface, perimeter, visited


with open("./2024/day12/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

global grid

grid = [instruction.strip() for instruction in instruction_list]


visited = set()
total = 0

for y, line in enumerate(grid):
    for x, letter in enumerate(line):
        surface, perimeter = 0, 0
        if (x, y) not in visited:
            tmp_surface, tmp_perimeter, tmp_visited = get_stats_from_letter(
                letter, x, y
            )
            surface += tmp_surface
            perimeter += tmp_perimeter
            visited.update(tmp_visited)
            total += surface * perimeter


print(f"Part 1: {total}")
