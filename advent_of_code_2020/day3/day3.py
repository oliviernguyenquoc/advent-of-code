f = open("./day3/input.txt")

map_list = f.readlines()

nb_tree = 0

for n_line, line in enumerate(map_list):
    if line[(n_line * 3) % (len(line)-1)] == "#":
        nb_tree += 1

print(nb_tree)

f.close()
