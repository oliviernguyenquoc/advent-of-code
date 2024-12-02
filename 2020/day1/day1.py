with open('./day1/input.txt') as f:
    arr = f.readlines()

# Can't x > 1010 to fullfill a*x = 2020 with a > 1
arr = [int(nb) for nb in arr]

print(len(arr))
#print(arr)

for i in arr:
    for j in arr:
        if i+j == 2020 and i!=j:
            break
    if i+j == 2020 and i!=j:
        break

print((i, j))
print(i*j)