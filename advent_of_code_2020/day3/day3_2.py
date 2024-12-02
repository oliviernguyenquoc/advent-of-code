from functools import reduce

f = open("./day3/input.txt")

map_list = f.readlines()

nb_tree_list = []
direction_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(direction_list)
for direction in direction_list:
    nb_tree = 0
    for n_line, line in enumerate(map_list):
        if (
            n_line % direction[1] == 0
            and line[(n_line // direction[1] * direction[0]) % (len(line) - 1)] == "#"
        ):
            nb_tree += 1

    nb_tree_list.append(nb_tree)

print(nb_tree_list)
print(reduce((lambda x,y: x*y), nb_tree_list))

f.close()
