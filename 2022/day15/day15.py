import re
from dataclasses import dataclass
import pathlib

X_MIN, X_MAX, Y_MIN, Y_MAX = 0, 4000000, 0, 4000000  # 0, 20, 0, 20


@dataclass
class Radar:
    sensor: tuple[int, int]
    beacon: tuple[int, int]

    def get_distance(self) -> int:
        return (
            max(self.sensor[0], self.beacon[0]) - min(self.sensor[0], self.beacon[0])
        ) + (max(self.sensor[1], self.beacon[1]) - min(self.sensor[1], self.beacon[1]))


@dataclass
class Environment:
    points: dict[tuple[int, int], str]

    def add_beacon(self, x: int, y: int):
        self.points[(x, y)] = "B"

    def add_sensor(self, x: int, y: int):
        self.points[(x, y)] = "S"

    def marked_as_occupied(
        self, sensor_x: int, sensor_y: int, distance: int, row_checked: int
    ):
        """PART 1: Check only the row we are looking for"""

        for i in range(sensor_x - distance, sensor_x + distance):
            j = row_checked
            distance_sensor_to_point = (max(sensor_x, i) - min(sensor_x, i)) + (
                max(sensor_y, j) - min(sensor_y, j)
            )
            if distance_sensor_to_point <= distance:
                if (i, j) not in self.points and j == row_checked:
                    self.points[(i, j)] = "#"

    def marked_as_potential_detress(self, sensor_x: int, sensor_y: int, distance: int):
        """Mark all intersection of radars (Potential distress point to reduce the number of points to check)"""

        all_edge_points = []
        for i in range(distance):
            all_edge_points += [
                (sensor_x + i, sensor_y + i - distance),
                (sensor_x + i, sensor_y + i + distance),
                (sensor_x + i - distance, sensor_y + i),
                (sensor_x + i + distance, sensor_y + i),
            ]

        for i, j in all_edge_points:
            if X_MIN < i < X_MAX and Y_MIN < j < Y_MAX:
                if (i, j) not in self.points:
                    self.points[(i, j)] = "?"
                elif self.points[(i, j)] == "?":
                    self.points[(i, j)] = "X"

    def check_potential_detress(self, sensor_x: int, sensor_y: int, distance: int):
        potential_detress = [
            point for point, type in self.points.items() if type == "X"
        ]

        for detress_x, detress_y in potential_detress:
            distance_to_point = (
                max(sensor_x, detress_x) - min(sensor_x, detress_x)
            ) + (max(sensor_y, detress_y) - min(sensor_y, detress_y))

            if distance_to_point <= distance:
                self.points[detress_x, detress_y] = "#"


def part1(instruction_list, is_test):
    if is_test:
        ROW_CHECKED = 10
    else:
        ROW_CHECKED = 2000000

    environment = Environment({})

    for instruction in instruction_list:
        sensor_x, sensor_y, beacon_x, beacon_y = re.findall(
            r"Sensor at x=([^,]*), y=([^:]*): closest beacon is at x=([^,]*), y=([^:]*)",
            instruction,
        )[0]
        sensor = (int(sensor_x), int(sensor_y))
        beacon = (int(beacon_x), int(beacon_y))
        radar = Radar(sensor=sensor, beacon=beacon)
        environment.add_beacon(*beacon)
        environment.add_sensor(*sensor)
        environment.marked_as_occupied(
            *sensor, radar.get_distance(), row_checked=ROW_CHECKED
        )

    return len(
        [
            point
            for point, type in environment.points.items()
            if type == "#" and point[1] == ROW_CHECKED
        ]
    )


def part2(instruction_list):
    environment = Environment({})
    # beacon_list = {}

    for instruction in instruction_list:
        print(instruction)
        sensor_x, sensor_y, beacon_x, beacon_y = re.findall(
            r"Sensor at x=([^,]*), y=([^:]*): closest beacon is at x=([^,]*), y=([^:]*)",
            instruction,
        )[0]
        sensor = (int(sensor_x), int(sensor_y))
        beacon = (int(beacon_x), int(beacon_y))
        radar = Radar(sensor=sensor, beacon=beacon)
        environment.add_beacon(*beacon)
        environment.add_sensor(*sensor)
        environment.marked_as_potential_detress(*sensor, radar.get_distance() + 1)

    print("Number of potential distress points:")
    print(len([point for point, type in environment.points.items() if type == "X"]))

    for instruction in instruction_list:
        print(instruction)
        sensor_x, sensor_y, beacon_x, beacon_y = re.findall(
            r"Sensor at x=([^,]*), y=([^:]*): closest beacon is at x=([^,]*), y=([^:]*)",
            instruction,
        )[0]
        sensor = (int(sensor_x), int(sensor_y))
        beacon = (int(beacon_x), int(beacon_y))
        radar = Radar(sensor=sensor, beacon=beacon)
        environment.check_potential_detress(*sensor, radar.get_distance())

    print("Coordinate of distress point:")
    print([point for point, type in environment.points.items() if type == "X"])
    distress_signal = [
        point for point, type in environment.points.items() if type == "X"
    ][0]

    return distress_signal[0] * 4000000 + distress_signal[1]


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list, is_test=False)}")
    print(f"Part 2: {part2(instruction_list)}")
