from typing import Dict, List, Tuple
import math


class Tile:
    def __init__(self, name: str, code: List[str]):
        self.name = name
        self.code = code
        self.code_size = len(code[0])
        self.borders = []
        if name[-4:].isdigit():
            self.number = int(name[-4:])
        self.get_borders()

    def get_borders(self):
        self.borders = [
            self.code[0],
            "".join([i[-1] for i in self.code]),
            self.code[-1][::-1],
            "".join([i[0] for i in self.code][::-1]),
        ]

        # Inverse Right and left when flipped
        self.borders += [self.borders[i][::-1] for i in range(4)]

    def turn_tile(self, nb_quarter: int):
        new_code = []
        if (nb_quarter % 4) == 0:
            new_code = self.code
        if (nb_quarter % 4) == 1:
            for i in range(self.code_size):
                new_str = ""
                for j in reversed(range(self.code_size)):
                    new_str += self.code[j][i]
                new_code.append(new_str)
        if (nb_quarter % 4) == 2:
            for i in range(self.code_size):
                new_code.append(self.code[-i - 1][::-1])
        if (nb_quarter % 4) == 3:
            for i in range(self.code_size):
                new_str = ""
                for j in range(self.code_size):
                    new_str += self.code[j][-i - 1]
                new_code.append(new_str)

        self.code = new_code
        self.get_borders()

    def flip_horizontal_tile(self):
        self.code = [self.code[-i - 1] for i in range(self.code_size)]
        self.get_borders()

    def delete_borders(self):
        self.code = self.code[1:-1]
        self.code = [row[1:-1] for row in self.code]
        self.code_size = self.code_size - 2

    def __repr__(self):
        return f"<{self.name}>"

    def count_nb_monster(self, sea_monster_list: List[Tuple[int, int]])->int:
        nb_monster = 0
        for i in range(self.code_size-2):
            for j in range(self.code_size-19):
                if all([self.code[i+k][j+l] == "#" for k, l in sea_monster_list]):
                    nb_monster +=1

        return nb_monster

    def count_ones(self):
        nb = 0
        for row in self.code:
            nb += row.count('#')
        
        return nb

    # def __str__(self):
    #     return "\n".join(self.code)


def find_match(tile_dict: Dict[str, Tile]) -> Dict[str, Tile]:
    adjacent_dict = {tile_name: [] for tile_name in tile_dict}

    for tile_name_1, tile_1 in tile_dict.items():
        for tile_name_2, tile_2 in tile_dict.items():
            if tile_name_1 != tile_name_2 and any(
                x in tile_1.borders for x in tile_2.borders
            ):
                adjacent_dict[tile_name_1].append(tile_dict[tile_name_2])

    return adjacent_dict


f = open("./day20/input.txt")

tiles_list = "".join(f.readlines()).split("\n\n")

f.close()

tile_dict = {}

for tile in tiles_list:
    tile_name, tile_code = tile.split(":")
    tile_code_list = tile_code[1:].split("\n")

    tile_dict[tile_name] = Tile(name=tile_name, code=tile_code_list)

adjacent_dict = find_match(tile_dict)

corner_tile_list = []

# Find corners
for tile_name, tile_match_list in adjacent_dict.items():
    if len(tile_match_list) == 2:
        corner_tile_list.append(tile_dict[tile_name])

print(f"Part 1: {math.prod([tile.number for tile in corner_tile_list])}")


def get_right_tile(
    adjacent_dict: Dict[str, Tile],
    tile_dict: Dict[str, Tile],
    corner_tile: Tile,
    side: int,
    already_used_tile_names: List[str] = [],
) -> Tuple[str, int]:

    connected_tile_names = [tile.name for tile in adjacent_dict[corner_tile.name]]
    tile_name_1, tile_name_2 = list(
        set(connected_tile_names) - set(already_used_tile_names)
    )
    adjacent_tile_1 = tile_dict[tile_name_1]
    adjacent_tile_2 = tile_dict[tile_name_2]

    for j in range(8):
        for k in range(8):
            if (
                corner_tile.borders[side] == adjacent_tile_1.borders[j]
                and corner_tile.borders[(side + 1) % 4] == adjacent_tile_2.borders[k]
            ):
                return (adjacent_tile_1, j)
            elif (
                corner_tile.borders[side] == adjacent_tile_2.borders[j]
                and corner_tile.borders[(side + 1) % 4] == adjacent_tile_1.borders[k]
            ):
                return (adjacent_tile_2, j)
    return None


def get_down_tile(
    adjacent_dict: Dict[str, Tile],
    tile_dict: Dict[str, Tile],
    corner_tile: Tile,
    side: int,
    already_used_tile_names: List[str] = [],
) -> Tuple[str, int]:

    connected_tile_names = [tile.name for tile in adjacent_dict[corner_tile.name]]
    tile_name = list(set(connected_tile_names) - set(already_used_tile_names))
    adjacent_tile = tile_dict[tile_name[0]]

    for i in range(8):
        if corner_tile.borders[side] == adjacent_tile.borders[i]:
            return (adjacent_tile, i)

    return None


