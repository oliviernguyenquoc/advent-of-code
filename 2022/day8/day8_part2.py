import pathlib


def count_nb_tree_scenic(height: int, trees: list[int]) -> int:
    res = 0
    for tree in trees:
        if tree < height:
            res += 1
        else:
            res += 1
            break

    return res


def part2(instruction_list):
    forest = []

    for instruction in instruction_list:
        forest.append([int(tree) for tree in instruction])

    n = len(instruction_list[0])
    m = len(instruction_list)

    scenic_matrix: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]

    for row in range(m):
        for col in range(n):
            # scenic_for_tree: int = 1
            # Right
            right_scenic = count_nb_tree_scenic(
                height=forest[row][col], trees=forest[row][col + 1 :]
            )

            # Left
            left_scenic = count_nb_tree_scenic(
                height=forest[row][col], trees=forest[row][:col][::-1]
            )

            # Up
            vertical_line_trees: list[int] = [forest[i][col] for i in range(m)]
            up_scenic = count_nb_tree_scenic(
                height=forest[row][col], trees=vertical_line_trees[:row][::-1]
            )

            # Down
            down_scenic = count_nb_tree_scenic(
                height=forest[row][col], trees=vertical_line_trees[row + 1 :]
            )

            scenic_matrix[row][col] = (
                right_scenic * left_scenic * up_scenic * down_scenic
            )

    return max([max(line) for line in scenic_matrix])


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
