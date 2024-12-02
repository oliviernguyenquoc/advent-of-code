f = open('./day2/input.txt')

total_true_password = 0

while True:
    arr = f.readline().split()
    if not arr:
        break

    min_letter, max_letter = map(int, arr[0].split("-"))
    letter = arr[1][0]
    password = arr[2]
    print((min_letter, max_letter, letter, password))
    count_letter = password.count(letter)
    if count_letter >= min_letter and count_letter <= max_letter:
        total_true_password+=1

print(total_true_password)
f.close()