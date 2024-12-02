f = open("./day13/input.txt")

instruction_list = f.readlines()

departure = int(instruction_list[0])
bus_list = instruction_list[1].split(",")

min_bus = 1000
min_bus_number = 0

for bus_id in bus_list:
    if bus_id != 'x' and min_bus > int(bus_id) - (departure % int(bus_id)):
        min_bus = int(bus_id) - (departure % int(bus_id))
        min_bus_number = int(bus_id)

print(min_bus_number, min_bus)
print(min_bus_number * min_bus)

f.close()
