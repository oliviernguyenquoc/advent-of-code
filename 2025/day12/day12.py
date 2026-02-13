import pathlib


class Shape:

    @staticmethod
    def _vertical_flip(geometry: list[str]) -> list[str]:
        return [geometry[2], geometry[1], geometry[0]]

    @staticmethod
    def _horizontal_flip(geometry: list[str]) -> list[str]:
        return [row[::-1] for row in geometry]

    @staticmethod
    def _turn_right(geometry: list[str]) -> list[str]:
        return [
            "".join([geometry[2][i], geometry[1][i], geometry[0][i]]) for i in range(3)
        ]

    @classmethod
    def get_all_possible_orientation(cls, initial_geometry: list[str]) -> list[list[str]]:
        return [
                initial_geometry,
                cls._turn_right(initial_geometry),
                cls._turn_right(cls._turn_right(initial_geometry)),
                cls._turn_right(cls._turn_right(cls._turn_right(initial_geometry))),

                cls._vertical_flip(initial_geometry),
                cls._horizontal_flip(initial_geometry),
                cls._turn_right(cls._vertical_flip(initial_geometry)),
                cls._turn_right(cls._horizontal_flip(initial_geometry))
        ]
        
    def __init__(self, initial_geometry: list[str], idx: int):
        self.orientations = self.get_all_possible_orientation(initial_geometry)
        self.idx = idx


def parse_data(
    instruction_list,
) -> tuple[list[Shape], list[tuple[tuple[int, int], list[int]]]]:
    shapes = []
    for i in range(6):
        geometry = instruction_list[5 * i].strip()
        geometry.append(instruction_list[5 * i + 1].strip())
        geometry.append(instruction_list[5 * i + 2].strip())
        shapes.append(Shape(geometry=geometry, idx=i))

    spaces = []
    for instruction in instruction_list[31:]:
        space, present_str_list = instruction.split(": ")
        length_str, width_str = space.split("x")
        present_list = [int(present) for present in present_str_list.split(" ")]
        spaces.append([((int(length_str), int(width_str)), present_list)])

    return shapes, spaces


def part1(instruction_list) -> int:
    return 0


def part2(instruction_list) -> int:
    return 0


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list)}")

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 2: {part2(instruction_list)}")
    # Too low: 9896858887860 et 98968588878600
