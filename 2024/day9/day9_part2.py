import itertools
import pathlib


def part2(instruction_list):
    amphipod = instruction_list[0].strip()
    amphipod += "0"

    free_indexes = []
    taken_indexes = {}

    idx = 0
    for id_number, (nb_taken_space, nb_free_space) in enumerate(
        itertools.batched(amphipod, 2)
    ):
        taken_indexes[id_number] = [i + idx for i in range(int(nb_taken_space))]
        free_indexes.append((int(nb_free_space), idx + int(nb_taken_space)))

        idx += int(nb_taken_space) + int(nb_free_space)

    for idx in range(max(taken_indexes.keys()), -1, -1):
        free_indexes.sort(key=lambda x: x[1])
        for nb_free_space, free_idx in free_indexes:
            nb_space_required = len(taken_indexes[idx])
            if nb_space_required <= nb_free_space and free_idx <= taken_indexes[idx][0]:
                free_indexes.remove((nb_free_space, free_idx))
                if nb_space_required != nb_free_space:
                    free_indexes.append(
                        (
                            nb_free_space - nb_space_required,
                            free_idx + nb_space_required,
                        )
                    )

                taken_indexes[idx] = [
                    i + free_idx for i in range(int(nb_space_required))
                ]
                break

    total = 0
    for id_number, idx_list in taken_indexes.items():
        total += sum([id_number * idx for idx in idx_list])

    return total


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 2: {part2(instruction_list)}")
