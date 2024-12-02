def get_part2_exemple_dict():
    teleport_dict = {}

    for i in range(4):
        teleport_dict.update({(12, i, "R"): (15, 11 - i, "L")})
        teleport_dict.update({(16, 11 - i, "R"): (11, i, "L")})

        teleport_dict.update({(7, i, "L"): (4 + i, 4, "D")})
        teleport_dict.update({(4 + i, 3, "U"): (8, i, "R")})

        teleport_dict.update({(8 + i, -1, "U"): (3 - i, 4, "D")})
        teleport_dict.update({(3 - i, 3, "U"): (8 + i, 0, "D")})

        teleport_dict.update({(-1, 4 + i, "L"): (15 - i, 11, "U")})
        teleport_dict.update({(15 - i, 12, "D"): (0, 4 + i, "R")})

        teleport_dict.update({(4 + i, 8, "D"): (8, 11 - i, "R")})
        teleport_dict.update({(7, 11 - i, "L"): (4 + i, 7, "U")})

        teleport_dict.update({(12 + i, 7, "U"): (11, 7 - i, "L")})
        teleport_dict.update({(12, 7 - i, "R"): (12 + i, 8, "D")})

        teleport_dict.update({(8 + i, 12, "D"): (3 - i, 7, "U")})
        teleport_dict.update({(3 - i, 8, "D"): (8 + i, 11, "U")})

    return teleport_dict


def get_part2_dict():
    teleport_dict = {}

    for i in range(50):
        teleport_dict.update({(50 + i, -1, "U"): (0, 150 + i, "R")})
        teleport_dict.update({(-1, 150 + i, "L"): (50 + i, 0, "D")})

        teleport_dict.update({(49, i, "L"): (0, 149 - i, "R")})
        teleport_dict.update({(-1, 149 - i, "L"): (50, i, "R")})

        teleport_dict.update({(150, i, "R"): (99, 149 - i, "L")})
        teleport_dict.update({(100, 149 - i, "R"): (149, i, "L")})

        teleport_dict.update({(100 + i, -1, "U"): (i, 199, "U")})
        teleport_dict.update({(i, 200, "D"): (100 + i, 0, "D")})

        teleport_dict.update({(100 + i, 50, "D"): (99, 50 + i, "L")})
        teleport_dict.update({(100, 50 + i, "R"): (100 + i, 49, "U")})

        teleport_dict.update({(49, 50 + i, "L"): (i, 100, "D")})
        teleport_dict.update({(i, 99, "U"): (50, 50 + i, "R")})

        teleport_dict.update({(50, 150 + i, "R"): (50 + i, 149, "U")})
        teleport_dict.update({(50 + i, 150, "D"): (49, 150 + i, "L")})

    return teleport_dict


def check_dict(teleport_dict, quare_len=20):
    for i in range(-1, quare_len + 1):
        line = ""
        for j in range(-1, quare_len + 1):
            if (j, i, "U") in teleport_dict:
                line += "^"
            elif (j, i, "D") in teleport_dict:
                line += "v"
            elif (j, i, "R") in teleport_dict:
                line += ">"
            elif (j, i, "L") in teleport_dict:
                line += "<"
            else:
                line += " "

        print(line)


t_dict = get_part2_exemple_dict()
check_dict(t_dict, quare_len=20)

t_dict = get_part2_dict()
print(len(t_dict))
print(len(list(set(t_dict))))
check_dict(t_dict, quare_len=200)
