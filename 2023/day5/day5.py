import re
import dataclasses


@dataclasses.dataclass
class Range:
    source_range_start: int
    destination_range_start: int
    range_length: int

    @property
    def source_range_end(self):
        return self.source_range_start + self.range_length - 1

    def is_source_inrange(self, nb_to_check: int) -> bool:
        return self.source_range_start <= nb_to_check <= self.source_range_end


@dataclasses.dataclass
class Map:
    source: str
    destination: str
    range_list: list[Range]

    def map_next_point(self, nb_to_check: int) -> int:
        for range in self.range_list:
            if range.is_source_inrange(nb_to_check):
                return range.destination_range_start + (
                    nb_to_check - range.source_range_start
                )

        return nb_to_check

    @classmethod
    def read_instructions(cls, instructions: list[str]):
        instruction = instructions.pop(0)
        source, destination = re.search(
            r"([^-]*)\-to\-([^-]*) map:", instruction
        ).groups()

        maping = cls(source=source, destination=destination, range_list=[])

        instruction = instructions.pop(0)

        while instruction not in ("\n", ""):
            destination_range_start, source_range_start, range_length = re.search(
                r"([0-9]*) ([0-9]*) ([0-9]*)", instruction
            ).groups()

            # Cast to int
            destination_range_start = int(destination_range_start)
            source_range_start = int(source_range_start)
            range_length = int(range_length)

            maping.range_list.append(
                Range(
                    source_range_start=source_range_start,
                    destination_range_start=destination_range_start,
                    range_length=range_length,
                )
            )

            if instructions:
                instruction = instructions.pop(0)
            else:
                break

        return maping


def part1(instructions):
    seed_instruction = instructions.pop(0)
    seed_txt = re.search(r"seeds: ([0-9 ]*)", seed_instruction).groups()
    seeds = [int(seed) for seed in seed_txt[0].split()]

    map_dict = {}

    # Remove new line
    instructions.pop(0)

    while len(instructions) != 0:
        maping = Map.read_instructions(instructions)
        map_dict[maping.source] = maping

    seed_dict: dict[int, int] = {key: 100000000000000 for key in seeds}

    for seed in seeds:
        point = "seed"
        curent_value = seed

        while point != "location":
            maping = map_dict[point]
            curent_value = maping.map_next_point(curent_value)
            point = maping.destination

        seed_dict[seed] = curent_value

    inverted_dict = {value: key for key, value in seed_dict.items()}

    return min(inverted_dict.keys())


if __name__ == "__main__":
    with open("./day5/input.txt", encoding="utf-8") as f:
        instructions: list[str] = f.readlines()

    print(f"Part 1: {part1(instructions)}")
