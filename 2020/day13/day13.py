import pathlib


def part1(instruction_list):
    departure = int(instruction_list[0])
    bus_list = instruction_list[1].split(",")

    min_bus = 1000
    min_bus_number = 0

    for bus_id in bus_list:
        if bus_id != "x" and min_bus > int(bus_id) - (departure % int(bus_id)):
            min_bus = int(bus_id) - (departure % int(bus_id))
            min_bus_number = int(bus_id)

    print(min_bus_number, min_bus)
    return min_bus_number * min_bus


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()

    print(f"Part 1: {part1(instruction_list)}")
