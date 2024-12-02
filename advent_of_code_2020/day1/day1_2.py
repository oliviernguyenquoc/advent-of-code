with open('./day1/input.txt') as f:
    arr = f.readlines()

# Can't x > 1010 to fullfill a*x = 2020 with a > 1
arr = [int(nb) for nb in arr]

print(len(arr))

for i in arr:
    for j in arr:
        for k in arr:
            if i+j+k == 2020 and i!=j and j!=k:
                break
        if i+j+k == 2020 and i!=j and j!=k:
            break
    if i+j+k == 2020 and i!=j and j!=k:
            break

print((i, j, k))
print(i*j*k)