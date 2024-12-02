f = open("./day4/input.txt")

nb_valid_passport = 0
required_field_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passport_list = f.readlines()
passport_list = "".join(passport_list).split("\n\n")
for passport in passport_list:
    passport = passport.replace("\n", " ").strip()
    field_list = passport.split(" ")
    field_dict = {field.split(":")[0]: field.split(":")[1] for field in field_list}

    if all(required_field in field_dict for required_field in required_field_list):
        nb_valid_passport += 1

print(nb_valid_passport)

f.close()
