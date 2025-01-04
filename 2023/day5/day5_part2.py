import re
import dataclasses
import itertools


@dataclasses.dataclass
class Range:
    source_range_start: int
    destination_range_start: int
    range_length: int

    @property
    def source_range_end(self):
        return self.source_range_start + self.range_length - 1

    @property
    def destination_range_end(self):
        return self.destination_range_start + self.range_length - 1

    def is_source_inrange(self, nb_to_check: int) -> bool:
        return self.source_range_start <= nb_to_check <= self.source_range_end

    def is_destination_inrange(self, nb_to_check: int) -> bool:
        return self.destination_range_start <= nb_to_check <= self.destination_range_end


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

    def map_reversed_next_point(self, nb_to_check: int) -> int:
        for range in self.range_list:
            if range.is_destination_inrange(nb_to_check):
                return range.source_range_start + (
                    nb_to_check - range.destination_range_start
                )

    def merge_ranges(self) -> list[tuple[int, int]]:
        start_list = []

        for range in self.range_list:
            start_list.append(
                (
                    range.destination_range_start,
                    range.destination_range_start + range.range_length,
                )
            )

        start_list.sort(key=lambda tup: tup[0])

        for i in len(start_list) - 1:
            if start_list[i][1] <= start_list[i + 1][0]:
                start_list[i][1] = start_list[i + 1][1]
                start_list.pop(i + 1)

        return start_list

    def sort(self):
        self.range_list.sort(key=lambda x: x.destination_range_start)

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

    def get_split_points(self, begin: int, end: int) -> list[tuple[int, int]]:
        split_points = set()
        for range in self.range_list:
            if begin < range.destination_range_start < end:
                split_points.add(range.destination_range_start - 1)
                split_points.add(range.destination_range_start)
            if begin < range.destination_range_end < end:
                split_points.add(range.destination_range_end - 1)
                split_points.add(range.destination_range_end)

        split_points.add(begin)
        split_points.add(end)
        split_points = sorted(split_points)

        return [(a, b) for a, b in itertools.pairwise(split_points)]


if __name__ == "__main__":
    with open("./day5/input.txt", encoding="utf-8") as f:
        instructions: list[str] = f.readlines()

    seed_instruction = instructions.pop(0)
    seed_txt = re.search(r"seeds: ([0-9 ]*)", seed_instruction).groups()
    seeds = [int(seed) for seed in seed_txt[0].split()]

    seed_couples = []

    while seeds:
        seed_range_start = seeds.pop(0)
        seed_range_length = seeds.pop(0)
        seed_couples.append((seed_range_start, seed_range_start + seed_range_length))

    map_dict = {}

    # Remove new line
    instructions.pop(0)

    while len(instructions) != 0:
        maping = Map.read_instructions(instructions)
        map_dict[maping.destination] = maping

    point = "location"

    map_dict["location"].sort()

    res_dict = {}

    segments: list[tuple[int, int]] = []
    for range_location in map_dict["location"].range_list:
        segments.append(
            (
                range_location.destination_range_start,
                range_location.destination_range_end,
            )
        )

        while point != "location":
            while segments:
                segment = segments.pop(0)
                maping = map_dict[point]
                split_points = maping.get_split_points(segment[0], segment[1])
                if split_points:
                    segments += split_points
                curent_value = maping.map_reversed_next_point(segment[0])
                point = maping.source

            if (
                seed_range_start
                <= curent_value
                <= seed_range_start + seed_range_length - 1
            ):
                found = True
                break

    print(found, curent_value)
