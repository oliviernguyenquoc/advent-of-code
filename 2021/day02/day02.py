import pathlib


def part1(instruction_list):
    horizontal_position = 0
    depth_position = 0

    for instruction in instruction_list:
        move, intensity = instruction.split()
        match move:
            case "forward":
                horizontal_position += int(intensity)
            case "down":
                depth_position += int(intensity)
            case "up":
                depth_position -= int(intensity)

    return horizontal_position * depth_position


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
