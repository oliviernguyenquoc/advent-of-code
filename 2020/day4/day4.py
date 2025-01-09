import pathlib


def part1(passport_list):
    nb_valid_passport = 0
    required_field_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    passport_list = "".join(passport_list).split("\n\n")
    for passport in passport_list:
        passport = passport.replace("\n", " ").strip()
        field_list = passport.split(" ")
        field_dict = {field.split(":")[0]: field.split(":")[1] for field in field_list}

        if all(required_field in field_dict for required_field in required_field_list):
            nb_valid_passport += 1

    return nb_valid_passport


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 1: {part1(instruction_list)}")
