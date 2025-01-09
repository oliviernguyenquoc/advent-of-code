import string
import pathlib


def part2(passport_list):
    nb_valid_passport = 0
    required_field_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    passport_list = "".join(passport_list).split("\n\n")
    for passport in passport_list:
        passport = passport.replace("\n", " ").strip()
        field_list = passport.split(" ")
        field_dict = {field.split(":")[0]: field.split(":")[1] for field in field_list}

        valid_passport = True

        if all(required_field in field_dict for required_field in required_field_list):
            for field, value in field_dict.items():
                if field == "byr":
                    if not (
                        value.isdigit() and int(value) >= 1920 and int(value) <= 2002
                    ):
                        valid_passport = False

                if field == "iyr":
                    if not (
                        value.isdigit() and int(value) >= 2010 and int(value) <= 2020
                    ):
                        valid_passport = False

                if field == "eyr":
                    if not (
                        value.isdigit() and int(value) >= 2020 and int(value) <= 2030
                    ):
                        valid_passport = False

                if field == "hgt":
                    if value[-2:] == "cm":
                        if not (
                            value[:-2].isdigit()
                            and int(value[:-2]) >= 150
                            and int(value[:-2]) <= 193
                        ):
                            valid_passport = False
                    elif value[-2:] == "in":
                        if not (
                            value[:-2].isdigit()
                            and int(value[:-2]) >= 59
                            and int(value[:-2]) <= 76
                        ):
                            valid_passport = False
                    else:
                        valid_passport = False

                if field == "hcl":
                    if not (
                        len(value) == 7
                        and value[0] == "#"
                        and all(c in string.hexdigits for c in value[1:])
                    ):
                        valid_passport = False

                if field == "ecl":
                    if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        valid_passport = False

                if field == "pid":
                    if not (value.isdigit() and len(value) == 9):
                        valid_passport = False

            if valid_passport:
                nb_valid_passport += 1

    return nb_valid_passport


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
