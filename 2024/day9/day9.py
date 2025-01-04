import pathlib


def part1(instruction_list):
    amphipod = instruction_list[0].strip()

    disk_map = []

    i = 0
    id = 0
    for j, nb in enumerate(amphipod):
        nb = int(nb)
        if j % 2 == 0:
            for k in range(nb):
                disk_map.append((k + i, id))
            i += k + 1
            id += 1
        else:
            i += nb

    len_disk_map = len(disk_map)

    for i in range(len_disk_map):
        if i != disk_map[i][0]:
            disk_map[-1] = (i, disk_map[-1][1])
            disk_map = disk_map[:i] + [disk_map[-1]] + disk_map[i:-1]

    total = 0
    for i, idx in disk_map:
        total += i * idx

    print(f"Part 1: {total}")
    return total


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