def print_tiles(tile_list: List[Tile], len_final_square: int, limit: int = None):
    if not limit or limit > len_final_square:
        limit = len_final_square
    for j in range(limit):
        for i in range(tile_list[0].code_size):
            print(
                " ".join(
                    [
                        tile.code[i]
                        for tile in tile_list[
                            j * len_final_square : len_final_square * (j + 1)
                        ]
                    ]
                )
            )
        print("\n")


corner_tile = corner_tile_list[0]

already_used_tile_names = []
rearranged_tiles = []

# For the first corner
i = 0
right_tile = get_right_tile(adjacent_dict, tile_dict, corner_tile, i)
while right_tile is None:
    i += 1
    right_tile = get_right_tile(adjacent_dict, tile_dict, corner_tile, i)

    if i > 4:
        print("ISSUE")
        exit(1)


already_used_tile_names += [corner_tile.name]

corner_tile.turn_tile(5 - i)

rearranged_tiles.append(corner_tile)
len_final_square = int(math.sqrt(len(tile_dict)))

# Order / turn tiles in the first row (Going from top left corner to the tiles at the direct right)
print("--- Row 0 ----")
for col in range(len_final_square - 1):

    print(f"-------- Col {col} ---------")
    adjacent_tile, j = get_right_tile(
        adjacent_dict, tile_dict, corner_tile, 1, already_used_tile_names
    )
    adjacent_tile.turn_tile(7 - j)
    if j < 4:
        adjacent_tile.flip_horizontal_tile()

    corner_tile = adjacent_tile
    rearranged_tiles.append(adjacent_tile)
    already_used_tile_names.append(adjacent_tile.name)

# Order / turn tiles in the other rows (finding tile of the bottom of the first line ...)
for row in range(1, len_final_square):
    print(f"--- Row {row} ----")

    for col in range(len_final_square):
        print(f"--- Col {col} ----")

        adjacent_tile, j = get_down_tile(
            adjacent_dict,
            tile_dict,
            rearranged_tiles[(row - 1) * len_final_square + col],
            2,
            already_used_tile_names,
        )

        if j < 4:
            adjacent_tile.turn_tile(6 - j)
        else:
            adjacent_tile.turn_tile(4 - j)
        if j < 4:
            adjacent_tile.flip_horizontal_tile()

        corner_tile = adjacent_tile
        rearranged_tiles.append(adjacent_tile)
        already_used_tile_names.append(adjacent_tile.name)

print_tiles(rearranged_tiles, len_final_square, 1)

# Delete borders
for tile in rearranged_tiles:
    tile.delete_borders()

print("------")
print_tiles(rearranged_tiles, len_final_square, 1)

# Full image
full_image = []
for i in range(len_final_square):
    sub_list = rearranged_tiles[i * len_final_square : len_final_square * (i + 1)]
    for j in range(rearranged_tiles[0].code_size):
        full_image.append("".join([tile.code[j] for tile in sub_list]))

print("------")
for line in full_image[:6]:
    print(line)

image_tile = Tile("Full image", full_image)
see_monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
see_monster_list = [
    (i, j)
    for i in range(len(see_monster))
    for j, char in enumerate(see_monster[i])
    if char == "#"
]

nb_monster = 0

for _ in range(4):
    nb_monster += image_tile.count_nb_monster(see_monster_list)
    image_tile.turn_tile(1)
    print(nb_monster)

image_tile.flip_horizontal_tile()

for _ in range(4):
    nb_monster += image_tile.count_nb_monster(see_monster_list)
    image_tile.turn_tile(1)
    print(nb_monster)

print(image_tile.count_ones(), nb_monster*len(see_monster_list))
print(f"Part 2: {image_tile.count_ones() - (nb_monster*len(see_monster_list))}")


# X/0 => X/270° + Flip H
# X/1 => X/180° + Flip H
# X/2 => X/90° + Flip H
# X/3 => X/ Flip H
# X/4 => X/270°
# X/5 => X/180°
# X/6=> X/90°
# X/7 => Nothing

# 0/X => 90°/X
# 1/X => Nothing
# 2/X => 270°
# 3/X => 180°
# 4/X => 90° + Flip H
# 5/X => Flip H
# 6/X => 270° + Flip H
# 7/X => 180° + Flip H


# {
#     "Tile 2311": ["Tile 1951", "Tile 1427", "Tile 3079"],
#     "Tile 1951": ["Tile 2311", "Tile 2729"],
#     "Tile 1171": ["Tile 1489", "Tile 2473"],
#     "Tile 1427": ["Tile 2311", "Tile 1489", "Tile 2473", "Tile 2729"],
#     "Tile 1489": ["Tile 1171", "Tile 1427", "Tile 2971"],
#     "Tile 2473": ["Tile 1171", "Tile 1427", "Tile 3079"],
#     "Tile 2971": ["Tile 1489", "Tile 2729"],
#     "Tile 2729": ["Tile 1951", "Tile 1427", "Tile 2971"],
#     "Tile 3079": ["Tile 2311", "Tile 2473"],
# }