f = open("./day5/input.txt")

seat_list = f.readlines()

seat_position_list = []

for seat in seat_list:
    min_row = 0
    max_row = 128
    min_col = 0
    max_col = 8

    for instruction in seat:
        #print(instruction)
        if instruction == "F":
            max_row = max_row - ((max_row - min_row) // 2)
        elif instruction == "B":
            min_row = min_row + ((max_row - min_row) // 2)
        elif instruction == "R":
            min_col = min_col + ((max_col - min_col) // 2)
        elif instruction == "L":
            max_col = max_col - ((max_col - min_col) // 2)

    if min_row == max_row - 1 and min_col == max_col - 1:
        seat_position_list.append((min_row, min_col))
    else:
        print("ERROR")

print(seat_position_list)

max_id = 0

for row, col in seat_position_list:
    if 8 * row + col > max_id:
        max_id = 8 * row + col

print(max_id)

f.close()
