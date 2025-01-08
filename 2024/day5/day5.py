from collections import defaultdict
import pathlib


def solve(instruction_list, part=1):
    i = 0
    rules = defaultdict(set)

    while instruction_list[i] != "":
        nb1, nb2 = instruction_list[i].split("|")
        rules[int(nb1)].add(int(nb2))
        i += 1

    i += 1
    update_list = []
    for j in range(i, len(instruction_list)):
        update_list.append([int(nb) for nb in instruction_list[j].split(",")])

    # Part 1
    update_ok = []
    update_not_ok = []

    for programmed_update in update_list:
        seen = set()
        is_rule_broken = False
        for nb in programmed_update:
            if seen.intersection(rules[nb]) == set():
                seen.add(nb)
            else:
                is_rule_broken = True

        if not is_rule_broken:
            update_ok.append(programmed_update)
        else:
            update_not_ok.append(programmed_update)

    middle_list = [upd[len(upd) // 2] for upd in update_ok]

    if part == 1:
        return sum(middle_list)

    # Part 2
    update_corrected = []
    for programmed_update in update_not_ok:
        i = 0
        seen = set()
        while i < len(programmed_update):
            nb = programmed_update[i]
            while seen.intersection(rules[nb]) != set():
                if i >= 0:
                    seen.remove(programmed_update[i - 1])
                programmed_update = (
                    programmed_update[: i - 1]
                    + [programmed_update[i]]
                    + [programmed_update[i - 1]]
                    + programmed_update[i + 1 :]
                )
                i -= 1

            seen.add(programmed_update[i])
            i += 1
        update_corrected.append(programmed_update)

    middle_list = [upd[len(upd) // 2] for upd in update_corrected]

    return sum(middle_list)


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {solve(instruction_list, part=1)}")
    print(f"Part 2: {solve(instruction_list, part=2)}")
