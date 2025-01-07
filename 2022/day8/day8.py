def part1(instruction_list):
    forest = []

    for instruction in instruction_list:
        forest.append([int(tree) for tree in instruction])

    n = len(instruction_list[0])
    m = len(instruction_list)

    visible_tree_matrix: list[list[bool]] = [
        [False for _ in range(n)] for _ in range(m)
    ]

    for i, line_tree in enumerate(forest):
        max_height: int = -1

        # Left to right
        for j, height_tree in enumerate(line_tree):
            if height_tree > max_height:
                visible_tree_matrix[i][j] = True
                max_height = height_tree

        max_height: int = -1
        # Right to left
        for j, height_tree in enumerate(line_tree[::-1]):
            if height_tree > max_height:
                visible_tree_matrix[i][-j - 1] = True
                max_height = height_tree

    for i in range(m):
        # Top to bottom
        line_tree = [line[i] for line in forest]

        max_height: int = -1

        # Left to right
        for j, height_tree in enumerate(line_tree):
            if height_tree > max_height:
                visible_tree_matrix[j][i] = True
                max_height = height_tree

        max_height: int = -1
        # Right to left
        for j, height_tree in enumerate(line_tree[::-1]):
            if height_tree > max_height:
                visible_tree_matrix[-j - 1][i] = True
                max_height = height_tree

    total_nb_tree = sum([sum(line_tree) for line_tree in visible_tree_matrix])
    return total_nb_tree


if __name__ == "__main__":
    with open("./day8/input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
