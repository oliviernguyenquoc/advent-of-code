f = open('./day2/input2.txt')

total_true_password = 0

while True:
    arr = f.readline().split()
    if not arr:
        break

    min_letter, max_letter = map(int, arr[0].split("-"))
    letter = arr[1][0]
    password = arr[2]
    print((min_letter, max_letter, letter, password))
    if (password[min_letter -1] == letter) != (password[max_letter -1] == letter):
        total_true_password+=1
        print("true")

print(total_true_password)
f.close()