import pathlib
import collections


def track_beam(instruction_list) -> tuple[dict[int, int], int]:
    start_x = [x for x, char in enumerate(instruction_list[0]) if char == "S"][0]
    Y_MAX = len(instruction_list)
    nb_split = 0

    beams_queue = [start_x]
    beam_dict = collections.defaultdict(int)
    beam_dict[start_x] = 1

    for y in range(Y_MAX - 1):
        beams_tmp = set()
        while beams_queue:
            x = beams_queue.pop(0)
            if instruction_list[y + 1][x] == "^":
                nb_split += 1
                beam_dict[x - 1] += beam_dict[x]
                beam_dict[x + 1] += beam_dict[x]
                beam_dict[x] = 0

                beams_tmp.add(x - 1)
                beams_tmp.add(x + 1)
            else:
                beams_tmp.add(x)

        beams_queue = list(beams_tmp).copy()

    return beam_dict, nb_split


def part1(instruction_list) -> int:
    _, nb_split = track_beam(instruction_list)

    return nb_split


def part2(instruction_list) -> int:
    beam_dict, _ = track_beam(instruction_list)

    return sum(beam_dict.values())


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list.copy())}")
    print(f"Part 2: {part2(instruction_list)}")
